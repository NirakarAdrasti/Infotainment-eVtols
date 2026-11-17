import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # Use your model file here

# Open video file
video_path = "video.mp4"  # Replace with your video path
cap = cv2.VideoCapture(video_path)

# Ground line (initialized dynamically)
GROUND_Y = None

# Class names
CLASSES = model.names

# Flying and ground classes
flying_classes = ['bird', 'airplane', 'kite', 'drone']
ground_classes = ['person', 'car', 'truck', 'bus', 'bicycle', 'motorcycle']

# Conversion factor (calibrate this for real-world scaling)
PIXEL_TO_METER = 0.175  # 1 pixel = 1.75 cm

while True:
    
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 inference
    results = model(frame)[0]
    detections = results.boxes.data.cpu().numpy()

    flying_objects = []
    ground_objects = []

    # Detect GROUND_Y from ground object bottom edges
    if GROUND_Y is None:
        GROUND_Y = 0

    for det in detections:
        x1, y1, x2, y2, conf, cls_id = det
        cls_id = int(cls_id)
        class_name = CLASSES[cls_id]
        x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))

        if class_name in ground_classes:
            ground_objects.append(((x1, y1, x2, y2), class_name))
            GROUND_Y = max(GROUND_Y, y2)
        elif class_name in flying_classes:
            flying_objects.append(((x1, y1, x2, y2), class_name))

    # Draw ground line
    if GROUND_Y:
        cv2.line(frame, (0, GROUND_Y), (frame.shape[1], GROUND_Y), (0, 255, 0), 2)
        cv2.putText(frame, f"Ground Level: Y={GROUND_Y}", (10, GROUND_Y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Draw flying objects and estimate height in meters
    for (x1, y1, x2, y2), name in flying_objects:
        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)
        height_px = GROUND_Y - center_y
        height_m = height_px * PIXEL_TO_METER
        height_m = round(height_m, 2)

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Label with height in meters
        cv2.putText(frame, f"{name} Height: {height_m} m", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        # Line from object to ground
        cv2.line(frame, (center_x, center_y), (center_x, GROUND_Y), (255, 0, 0), 1)

    # Draw ground objects
    for (x1, y1, x2, y2), name in ground_objects:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)
        cv2.putText(frame, name, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    # Show frame
    cv2.imshow("Object Detection & Height Estimation", frame)
    if cv2.waitKey(1) == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
