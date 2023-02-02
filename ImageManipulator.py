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
