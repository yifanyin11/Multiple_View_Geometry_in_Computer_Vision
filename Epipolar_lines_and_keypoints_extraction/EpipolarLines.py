import numpy as np
import cv2 as cv
import FundamentalMatrix

def EpipolarLines(x, xp, F):
    # lines1 = cv.computeCorrespondEpilines(x.reshape(-1, 1, 2), 1, F)
    # lines1 = np.transpose(lines1)
    #
    # lines2 = cv.computeCorrespondEpilines(xp.reshape(-1, 1, 2), 2, F)
    # lines2 = np.transpose(lines2)
    lines1 = cv.computeCorrespondEpilines(x.reshape(-1, 1, 2), 1, F)
    lines1 = np.transpose(lines1)

    lines2 = cv.computeCorrespondEpilines(xp.reshape(-1, 1, 2), 2, F)
    lines2 = np.transpose(lines2)

    return lines1, lines2
