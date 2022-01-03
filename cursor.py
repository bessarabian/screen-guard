import pyautogui
from pynput import keyboard
from camera import CameraManager

class MouseManager():
    def __init__(self, posx, posy):
        self._cursorPosition = (posx, posy)

    def getCursorPosition(self):
        return self._cursorPosition

    def setCursor(self):
        pyautogui.moveTo(self.getCursorPosition())

    def listenCursor(self):
        while True:
            if self.getCursorPosition() == pyautogui.position():
                return True
            elif self.getCursorPosition() != pyautogui.position():
                return False