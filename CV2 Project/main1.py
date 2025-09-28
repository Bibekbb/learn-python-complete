import cv2
import pyautogui
import mediapipe as mp

# Set up FaceMesh
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Set up the camera
cam = cv2.VideoCapture(0)

# Get screen dimensions
screen_w, screen_h = pyautogui.size()

while True:
    # Read a frame from the camera
    _, frame = cam.read()

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with FaceMesh
    output = face_mesh.process(rgb_frame)

    # Get the landmarks
    landmark_points = output.multi_face_landmarks

    # Check if landmarks are detected
    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Draw circles for specific landmarks
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame.shape[1])
            y = int(landmark.y * frame.shape[0])
            cv2.circle(frame, (x, y), 3, (0, 255, 0))

            # Move the cursor to the specified landmark
            if id == 1:
                screen_x = int(screen_w * landmark.x)
                screen_y = int(screen_h * landmark.y)
                pyautogui.moveTo(screen_x, screen_y)

        # Extract left eye landmarks
        left_eye_landmarks = [landmarks[145], landmarks[159]]

        
        for landmark in left_eye_landmarks:
            x = int(landmark.x * frame.shape[1])
            y = int(landmark.y * frame.shape[0])
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        
        if (left_eye_landmarks[0].y - left_eye_landmarks[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)

    
    cv2.imshow('Eye Controlled Mouse', frame)

    
    if cv2.waitKey(1) == 27:
        break


cam.release()
cv2.destroyAllWindows()
