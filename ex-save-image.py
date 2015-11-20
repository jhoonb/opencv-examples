import cv2

# open image
img = cv2.imread('/home/godel/opencv/opencv-examples/images/python.png')

# save image (and change from .png to .jpg)
cv2.imwrite('python-logo.jpg', img)
