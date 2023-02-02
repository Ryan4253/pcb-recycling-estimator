import Camera
import Detector
import PriceCalculator
import cv2
import ImageManipulator
import time

# Camera.initialize()
# images = ImageManipulator.splitImage(cv2.imread('images.jpg'), 4, 4)
# for image in images:
#     result = Detector.detectComponents(image, True)
#     print(result)
#     print(PriceCalculator.calculatePrice(result))

image = cv2.imread('images.jpg')
bounding_boxes = ImageManipulator.getBoundingBox(image)
for bbox in bounding_boxes:
    [x , y, w, h] = bbox
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print(bbox)

cv2.imshow("OUTPUT", image)
cv2.waitKey(0)