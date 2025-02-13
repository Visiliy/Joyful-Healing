import eel # подключаем библиотеку eel
import cv2
import mediapipe
import numpy as np
from pygame import mixer # из библиотеки pygame подкльчаем модуль mixer

count = 0 # инициализируем счётчик для подсчёта количества нажатий.

def close_callback(route, websockets): # функция для остановки приложения
    if not websockets: # если нажат крестик
        exit() # остановка программы


@eel.expose # декаратор для того, чтобы функцию можно было вызывать из javascript
def hello(res): # res - название процедуры
    global count # подключаем счётчик
    print("Hello, Sonya and Lera!")
    print(res)
    mixer.init() # активируем модуль для проигрывания музыки
    mixer.music.load("music/Uspokaivayushhaya_muzyka_-_lejjta_56569736.mp3") # загружаем трек
    if count % 2 == 0:
        mixer.music.play() # включаем трек
    else:
        mixer.music.stop() # останавливаем трек
    count += 1

def main():
    eel.init("frontend") # подключаем папку с кодом приложения
    eel.start( # активируем окно приложения
        "index.html", close_callback=close_callback, cmdline_args=["--start-maximized"]
    )
    # index.html - файл с кодом приложения
    # close_callback - подключение функции для звкрытия окна
    # cmdline_args=["--start-maximized"] - открытие окна на весь экран


if __name__ == "__main__": # если запуск программы из файла main.py
    main() # то вызываем функцию main и запускаем приложение