import eel
import cv2
import json
import mediapipe
from pygame import mixer


def close_callback(route, websockets): # функция для остановки приложения
    if not websockets: # если нажат крестик
        exit() # остановка программы


@eel.expose # декоратор для того, чтобы функцию можно было вызывать из javascript
def hello(res): # res - название процедуры
    mixer.init() # активируем модуль для проигрывания музыки
    mixer.music.load("music/Uspokaivayushhaya_muzyka_-_lejjta_56569736.mp3") # загружаем трек
    mixer.music.play() # включаем трек

    mp_solutions = mediapipe.solutions.face_mesh
    face = mp_solutions.FaceMesh(min_detection_confidence=0.5)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Ошибка видео")

    with open(f"library/{res}.txt", "r", encoding="utf-8") as f:
        pocket = json.loads(f.read())

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
                mixer.music.stop()
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


def main():
    eel.init("frontend") # подключаем папку с кодом приложения
    eel.start( # активируем окно приложения
        "index.html", close_callback=close_callback, cmdline_args=["--start-maximized"]
    )
    # index.html - файл с кодом приложения
    # close_callback - подключение функции для закрытия окна
    # cmdline_args=["--start-maximized"] - открытие окна на весь экран


if __name__ == "__main__": # если запуск программы из файла main.py
    main() # то вызываем функцию main и запускаем приложение