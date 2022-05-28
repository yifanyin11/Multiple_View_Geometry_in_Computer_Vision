import numpy as np
import cv2

def findhomography(keypoints1, keypoints2, matches):
    N = np.size(matches)
    X_query = np.zeros((N, 2))
    X_train = np.zeros((N, 2))
    for i in range(N):
        X_query[i, :] = keypoints1[matches[i].queryIdx].pt
        X_train[i, :] = keypoints2[matches[i].trainIdx].pt
    Homography, mask = cv2.findHomography(X_query, X_train, cv2.RANSAC, 5.0)
    return Homography


