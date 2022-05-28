import cv2 as cv
import numpy
import sys
import math
import os

def Rectify( img, K, dist ):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(K, dist, img.shape[::-1], 1, img.shape[::-1])

    mapx, mapy = cv.initUndistortRectifyMap(K, dist, None, newcameramtx, img.shape[::-1], 5)
    newimg = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)

    return newimg
