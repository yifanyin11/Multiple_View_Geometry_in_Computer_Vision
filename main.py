import numpy as np
import cv2 as cv
import CalibrateCamera
import ExtractKeypoints
import RectifyImage
import FundamentalMatrix
import EpipolarLines
import DisplayKeypointsandLines
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # calibrate camera
    path1 = 'calibration_images'
    path2 = 'test_images'

    rms, K, dist = CalibrateCamera.CalibrateCamera(path1, 12, 9, 0.02)

    img1 = cv.imread(path2 + '/image1.png')
    img2 = cv.imread(path2 + '/image2.png')

    img1 = RectifyImage.Rectify(img1, K, dist)
    img2 = RectifyImage.Rectify(img2, K, dist)

    X1, X2 = ExtractKeypoints.ExtractKeypoints(img1, img2, 10)
    # print(X1)
    # print(X2)

    F = FundamentalMatrix.FundamentalMatrix(X1, X2)

    lines1, lines2 = EpipolarLines.EpipolarLines(X1, X2, F)

    DisplayKeypointsandLines.DisplayKeypointsandLines(img1, img2, X1, X2, lines1, lines2)


