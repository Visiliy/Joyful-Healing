import cv2
import numpy as np
import mediapipe
import json

mp_solutions = mediapipe.solutions.face_mesh
face = mp_solutions.FaceMesh(min_detection_confidence=0.5)
pocket = []
#
# 1. Загружаем изображение
image_path = 'photo/photo1.jpg'  # Укажи путь к своей картинке
image = cv2.imread(image_path)
(h, w) = image.shape[:2]
new_widh = 800
aspect_ratio = h / w
new_height = int(new_widh * aspect_ratio)
image = cv2.resize(image, (new_widh, new_height))
image = cv2.flip(image, 1)
# 2. Преобразуем цвет в HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 3. Определяем диапазон для ярко-зелёного цвета
lower_green = np.array([40, 100, 100])  # Нижний предел для зелёного
upper_green = np.array([80, 255, 255])  # Верхний предел для зелёного
# 4. Создаём маску для зелёного цвета
mask = cv2.inRange(hsv_image, lower_green, upper_green)
# 5. Находим координаты зелёных точек
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
            if mask[y,x]>0:
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
                pocket.append(idx)
            cv2.circle(frame, (x, y), 3, (225, 0, 0), -1)
            cv2.putText(frame, str(idx), (x, y), cv2.FORMATTER_FMT_NUMPY, 0.3, (255, 255, 255), 1)
            idx = idx + 1
cv2.putText(frame, "", (120, 100), cv2.FORMATTER_FMT_NUMPY, 2, (255, 255, 255), 2)
cv2.imshow("Video", frame)
cv2.imwrite(image_path[:-5]+"new.jpg", frame )
cv2.waitKey(0)
cv2.destroyAllWindows()
with open("2.txt", "w", encoding="utf-8") as file:
    file.write(json.dumps(pocket))
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Ошибка видео")

# with open("0.txt", "r", encoding="utf-8") as f:
#     pocket = json.loads(f.read())

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
                        face_mark = [ x, y]
                        # if face_mark in coordinates:
                        #     pocket.append(idx)
                        cv2.circle(frame, (x,y), 3, (0, 225, 0), -1 )
                    idx = idx + 1

        cv2.putText(frame, "", (120, 100), cv2.FORMATTER_FMT_NUMPY, 2, (0, 0, 0), 2)
        frame = cv2.flip(frame, 1)
        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()

