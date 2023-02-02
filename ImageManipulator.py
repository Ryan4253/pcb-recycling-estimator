import cv2

def splitImage(image, row, col):
    height, width, _ = image.shape

    ret = []
    pieceHeight = round(height / row)
    pieceWidth = round(width / col)

    for i in range(row):
        for j in range(col):
            piece = image[pieceHeight * i : pieceHeight * (i+1), pieceWidth * j : pieceWidth * (j+1), :]
            ret.append(piece)
            cv2.imwrite(f"img{i}_{j}.png", piece)

    return ret

def getBoundingBox(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    th, binary = cv2.threshold(blurred , 0, 255, cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 0, 0), 3)
    
    bounding_boxes = [cv2.boundingRect(cnt) for cnt in contours]
    
    return bounding_boxes