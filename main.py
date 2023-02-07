import Camera
import Detector
import PriceCalculator
import cv2
import ImageManipulator
import MotorController

try:
    while True:
        choice = input('Input: ').lower()

        if choice == 'end':
            MotorController.ser.close()
            break

        MotorController.setPower(int(choice))
            
except KeyboardInterrupt:
    MotorController.ser.close()

Camera.initialize()
images = ImageManipulator.splitImage(cv2.imread('img.jpg'), 2, 2)
for image in images:
    result = Detector.detectComponents(image, True)
    print(result)
    print(PriceCalculator.calculatePrice(result))
