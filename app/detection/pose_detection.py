
import mediapipe as mp

mp_pose = mp.solutions.pose

def detect_unsafe_pose(landmarks):
    nose = landmarks[mp_pose.PoseLandmark.NOSE.value]

    left_shoulder = landmarks[
        mp_pose.PoseLandmark.LEFT_SHOULDER.value
    ]

    right_shoulder = landmarks[
        mp_pose.PoseLandmark.RIGHT_SHOULDER.value
    ]

    shoulder_center_x = (
        left_shoulder.x + right_shoulder.x
    ) / 2

    return abs(nose.x - shoulder_center_x) > 0.1