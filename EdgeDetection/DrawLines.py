import numpy as np
import cv2
import Canny
import Hough

def drawlines(img, lines):
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imwrite('bt.000_houghlines.png', img)
    cv2.imshow('houghlines', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# img = cv2.imread('bt.000.png')
# edges = Canny.canny()
# lines = Hough.hough(edges)
# drawlines(img, lines)

