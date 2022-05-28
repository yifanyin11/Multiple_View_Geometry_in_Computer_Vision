import cv2
import numpy as np

pointNum = 1

def picking(event, x, y, flags, param):
    global pointNum, coordinates, img
    # check whether a left click event happens
    if event == cv2.EVENT_LBUTTONDOWN:
        if pointNum == 1:
            coordinates = np.array([[x/300], [y/300], [1]])
        else:
            coordinates = np.append(coordinates, [[x/300], [y/300], [1]], axis=1)
        pointNum = pointNum+1
        # draw a circle to indicate a point has been selected
        cv2.circle(img, (x, y), 3, (255, 255, 0), -1)

def PointPicker( ):
    global pointNum, coordinates, img
    img = cv2.imread('dots.jpg', 0)
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', picking)

    # img = cv2.imread('dots.jpg', 0)
    # cv2.namedWindow('image')
    # cv2.setMouseCallback('image',picking)

    while (1):
        cv2.imshow('image', img)
        if cv2.waitKey(20) > 0:
            break

    cv2.destroyAllWindows()

    return coordinates

# coord = PointPicker()
# print(coord)

