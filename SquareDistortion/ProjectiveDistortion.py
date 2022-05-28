import cv2
import numpy as np

# point=np.matrix([[0.07, 1.0667, 1.0767, 0.07],[0.067,0.06,1.07,1.063],[1,1,1,1]])

def ProjectiveDistortion(ph):
    # define the mapped matrix
    php = np.zeros([3, np.size(ph,1)])
    # define homography H
    H = np.matrix([[1,0,0],[0,1,0],[1,1,1]])

    # do the mapping
    php = np.matmul(H, ph)
    for i in range(np.size(ph, axis=1)):
        php[:, i] = php[:, i] / php[2, i]

    # print(ph)
    # print(php)
    return php

# ppp=ProjectiveDistortion(point)
#
# print(ppp)

