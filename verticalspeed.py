import cv2
import numpy as np
from ultralytics import YOLO
import time

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # You can use your own trained model

# Open video file
video_path = "video2.mp4"
cap = cv2.VideoCapture(video_path)

# Variables to track vertical movement
prev_y = None
prev_time = None 
vertical_speed_kmph = 0  # in km/h

# Calibration: 1 pixel = X meters
# Example: If 50 pixels ≈ 1 meter in real-world -> meters_per_pixel = 1 / 50
meters_per_pixel = 1 / 50.0  # Set this based on your video (manual calibration)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run object detection
    results = model(frame, verbose=False)[0]
    detections = results.boxes.xyxy.cpu().numpy()

    # Process first detected object0
    if len(detections) > 0:
        x1, y1, x2, y2 = detections[0][:4]
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)
  

        if prev_y is not None and prev_time is not None:
            dy = cy - prev_y
            dt = current_time - prev_time
            if dt > 0:
                vertical_speed_px_per_sec = abs(dy / dt)  # Always positive
                vertical_speed_mps = vertical_speed_px_per_sec * meters_per_pixel
                vertical_speed_kmph = vertical_speed_mps * 3.6  # Convert to km/h

        prev_y = cy
        prev_time = current_time

        # Draw bounding box and speed
      #  cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, f"Vertical Speed: {vertical_speed_kmph:.2f} km/h", 
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Show video frame
    cv2.imshow("Flying Object Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
