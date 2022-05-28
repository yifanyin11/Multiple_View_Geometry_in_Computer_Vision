import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

def TKTranslation(W):
    # extract dimensions
    m = int(np.size(W, axis=0) / 2)
    avg = np.average(W, axis=1).reshape((2*m, 1))
    t = avg.reshape((m, 2)).T
    return t

