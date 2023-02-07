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
images = ImageManipulator.splitImage(Camera.takePicture(), 1, 2)
#images = ImageManipulator.splitImage(cv2.imread('images.jpg'), 3, 3)

price = 0
for image in images:
    result = Detector.detectComponents(image, True)
    print(result)
    price += PriceCalculator.calculatePrice(result)

print("Price: ", price)
