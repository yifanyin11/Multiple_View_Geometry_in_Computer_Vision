import numpy as np
import cv2
import Matching
import SIFT

def drawmatches(img1, img2, keypoints1, keypoints2, matches):
    img_match = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.imshow('image_match', img_match)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# img1 = cv2.imread('box.pgm')
# keypoints1, descriptors1 = SIFT.sift('box.pgm')
# img2 = cv2.imread('scene.pgm')
# keypoints2, descriptors2 = SIFT.sift('scene.pgm')
#
# matches = Matching.matching(descriptors1, descriptors2, 12)
# drawmatches(img1, img2, keypoints1, keypoints2, matches)

