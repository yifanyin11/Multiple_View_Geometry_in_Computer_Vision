import numpy as np
import TKTranslation
import TKCenterData

def TKFactorization(W):
    u, s, vh = np.linalg.svd(W, full_matrices=True)
    S = np.diag(s[:3])
    M = np.matmul(u[:, :3], np.diag(s[:3]))
    # print(M.shape)
    X = vh[:3, :]
    # print(X.shape)
    return M, X

# A = np.array([[1,2,8],[3,4,0],[5,6,9],[7,8,1],[9,10,11],[11,12,3]])
# # # print(A)
# # t = TKTranslation.TKTranslation(A)
# # W_bar = TKCenterData.TKCenterData(A, t)
# # # print(W_bar)
# # M, X = TKFactorization(W_bar)



