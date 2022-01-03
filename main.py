from cursor import MouseManager
from camera import CameraManager
import keyboard

cur = MouseManager(1119, 558)
cam = CameraManager(0)

while True:
    print("aboba")
    if keyboard.press_and_release('shift'):
        print("DA!!")
        break
