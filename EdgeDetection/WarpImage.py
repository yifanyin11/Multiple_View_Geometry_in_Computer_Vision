import cv2
import Matching
import FindHomography
import SIFT

def warpimage(img, H):
    size1 = 512
    size2 = 384
    im_out = cv2.warpPerspective(img, H, (size1, size2))
    return im_out

# img1 = cv2.imread('box.pgm')
# keypoints1, descriptors1 = SIFT.sift('box.pgm')
# img2 = cv2.imread('scene.pgm')
# keypoints2, descriptors2 = SIFT.sift('scene.pgm')
# matches = Matching.matching(descriptors1, descriptors2, 12)
# H = FindHomography.findhomography(keypoints1, keypoints2, matches)
# im_out = warpimage(img1, H)
#
# cv2.imshow('image', im_out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
