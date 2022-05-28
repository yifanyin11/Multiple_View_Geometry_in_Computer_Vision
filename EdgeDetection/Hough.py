import numpy as np
import cv2

def hough(img):
    # lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 160, minLineLength=120, maxLineGap=14)
    lines = cv2.HoughLinesP(img, 1, np.pi / 180, 130, minLineLength=350, maxLineGap=100)
    return lines

