# drawing different geometric shapes

import numpy as np
import cv2

# create a black image
# matrix (width, height, channel)
# uint8 -> 0...255 
img = np.zeros((500, 500, 3), np.uint8)

# color tuple (R,G,B), in numpy it's reverse (B,G,R)
blue = (255, 0, 0)
red = (0, 0, 255)
yellow = (0, 255, 255)
pink = (219, 0, 255)
gray = (141, 141, 141)

# - line
# draw a diagonal blue line with thickess of 6px
img = cv2.line(img, (0, 0), (494, 498), blue, 6)

# - retangle
# draw a yellow rectangle with thickness of 4px
img = cv2.rectangle(img, (10, 10), (394, 370), yellow, 4)

# - circle
# draw a red circle with thickness of 8px
cv2.circle(img, (300, 60), 60, red, 8)

# - ellipse
img = cv2.ellipse( img, (256, 256), (100, 50), 0, 0, 360, pink, 3)

# - polygon
# make points in array
pts = np.array([[20, 20], [40, 50], [70,10], [30,100]], np.int32)
pts = pts.reshape((-1, 1, 2))
#img = cv2.polylines(img, [pts], False, gray)
img = cv2.polylines(img, [pts], True, gray, 2)

# - text
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, ":) TEST", (10,450), font, 2, pink, 2, cv2.LINE_AA)

# show 
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
