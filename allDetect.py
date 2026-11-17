import cv2
import numpy as np
import time
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open video
video_path = "video.mp4"
cap = cv2.VideoCapture(video_path)

# Class names
CLASSES = model.names

# Flying and ground classes
flying_classes = ['bird', 'airplane', 'kite']
ground_classes = ['person', 'car', 'truck', 'bus', 'bicycle', 'motorcycle']

# Ground line
GROUND_Y = None

# Pixel to meter scale
PIXEL_TO_METER = 0.0175

# FPS
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30

# Store previous positions
previous_positions = {}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()

    # Run YOLO detection
    results = model(frame)[0]
    detections = results.boxes.data.cpu().numpy()

    flying_objects = []
    ground_objects = []

    if GROUND_Y is None:
        GROUND_Y = 0

    # Process detections
    for det in detections:
        
        x1, y1, x2, y2, conf, cls_id = det
        cls_id = int(cls_id)

        class_name = CLASSES[cls_id]

        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)

        if class_name in ground_classes:
            ground_objects.append(((int(x1), int(y1), int(x2), int(y2)), class_name))
            GROUND_Y = max(GROUND_Y, int(y2))

        elif class_name in flying_classes:
            flying_objects.append(((int(x1), int(y1), int(x2), int(y2)),
                                   class_name,
                                   center_x,
                                   center_y))

    # Draw ground line
    cv2.line(frame,
             (0, GROUND_Y),
             (frame.shape[1], GROUND_Y),
             (0, 255, 0),
             2)

    cv2.putText(frame,
                f"Ground Level: Y={GROUND_Y}",
                (10, GROUND_Y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2)

    # Process flying objects
    for idx, ((x1, y1, x2, y2), name, center_x, center_y) in enumerate(flying_objects):

        # Height from ground
        height_px = GROUND_Y - center_y
        height_m = height_px * PIXEL_TO_METER

        # Default speeds
        total_speed = 0
        horizontal_speed = 0
        vertical_speed = 0

        object_id = f"{name}_{idx}"

        # Calculate speed
        if object_id in previous_positions:

            prev_x, prev_y, prev_time = previous_positions[object_id]

            dx = center_x - prev_x
            dy = center_y - prev_y

            dt = current_time - prev_time

            if dt > 0:

                # Convert pixel movement to meters
                dx_m = dx * PIXEL_TO_METER
                dy_m = dy * PIXEL_TO_METER

                # Horizontal speed
                horizontal_speed = abs(dx_m / dt)

                # Vertical speed
                vertical_speed = abs(dy_m / dt)

                # Total speed
                total_speed = np.sqrt(horizontal_speed**2 +
                                      vertical_speed**2)

        # Save current position
        previous_positions[object_id] = (center_x,
                                         center_y,
                                         current_time)

        # Draw object box
        cv2.rectangle(frame,
                      (x1, y1),
                      (x2, y2),
                      (0, 0, 255),
                      2)

        # Draw height line
        cv2.line(frame,
                 (center_x, center_y),
                 (center_x, GROUND_Y),
                 (255, 0, 0),
                 2)

        # Display information
        info1 = f"{name}"
        info2 = f"Height: {height_m:.2f} m"
        info3 = f"wind Speed: {total_speed:.2f} m/s"
        info4 = f"H-Speed: {horizontal_speed:.2f} m/s"
        info5 = f"V-Speed: {vertical_speed:.2f} m/s"

        cv2.putText(frame,
                    info1,
                    (x1, y1 - 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 255),
                    2)

        cv2.putText(frame,
                    info2,
                    (x1, y1 - 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2)

        cv2.putText(frame,
                    info3,
                    (x1, y1 - 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 0),
                    2)

        cv2.putText(frame,
                    info4,
                    (x1, y1 - 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 0, 255),
                    2)

        cv2.putText(frame,
                    info5,
                    (x1, y1),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 165, 255),
                    2)

    # Draw ground objects
    for (x1, y1, x2, y2), name in ground_objects:

        cv2.rectangle(frame,
                      (x1, y1),
                      (x2, y2),
                      (0, 255, 200),
                      2)

        cv2.putText(frame,
                    name,
                    (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 200),
                    2)

    # Display frame
    cv2.imshow("eVTOL Flight Monitoring System", frame)

    # ESC key to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()