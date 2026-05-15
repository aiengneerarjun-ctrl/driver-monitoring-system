from app.utils.helpers import euclidean_distance
from app.config.settings import EAR_THRESHOLD

LEFT_EYE_INDEXES = [33, 160, 158, 133, 153, 144]
RIGHT_EYE_INDEXES = [362, 385, 387, 263, 373, 380]

def calculate_ear(landmarks, eye_indices):
    left = landmarks[eye_indices[0]]
    right = landmarks[eye_indices[3]]

    top1 = landmarks[eye_indices[1]]
    top2 = landmarks[eye_indices[2]]

    bottom1 = landmarks[eye_indices[5]]
    bottom2 = landmarks[eye_indices[4]]

    vertical = (
        euclidean_distance(top1, bottom1) +
        euclidean_distance(top2, bottom2)
    ) / 2.0

    horizontal = euclidean_distance(left, right)

    return vertical / horizontal

def is_eye_closed(landmarks):
    left_ear = calculate_ear(landmarks, LEFT_EYE_INDEXES)
    right_ear = calculate_ear(landmarks, RIGHT_EYE_INDEXES)

    avg_ear = (left_ear + right_ear) / 2

    return avg_ear < EAR_THRESHOLD