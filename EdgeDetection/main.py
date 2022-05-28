import cv2
import SIFT
import Matching
import FindHomography
import WarpImage
import DrawMatches
import numpy as np

img1 = cv2.imread('box.pgm')
keypoints1, descriptors1 = SIFT.sift('box.pgm')
img2 = cv2.imread('scene.pgm')
keypoints2, descriptors2 = SIFT.sift('scene.pgm')
matches = Matching.matching(descriptors1, descriptors2, 12)
DrawMatches.drawmatches(img1, img2, keypoints1, keypoints2, matches)
H = FindHomography.findhomography(keypoints1, keypoints2, matches)
im_out = WarpImage.warpimage(img1, H)

cv2.imshow('image', im_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
