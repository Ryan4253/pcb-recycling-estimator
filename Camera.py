import cv2
import time
import Constants

cap = cv2.VideoCapture(Constants.CAMERA_ID)

def initialize():
    cap.set(3, Constants.CAMERA_PIXEL_WIDTH) # WIDTH
    cap.set(4, Constants.CAMERA_PIXEL_HEIGHT) # HEIGHT
    time.sleep(Constants.CAMERA_INITIALIZE_TIME)

def takePicture():
    _, frame = cap.read()
    return frame

