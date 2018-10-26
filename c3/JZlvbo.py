import cv2
import numpy as np
img=cv2.imread("t.jpeg")
img1=cv2.blur(img,(3,3))
cv2.imshow("before",img)
cv2.imshow("after",img1)
cv2.waitKey(0)

