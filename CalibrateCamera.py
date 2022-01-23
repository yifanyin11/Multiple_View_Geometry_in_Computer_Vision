import numpy as np
import cv2 as cv
import os

def CalibrateCamera(path, width, height, size):
    # termination criteria
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    objp = np.zeros((width*height, 3), np.float32)
    objp[:, :2] = (np.mgrid[0:height, 0:width]*size).T.reshape(-1, 2)

    # Arrays to store object points and image points from all the images.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.
    global gray
    for fname in os.listdir(path):
        img = cv.imread(path+'/'+fname)

        global gray
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, (height, width), None)
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
            corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)
            # Draw and display the corners
    #         cv.drawChessboardCorners(img, (height, width), corners2, ret)
    #         cv.imshow('img', img)
    #         cv.waitKey(500)
    # cv.destroyAllWindows()

    # calibrate the camera
    ret, K, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    # calculate mean square error
    square_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], K, dist)
        error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
        # print(error)
        square_error += error

    rms = square_error/len(objpoints)

    return rms, K, dist

# # for debugging
# path = 'calibration_images'
#
# rms, K, dist = CalibrateCamera(path, 12, 9, 0.02)
#
# print(rms)
# print(K)
# print(dist)