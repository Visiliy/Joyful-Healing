import cv2
import numpy as np
import mediapipe


mp_solutions = mediapipe.solutions.face_mesh
face = mp_solutions.FaceMesh(min_detection_confidence=0.5)
pocket = []      
image_path = "photo/photo1.jpg"
image = cv2.imread(image_path)
(h, w) = image.shape[:2]
new_widh = 800
aspect_ratio = h / w
new_height = int(new_widh * aspect_ratio)
image = cv2.resize(image, (new_widh, new_height))
image = cv2.flip(image, 1)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_green = np.array([40, 100, 100])
upper_green = np.array([80, 255, 255])
mask = cv2.inRange(hsv_image, lower_green, upper_green)
coordinates = np.column_stack(np.where(mask > 0))
print(coordinates)
frame = image
results = face.process(frame)
if results.multi_face_landmarks:
    for face_land in results.multi_face_landmarks:
        idx = 0
        for elem in face_land.landmark:
            x = int(elem.x * frame.shape[1])
            y = int(elem.y * frame.shape[0])
            face_mark = [x, y]
            if mask[y, x] > 0:
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
                pocket.append(idx)
            cv2.circle(frame, (x, y), 3, (225, 0, 0), -1)
            cv2.putText(frame, str(idx), (x, y), cv2.FORMATTER_FMT_NUMPY, 0.3, (255, 255, 255), 1)
            idx = idx + 1
cv2.putText(frame, "", (120, 100), cv2.FORMATTER_FMT_NUMPY, 2, (255, 255, 255), 2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Ошибка видео")
try:
    while True:
        ret, frame = cap.read()
        results = face.process(frame)
        if results.multi_face_landmarks:
            for face_land in results.multi_face_landmarks:
                idx = 0
                for elem in face_land.landmark:
                    if idx in pocket:
                        x = int(elem.x * frame.shape[1])
                        y = int(elem.y * frame.shape[0])
                        face_mark = [x, y]
                        # if face_mark in coordinates:
                        #     pocket.append(idx)
                        cv2.circle(frame, (x, y), 3, (0, 225, 0), -1)
                        idx = idx + 1
        cv2.putText(frame, "", (120, 100), cv2.FORMATTER_FMT_NUMPY, 2, (0, 0, 0), 2)
        frame = cv2.flip(frame, 1)
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.namedWindow("main", cv2.WINDOW_AUTOSIZE)
    cv2.destroyAllWindows()