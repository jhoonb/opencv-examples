import numpy as np
import cv2

color = (255, 0, 0)

# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 100, color, 2)

# create a black image
img = np.zeros((500, 500, 3), np.uint8)
cv2.namedWindow('example4')
cv2.setMouseCallback('example4', draw_circle)

while True:
    cv2.imshow('example4', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()
