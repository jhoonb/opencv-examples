import numpy as np
import cv2


color = (100, 255, 0)
color2 = (1, 100, 60)
drawing = False
mode = True
ix, iy = -1,-1

#mouse callback function

def draw(event, x, y, flags, param):
    global drawing, mode, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), color, -1)
            else:
                cv2.circle(img, (x, y), 5, color2, -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix,iy), (x,y), color, -1)
        else:
            cv2.circle(img, (x, y), 20, color2, -1)
    else:
        pass


img = np.zeros((600, 600, 3), np.uint8)
cv2.namedWindow('example5')
cv2.setMouseCallback('example5', draw)

while True:
    cv2.imshow('example5', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break


cv2.destroyAllWindows() 
