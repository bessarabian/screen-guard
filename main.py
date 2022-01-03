import keyboard, pyautogui, cv2
from datetime import date
import time

m_position = (986, 464)
shots = 3
start_keys = "ctrl+8"
pause_keys = "ctrl+9"

def on_guard():
    pyautogui.moveTo(500, 500)
    while 1:
        time.sleep(0.1)
        if keyboard.is_pressed(start_keys):
            print("script started")
            main()
        

def main():
    pyautogui.moveTo(m_position)
    while 1:
        time.sleep(0.1)
        if keyboard.is_pressed(pause_keys):
            print("script on pause")
            on_guard()
        if pyautogui.position() != m_position:
            print("Doing a webcam shot!")
            webShot()
            break

def webShot():
    index = 1
    try:
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    except:
        cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    for i in range(shots):
        ret, frame = cam.read()
        cv2.imwrite(f"web_shot_{index}.png", frame)
        index += 1
    cam.release()
    time.sleep(0.5)

if __name__ == "__main__":
    on_guard()