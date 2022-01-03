from datetime import date
import time
import cv2
import os

class CameraManager():
    def __init__(self, cam_port):
        self.webcam_port = cam_port

    def getCamShot(self):
        cam = cv2.VideoCapture(self.webcam_port, cv2.CAP_DSHOW)
        ret, frame = cam.read()
        time.sleep(0.5)
        img_name = "webcam_shot_{}.png".format(date.today())
        cv2.imwrite(img_name, frame)
        cam.release()
        cv2.destroyAllWindows()