import cv2
import mediapipe as mp

from app.config.settings import (
    CAMERA_INDEX,
    WINDOW_NAME
)

from app.detection.eye_detection import is_eye_closed
from app.detection.pose_detection import detect_unsafe_pose
from app.services.alert_service import trigger_alert
from app.detection.face_mesh import face_mesh

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

mp_drawing = mp.solutions.drawing_utils

running = False

def start_camera():
    global running

    running = True

    cap = cv2.VideoCapture(CAMERA_INDEX)

    while running and cap.isOpened():

        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        pose_result = pose.process(rgb_frame)

        face_result = face_mesh.process(rgb_frame)

        if pose_result.pose_landmarks:

            mp_drawing.draw_landmarks(
                frame,
                pose_result.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

            if detect_unsafe_pose(
                pose_result.pose_landmarks.landmark
            ):

                cv2.putText(
                    frame,
                    "Unsafe Driving Detected",
                    (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

                trigger_alert()

        if face_result.multi_face_landmarks:

            for face_landmarks in face_result.multi_face_landmarks:

                if is_eye_closed(face_landmarks.landmark):

                    cv2.putText(
                        frame,
                        "Eyes Closed",
                        (10, 90),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        2
                    )

                    trigger_alert()

        cv2.imshow(WINDOW_NAME, frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def stop_camera():
    global running
    running = False