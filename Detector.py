import cv2
import numpy as np
import matplotlib.pyplot as plt
import Constants

def processDetection(detection, width, height):
    # Results Processing
    centerXPct, centerYPct, wPct, hPct = detection[0:4]
    confidence = float(detection[4])
    classId = np.argmax(detection[5:])

    # Boudning Box Calculation
    centerX = int(centerXPct * width)
    centerY = int(centerYPct * height)
    w = int(wPct * width)
    h = int(hPct * height)
    x = int(centerX - w / 2)
    y = int(centerY - h / 2)

    return [[x, y, w, h], confidence, classId]

def getComponentCounts(detections):
    components = {
        "Capacitor"   : 0,
        "IC"          : 0,
        "MLCC"        : 0,
        "Heatsink_Al" : 0,
        "Heatsink_Cu" : 0,
        "RJ45"        : 0,
        "USB"         : 0,
        "DB9"         : 0,
        "HDMI"        : 0
    }

    for detection in detections:
        components[Constants.CLASSES[detection[2]]] += 1

    return components

def detectComponents(image, visualize = False):
    # Run Object Detection
    net = cv2.dnn.readNetFromDarknet(Constants.CONFIG_FILE,Constants.WEIGHTS_FILE)
    layerNames = net.getLayerNames()
    outputLayers = [layerNames[i-1] for i in net.getUnconnectedOutLayers()]
    blob = cv2.dnn.blobFromImage(image, Constants.IMAGE_SCALE, Constants.IMAGE_DATA_SIZE, Constants.MEAN_SUBTRACTION, True, crop=False)
    net.setInput(blob)
    outputs = net.forward(outputLayers)

    # Find all confident detections
    height, width, _ = image.shape 
    detections = []
    for output in outputs:
        for candidate in output:
            if candidate[4] < Constants.CONFIDENCE_THRESHOLD:  
                continue 
            detections.append(processDetection(candidate, width, height))

    # Performs Non-Maximum Supression on detected components
    boxes = [detection[0] for detection in detections]
    confidences = [detection[1] for detection in detections]
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, Constants.CONFIDENCE_THRESHOLD, Constants.NMS_THRESHOLD)
    detections = [detections[i] for i in indexes]

    if not visualize:
        return getComponentCounts(detections)

    # Result Visualization
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    for detection in detections:
        x, y, w, h = detection[0]
        label = Constants.CLASSES[detection[2]]
        color = Constants.CLASS_COLORS[detection[2]]
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 1)
        cv2.putText(image, label, (x, y - 5), Constants.FONT, 1, color, 1)
        plt.rcParams['figure.figsize'] = [15, 10]
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(img_rgb)
    plt.show()

    return getComponentCounts(detections)
