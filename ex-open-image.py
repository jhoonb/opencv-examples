# opencv lib
import cv2

# open image (insert the complete path)
img = cv2.imread('/home/godel/opencv/opencv-examples/images/chola.png')
# show
cv2.imshow("Example - 1", img)
# any key
cv2.waitKey(0)
# destroy
cv2.destroyAllWindows()
