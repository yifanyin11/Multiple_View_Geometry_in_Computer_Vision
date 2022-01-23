import numpy as np
import cv2 as cv
import os
import CalibrateCamera
import RectifyImage
import FundamentalMatrix
import EpipolarLines
import DisplayKeypointsandLines

def ExtractKeypoints(img1, img2, N):
    sift1 = cv.SIFT_create()
    sift2 = cv.SIFT_create()

    keypoints1, descriptors1 = sift1.detectAndCompute(img1, None)
    keypoints2, descriptors2 = sift2.detectAndCompute(img2, None)
    matches = cv.BFMatcher().match(descriptors1, descriptors2)
    # define a sort_key function for sorting based on distance
    def sort_key(match):
        return match.distance
    strong = sorted(matches, key=sort_key)
    matches = strong[:N]
    X_query = np.zeros((N, 2))
    X_train = np.zeros((N, 2))
    for i in range(N):
        X_query[i, :] = keypoints1[matches[i].queryIdx].pt
        X_train[i, :] = keypoints2[matches[i].trainIdx].pt
    X_query = X_query.astype(int)
    X_train = X_train.astype(int)
    return X_query, X_train
# # # for testing
# img1 = cv.imread('test_images/image1.png')
# img2 = cv.imread('test_images/image2.png')
#
# path = 'calibration_images'
# rms, K, dist = CalibrateCamera.CalibrateCamera(path, 12, 9, 0.01)
# img1 = RectifyImage.Rectify(img1, K, dist)
# img2 = RectifyImage.Rectify(img2, K, dist)
# X1, X2 = ExtractKeypoints(img1, img2, 10)
# # print(X1)
# # print(X2)
#
# F = FundamentalMatrix.FundamentalMatrix(X1, X2)
#
# lines1, lines2 = EpipolarLines.EpipolarLines(X1, X2, F)
#
# DisplayKeypointsandLines.DisplayKeypointsandLines(img1, img2, X1, X2, lines1, lines2)
#
