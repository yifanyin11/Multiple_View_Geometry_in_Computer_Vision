import SIFT
import cv2

def matching(descriptor1, descriptor2, N):
    matches = cv2.BFMatcher().match(descriptor1, descriptor2)
    # define a sort_key function for sorting based on distance
    def sort_key(match):
        return match.distance
    strong = sorted(matches, key=sort_key)
    matches = strong[:N]
    return matches

# img1 = cv2.imread('box.pgm')
# keypoints1, descriptors1 = SIFT.sift('box.pgm')
# img2 = cv2.imread('scene.pgm')
# keypoints2, descriptors2 = SIFT.sift('scene.pgm')
# matches = matching(descriptors1, descriptors2, 12)

