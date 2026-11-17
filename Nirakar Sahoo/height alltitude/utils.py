import cv2
import math
import time
import numpy as np

def detect_objects(frame):
    # Placeholder dummy detection
    # Replace this with YOLOv8, MobileNetSSD, or similar model
    h, w, _ = frame.shape
    bbox = [int(w*0.4), int(h*0.2), int(w*0.6), int(h*0.4)]  # Simulated flying object
    return [{'label': 'airplane', 'bbox': bbox, 'confidence': 0.95}]

def estimate_speed(curr_pos, prev_pos, frame_rate=30):
    if prev_pos is None:
        return 0.0, 0.0
    dx = curr_pos[0] - prev_pos[0]
    dy = curr_pos[1] - prev_pos[1]
    distance = math.sqrt(dx**2 + dy**2)
    speed = distance * frame_rate
    height = dy
    return speed, height
       
def display_overlay(frame, info):
    x, y = 10, 30
    for key, value in info.items():
        cv2.putText(frame, f"{key}: {value}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        y += 25

def draw_green_light(frame, center, radius):
    angle = (time.time() * 100) % 360
    rad = math.radians(angle)
    cx = int(center[0] + radius * math.cos(rad))
    cy = int(center[1] + radius * math.sin(rad))
    cv2.circle(frame, (cx, cy), 8, (0, 255, 0), -1)
    cv2.circle(frame, center, radius, (0, 255, 0), 1)
