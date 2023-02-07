import Color
import cv2

# Pyserial Constants
ARDUINO_PORT = 'COM3'
ARDUINO_BAUD_RATE = 115200

# Camera Setup
CAMERA_ID = 0
CAMERA_PIXEL_WIDTH = 1920
CAMERA_PIXEL_HEIGHT = 1080
CAMERA_INITIALIZE_TIME = 5

# Object Detection Files
CLASSES_FILE = 'board' + '.names'
CONFIG_FILE = 'yolov4-board' + '.cfg'
WEIGHTS_FILE = 'yolov4-board_best_mAP54' + '.weights'

# Object Detection Class Constants
CLASSES = [line.strip() for line in open(CLASSES_FILE)]

# Image Blob Detection Constants
IMAGE_SCALE = 1 / 255.0
IMAGE_DATA_SIZE = (416, 416)
MEAN_SUBTRACTION = (0, 0, 0)

# Detection Result Constants
CONFIDENCE_THRESHOLD = 0.3
NMS_THRESHOLD = 0.4

# Visualization Constants
CLASS_COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.BROWN, Color.CYAN, Color.MAGENTA, Color.ORANGE, Color.YELLOW, Color.PURPLE]
FONT = cv2.FONT_HERSHEY_PLAIN

# Price Calculation Constants
ALUMINUM_CONTENT = {
    "Capacitor"   : 0.35,
    "IC"          : 0,
    "MLCC"        : 0,
    "Heatsink_Al" : 0.9,
    "Heatsink_Cu" : 0,
    "RJ45"        : 2.2,
    "USB"         : 0,
    "DB9"         : 0.2,
    "HDMI"        : 1.6
}

COPPER_CONTENT = {
    "Capacitor"   : 0,
    "IC"          : 0.000016,
    "MLCC"        : 0.38,
    "Heatsink_Al" : 0,
    "Heatsink_Cu" : 5.5,
    "RJ45"        : 0,
    "USB"         : 0.6,
    "DB9"         : 0.5,
    "HDMI"        : 0
}

GOLD_CONTENT = {
    "Capacitor"   : 0,
    "IC"          : 0.000017,
    "MLCC"        : 0,
    "Heatsink_Al" : 0,
    "Heatsink_Cu" : 0,
    "RJ45"        : 0,
    "USB"         : 0,
    "DB9"         : 0,
    "HDMI"        : 0
}

IRON_CONTENT = {
    "Capacitor"   : 0,
    "IC"          : 0,
    "MLCC"        : 0,
    "Heatsink_Al" : 0,
    "Heatsink_Cu" : 0,
    "RJ45"        : 0,
    "USB"         : 1.5,
    "DB9"         : 4.3,
    "HDMI"        : 0
}

METAL_PRICE = {
    "Aluminum" : 0.021,
    "Copper"   : 0.090,
    "Gold"     : 1939.417,
    "Iron"     : 0.294
}