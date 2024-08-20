import cv2
import datetime

# Load the Haarcascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Start video capture from the webcam
cap = cv2.VideoCapture(0)

# Variables to help control the smile detection and capture
smile_detected = False
smile_frame_count = 0
capture_delay = 10  # Delay between captures in frames
frames_since_last_capture = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Region of Interest (ROI) for smile detection within the face rectangle
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect smiles within the ROI
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 25)

        # Check if a smile is detected
        if len(smiles) > 0:
            smile_frame_count += 1
            if smile_frame_count > 5 and frames_since_last_capture > capture_delay:
                # Capture the image after confirming the smile persists for a few frames
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = f"selfie_{timestamp}.jpg"
                cv2.imwrite(filename, frame)
                print(f"Selfie captured: {filename}")
                frames_since_last_capture = 0  # Reset capture delay
                smile_detected = True
        else:
            smile_frame_count = 0
            smile_detected = False

    frames_since_last_capture += 1

    # Display the frame
    cv2.imshow('Smile to Capture Selfie', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the windows
cap.release()
cv2.destroyAllWindows()
