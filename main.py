import eel
from pygame import mixer

count = 0

def close_callback(route, websockets):
    if not websockets:
        exit()


@eel.expose
def hello(res):
    global count
    print("Hello, Sonya and Lera!")
    print(res)
    mixer.init()
    mixer.music.load("music/Uspokaivayushhaya_muzyka_-_lejjta_56569736.mp3")
    if count % 2 == 0:
        mixer.music.play()
    else:
        mixer.music.stop()
    count += 1

def main():
    eel.init("frontend")
    eel.start(
        "index.html", close_callback=close_callback, cmdline_args=["--start-maximized"]
    )


if __name__ == "__main__":
    main()