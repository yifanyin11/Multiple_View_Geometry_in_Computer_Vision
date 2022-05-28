import numpy as np
import cv2

def sift(filename):
    img = cv2.imread(filename)
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(img, None)
    return keypoints, descriptors

# img = cv2.imread('box.pgm')
# keypoints, descriptors = sift('box.pgm')
# img = cv2.drawKeypoints(img, keypoints, img)
# cv2.imwrite('sift_keypoints.jpg', img)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
