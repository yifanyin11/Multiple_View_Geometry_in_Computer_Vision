import numpy as np
import cv2 as cv
import os
import RectifyImage

def drawlines(img1, img2, lines, pts1, pts2):

    r, c = img1.shape
    img1 = cv.cvtColor(img1, cv.COLOR_GRAY2BGR)
    img2 = cv.cvtColor(img2, cv.COLOR_GRAY2BGR)

    pts1 = pts1.tolist()
    pts2 = pts2.tolist()
    for r, pt1, pt2 in zip(lines, pts1, pts2):

        color = np.random.randint(0, 255, 3).tolist()
        color = tuple(color)

        x0, y0 = map(int, [0, -r[2]/r[1]])
        x1, y1 = map(int, [c, -(r[2]+r[0]*c)/r[1]])
        img1 = cv.line(img1, (x0, y0), (x1, y1), color, 1)

        img1 = cv.circle(img1, tuple(pt1), 5, color, -1)
        img2 = cv.circle(img2, tuple(pt2), 5, color, -1)
    return img1, img2

def DisplayKeypointsandLines( img1, img2, x, xp, lines1, lines2 ):
    lines1 = np.transpose(lines1).reshape(-1, 3)
    lines2 = np.transpose(lines2).reshape(-1, 3)
    img5, img6 = drawlines(img1, img2, lines2, x, xp)
    img3, img4 = drawlines(img2, img1, lines1, xp, x)
    cv.imshow('img1', img5)
    cv.imshow('img2', img3)
    cv.waitKey(0)
    cv.destroyAllWindows()
