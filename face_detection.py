import cv2
import face_recognition
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def detect_face():
# Load the known face image and encode it
    known_image = face_recognition.load_image_file("D:/PROGRAMMING/PYTHON/AIGENT/Profile_Pic.jpg")
    known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Initialize video capture
    video_capture = cv2.VideoCapture(0)

# Flag to track if authentication has already occurred
    authenticated_once = False

    while True:
    # Capture frame-by-frame
        ret, frame = video_capture.read()

    # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        authenticated = False

    # Loop through each face found in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the face encoding with the known face encoding
            matches = face_recognition.compare_faces([known_face_encoding], face_encoding)

        # If a match is found
            if matches[0]:
            # Set authenticated to true
                authenticated = True
            # Draw a rectangle around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            # Print authentication message if not printed before
                if not authenticated_once:
                    speak("Name: Prathmesh Boge")
                    speak("Age:17")
                    authenticated_once = True
                break

    # If authenticated, display message on the frame
        if authenticated:
            cv2.putText(frame, "You are authenticated!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, "Name:Prathmesh Boge", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, "Age:17", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "You are not authenticated", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the resulting frame
        cv2.imshow('Video', frame)

    # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    video_capture.release()
    cv2.destroyAllWindows()
detect_face()

