import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # Small and fast model

# Open video file
video_path = "video2.mp4"  # Replace with your video path
cap = cv2.VideoCapture(video_path)

# Define ground line manually (or use advanced terrain detection)
GROUND_Y = None  # To set dynamically

# Class names from COCO
CLASSES = model.names

# Define flying object classes (you can customize this list)
flying_classes = ['bird', 'airplane', 'kite', 'drone']

# Define ground objects
ground_classes = ['person', 'car', 'truck', 'bus', 'bicycle', 'motorcycle']

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)[0]
    detections = results.boxes.data.cpu().numpy()

    flying_objects = []
    ground_objects = []

    # Detect ground line from lowest object if not set
    if GROUND_Y is None:
        GROUND_Y = 0

    for det in detections:
        x1, y1, x2, y2, conf, cls_id = det
        cls_id = int(cls_id)
        class_name = CLASSES[cls_id]
        box_mid_y = int((y1 + y2) / 2)

        if class_name in ground_classes:
            ground_objects.append(((int(x1), int(y1), int(x2), int(y2)), class_name))
            GROUND_Y = max(GROUND_Y, int(y2))  # Ground line = lowest bottom edge
        elif class_name in flying_classes:   
            flying_objects.append(((int(x1), int(y1), int(x2), int(y2)), class_name))

    # Draw ground line
    if GROUND_Y:
        cv2.line(frame, (0, GROUND_Y), (frame.shape[1], GROUND_Y), (0, 255, 0), 2)
        cv2.putText(frame, f"Ground Level: Y={GROUND_Y}", (10, GROUND_Y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

#height conervt to meter


    # Draw and measure height of flying objects
    PIXEL_TO_METER = 0.0175  # Example scale: 1 pixel = 1.75cm
    for (x1, y1, x2, y2), name in flying_objects:
        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)
        height_px = GROUND_Y - center_y

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(frame, f"{name} Height: {height_px}px", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
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
