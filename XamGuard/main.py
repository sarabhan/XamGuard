import cv2
import numpy as np

# Function to perform optical flow using Farneback method
def optical_flow(prev_frame, next_frame):
    # Convert frames to grayscale
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    next_gray = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)

    # Calculate optical flow using Farneback method
    flow = cv2.calcOpticalFlowFarneback(prev_gray, next_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    return flow

# Load the pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
ret, prev_frame = cap.read()

# Detect faces in the first frame
faces = face_cascade.detectMultiScale(prev_frame, scaleFactor=1.3, minNeighbors=5)
# Extract the coordinates of the first detected face
if len(faces) == 1:
    x, y, w, h = faces[0]
    prev_face_center = (x + w // 2, y + h // 2)
else:
    print("No face detected in the first frame.")
    exit()

total_distance_left = 0.0
total_distance_right = 0.0

#assign value to movement threshold
MOVEMENT_THRESHOLD = 1000

while True:
    ret, next_frame = cap.read()
    if not ret:
        break
    elif len(faces)==0:
        cv2.putText(next_frame, "look into the camera!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    # Detect faces in the current frame
    faces = face_cascade.detectMultiScale(next_frame, scaleFactor=1.3, minNeighbors=5)
    # Extract the coordinates of the first detected face
    if len(faces) == 1:
        x, y, w, h = faces[0]
        next_face_center = (x + w // 2, y + h // 2)

        # Calculate optical flow & extract horizontal component
        flow = optical_flow(prev_frame, next_frame)
        horizontal_flow = flow[next_face_center[1], next_face_center[0]][0]

        # Update the distance traveled in left and right directions
        if horizontal_flow < 0:
            total_distance_left += abs(horizontal_flow)
        else:
            total_distance_right += abs(horizontal_flow)

        prev_face_center = next_face_center # Update the previous face center for the next iteration
    elif len(faces) > 1:
       cv2.putText(next_frame, f"{len(faces)} people detected!!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
       print("multiple people detected, candidate is cheating")
       break
    for face in faces:
        x, y, w, h = face
        cv2.rectangle(next_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Proctored System using Optical Flow', next_frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
        print(f"Total distance moved to the left: {total_distance_left} pixels")
        print(f"Total distance moved to the right: {total_distance_right} pixels")
        if (total_distance_left + total_distance_right) > MOVEMENT_THRESHOLD: #select distance threshold accordingly
            print("candidate moved around too much. may be cheating")

cap.release()

cv2.destroyAllWindows()
