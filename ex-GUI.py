import numpy as np
import cv2


def nothing():
    pass


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('example6')

cv2.createTrackbar('R', 'example6', 0, 255, nothing)
cv2.createTrackbar('G', 'example6', 0, 255, nothing)
cv2.createTrackbar('B', 'example6', 0, 255, nothing)

switch = '0: OFF \n1 : ON'
cv2.createTrackbar(switch, 'example6', 0, 1, nothing)

while True:
    cv2.imshow('example6', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos('R', 'example6')
    g = cv2.getTrackbarPos('G', 'example6')
    b = cv2.getTrackbarPos('B', 'example6')
    s = cv2.getTrackbarPos(switch, 'example6')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()
 
 


    
