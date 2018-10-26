#中值滤波
import  cv2

#导入图像
img = cv2.imread("t.jpeg")

###############################################
#进行中值滤波
#cv2.medianBlur(
#               InputArray      src,
#               OutputArray     dst,
#               int             Ksize
#               )
###############################################
result = cv2.medianBlur(img, 15)

cv2.imshow("before",img)

cv2.imshow("after", result)

cv2.imwrite("img.jpg",result)

cv2.waitKey(0)