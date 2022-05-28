import cv2
import numpy as np

# p=np.matrix([[0.1,0.24,0.78,0.63],[0.8,0.603,0.20,0.78],[1,1,1,1]])

def DrawPolygon( p ):
    # remove last row of the matrix to obtain coordinates in Euclidean space, convert back to pixels in unit
    pointEuc=np.delete(p, 2, 0)*300
    # print(pointEuc)

    pointEuc = np.transpose(pointEuc)
    # covert the coordinates into integers
    pts = pointEuc.astype(np.int32)
    # print(pts)
    # pts = abs(pts)
    ptsxmin = np.min(pts, axis=0)[0, 0]
    ptsxmax = np.max(pts, axis=0)[0, 0]
    ptsymin = np.min(pts, axis=0)[0, 1]
    ptsymax = np.max(pts, axis=0)[0, 1]
    sidex = ptsxmax-ptsxmin
    sidey = ptsymax-ptsymin
    pts[:, 0] = pts[:, 0] + (50-ptsxmin)
    pts[:, 1] = pts[:, 1] + (50-ptsymin)
    # create a white image
    img = np.ones((sidex+100, sidey+100, 3), np.uint8) * 255
    # print(pts)
    pts = pts.reshape((-1, 1, 2))
    # print(pts)
    thickness = 2
    # draw the polygon
    cv2.polylines(img, [pts], True, (0, 0, 0),thickness)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# 
# DrawPolygon(p)