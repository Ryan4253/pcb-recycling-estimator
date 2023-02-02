import Camera
import Detector
import PriceCalculator
import cv2
import ImageManipulator

Camera.initialize()
images = ImageManipulator.splitImage(cv2.imread('img.jpg'), 2, 2)
for image in images:
    result = Detector.detectComponents(image, True)
    print(result)
    print(PriceCalculator.calculatePrice(result))
