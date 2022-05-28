from numpy import loadtxt
import TKTranslation
import TKCenterData
import TKFactorization
import TKDisplay3D

W = loadtxt('measurement_matrix.txt')
t = TKTranslation.TKTranslation(W)
W_bar = TKCenterData.TKCenterData(W, t)
M, X = TKFactorization.TKFactorization(W_bar)

TKDisplay3D.TKDisplay3D(X)
