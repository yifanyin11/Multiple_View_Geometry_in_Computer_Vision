import cv2
import numpy as np

# p=np.matrix([[0.07, 1.0667, 1.0767, 0.07],[0.067,0.06,1.07,1.063]])
# p=np.transpose(p)
# pp=np.matrix([[0.06,0.501,0.34,0.03],[0.058,0.028,0.34,0.4983]])
# pp=np.transpose(pp)


def OpenCVRectification( p, pp ):
    p = np.delete(p,2,0)
    p = np.transpose(p)
    pp = np.delete(pp,2,0)
    pp = np.transpose(pp)
    M, mask = cv2.findHomography(p, pp, cv2.RANSAC, 5.0)
    return M

# M=OpenCVRectification(p,pp)
# print(M)