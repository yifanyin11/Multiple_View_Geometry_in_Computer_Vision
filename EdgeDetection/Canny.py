import cv2
import numpy as np

def canny():
    img = cv2.imread('bt.000.png')
    edges = cv2.Canny(img, 70, 200) # 50 150
    return edges

# edges=canny()
# cv2.imshow('image', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()