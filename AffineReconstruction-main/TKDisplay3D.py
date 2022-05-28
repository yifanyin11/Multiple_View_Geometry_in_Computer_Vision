import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from numpy import loadtxt
import TKTranslation
import TKCenterData
import TKFactorization

def TKDisplay3D(X):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[0, :], X[1, :], X[2, :])
    ax.set_title('3D Reconstruction')
    plt.show()

# For testing
# W = loadtxt('measurement_matrix.txt')
# t = TKTranslation.TKTranslation(W)
# W_bar = TKCenterData.TKCenterData(W, t)
# M, X = TKFactorization.TKFactorization(W_bar)
#
# TKDisplay3D(X)


