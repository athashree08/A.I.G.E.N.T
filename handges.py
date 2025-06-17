import cv2
import mediapipe as mp

# Initialize Mediapipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Function to detect hand gestures
def detect_hand_gestures(image):
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    gesture = "None"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Calculate hand landmarks
            landmarks = []
            for landmark in hand_landmarks.landmark:
                landmarks.append((int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])))

            # Detect gestures based on hand landmarks
            gesture = detect_gesture(landmarks)

            # Draw hand landmarks on the image
            for landmark in landmarks:
                cv2.circle(image, landmark, 5, (255, 0, 0), -1)

    return image, gesture

# Function to detect hand gestures
def detect_gesture(landmarks):
    # This is a simplified example. You can implement more complex logic here.
    if len(landmarks) == 21:  # Assuming 21 landmarks for a single hand
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]
        ring_tip = landmarks[16]
        pinky_tip = landmarks[20]

        # Detect gestures
        if thumb_tip[1] < index_tip[1] and thumb_tip[1] < middle_tip[1] and thumb_tip[1] < ring_tip[1] and thumb_tip[1] < pinky_tip[1]:
            if thumb_tip[0] < index_tip[0] and thumb_tip[0] < middle_tip[0] and thumb_tip[0] < ring_tip[0] and thumb_tip[0] < pinky_tip[0]:
                return "Thumbs Up"
        elif thumb_tip[1] > index_tip[1] and thumb_tip[1] > middle_tip[1] and thumb_tip[1] > ring_tip[1] and thumb_tip[1] > pinky_tip[1]:
            return "Hiii"
        elif index_tip[1] < middle_tip[1] and middle_tip[1] < ring_tip[1] and ring_tip[1] < pinky_tip[1]:
            return "Pointing Up"
        elif index_tip[1] > middle_tip[1] and thumb_tip[1] < index_tip[1] and middle_tip[1] < ring_tip[1] and index_tip[1] < pinky_tip[1]:
            return "V Sign"
        elif thumb_tip[1] < index_tip[1] and thumb_tip[1] > middle_tip[1] and thumb_tip[1] > ring_tip[1] and thumb_tip[1] > pinky_tip[1]:
            return "Thumbs Down"
        else:
            return "Don't Know"
    else:
        return "None"

# Main function for real-time hand gesture recognition
def detect():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame, gesture = detect_hand_gestures(frame)

        # Display the recognized gesture
        cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('Hand Gesture Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

detect()