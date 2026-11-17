import cv2
import numpy as np

# Input/output video file
input_video = 'flight_input.mp4'
output_video = 'flight_output_with_altitude.mp4'

# Open the input video
cap = cv2.VideoCapture(input_video)

# Check if video opened successfully
if not cap.isOpened():
    print("Error opening video file.")
    exit()

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define VideoWriter to save output
out = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# Initialize variables
frame_count = 0
base_altitude = 100  # Starting altitude in meters
rate_per_frame = 0.5  # Simulated rate of change

# Process each frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Simulate height and altitude (you can use object detection instead of simulation)
    current_altitude = base_altitude + frame_count * rate_per_frame
    current_height = current_altitude - 10  # e.g., height above some terrain

    # Add overlays on the frame
    text_altitude = f"Altitude: {current_altitude:.2f} m"
    text_height = f"Height: {current_height:.2f} m"

    cv2.putText(frame, text_altitude, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, text_height, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 255), 2)

    # Optional: green radar dot moving in a radius
    radius = 30
    center_x = int(100 + radius * np.cos(frame_count * 0.1))
    center_y = int(200 + radius * np.sin(frame_count * 0.1))
    cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

    # Write the frame to output video
    out.write(frame)
    frame_count += 1

# Release everything
cap.release()
out.release()
print("Flight overlay video created successfully.")


