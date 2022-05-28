import numpy as np
import cv2 as cv
def FundamentalMatrix( x, xp ):
    x = np.asarray(x)
    xp = np.asarray(xp)
    F, mask = cv.findFundamentalMat(x, xp, cv.FM_8POINT)
    return F
