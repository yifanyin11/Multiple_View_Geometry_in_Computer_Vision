import numpy as np
import TKTranslation

def TKCenterData(W, t):
    # extract the dimension
    m = int(np.size(W, axis=0) / 2)
    # reshape the translation array
    t = t.T.reshape((2*m, 1))
    W_bar = W-t
    return W_bar

# A = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
# print(A)
# t = TKTranslation.TKTranslation(A)
# W_bar = TKCenterData(A, t)
# print(W_bar)

