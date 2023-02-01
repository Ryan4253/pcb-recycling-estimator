import Camera
import Detector
import PriceCalculator

Camera.initialize()
result = Detector.detectComponents(Camera.takePicture(), True)
print(result)
print(PriceCalculator.calculatePrice(result))