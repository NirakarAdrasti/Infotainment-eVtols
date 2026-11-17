import cv2
import math
import time
from ultralytics import YOLO

# Load AI model
model = YOLO("yolov8n.pt")   # lightweight AI model

# Camera start
cap = cv2.VideoCapture(0)

# -------- Flight Parameters ----------
BATTERY_CAPACITY = 3000   # mAh
POWER_CONSUMPTION = 15    # mAh per second (drone motor usage)
DRONE_SPEED = 10          # meters per second
SAFE_DISTANCE = 5         # meters
# -------------------------------------

start_time = time.time()

def estimate_distance(box_width):
    # Approx distance formula (camera focal approx)
    focal_length = 700
    real_width = 0.5  # average human/object width in meters
    distance = (real_width * focal_length) / box_width
    return round(distance,2)

def remaining_flight_time():
    elapsed = time.time() - start_time
    used_battery = elapsed * POWER_CONSUMPTION
    remaining = BATTERY_CAPACITY - used_battery
    if remaining < 0:
        remaining = 0
    return round(remaining / POWER_CONSUMPTION,1)

while True:
    success, img = cap.read()
    if not success:
        break

    results = model(img, stream=True)

    warning = "SAFE"

    for r in results:
        boxes = r.boxes
        for box in boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            w = x2 - x1

            distance = estimate_distance(w)

            if distance < SAFE_DISTANCE:
                warning = "DANGER"

            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(img,f"{distance}m",(x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)

    # Flight time
    time_left = remaining_flight_time()

    cv2.putText(img,f"Flight Time Left: {time_left}s",(10,30),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)

    # Warning
    color = (0,255,0) if warning=="SAFE" else (0,0,255)
    cv2.putText(img,f"Status: {warning}",(10,60),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,color,3)

    cv2.imshow("AI Flight Assist",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
