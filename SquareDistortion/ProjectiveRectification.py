import cv2
import numpy as np
import DrawPolygon

# p=np.matrix([[0.06,0.501,0.34,0.03],[0.058,0.028,0.34,0.4983],[1,1,1,1]])

def ProjectiveRectification( pp ):
    l1 = np.cross(np.transpose(pp[:, 0]), np.transpose(pp[:, 1]))
    l2 = np.cross(np.transpose(pp[:, 3]), np.transpose(pp[:, 2]))
    p1 = np.cross(l1, l2)
    p1 = p1/p1[0, 2]
    # print(p1)
    l3 = np.cross(np.transpose(pp[:, 0]), np.transpose(pp[:, 3]))
    l4 = np.cross(np.transpose(pp[:, 1]), np.transpose(pp[:, 2]))
    p2 = np.cross(l3, l4)
    p2 = p2/p2[0, 2]
    l_inf = np.cross(p1, p2)

    Hpr = np.eye(3)
    Hpr[2, :] = l_inf
    p_rect = np.matmul(Hpr, pp)
    # print(p_rect)
    for i in range(np.size(p_rect,axis=1)):
        p_rect[:,i] = p_rect[:,i]/p_rect[2,i]
    DrawPolygon.DrawPolygon(p_rect)
    # print(p_rect)
    # print(pp)
    return Hpr


# Hpr = ProjectiveRectification(p)
# print(Hpr)