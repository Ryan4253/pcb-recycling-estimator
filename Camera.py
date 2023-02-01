import cv2
import time

cap = cv2.VideoCapture(0)

def initialize():
    cap.set(3,1920) # WIDTH
    cap.set(4,1080) # HEIGHT
    time.sleep(10)

def takePicture():
    ret, frame = cap.read()
    return frame

