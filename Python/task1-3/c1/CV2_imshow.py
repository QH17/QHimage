#cv2.imshow 和 cv2.imread 的基本用法。

#导入opencv2模块
import cv2 as cv

#利用img变量储存1.jpg图像。
img = cv.imread("2.jpg")

#将img变量获得的信息显示出来。
cv.imshow("1.jpg",img)

#waitKey()函数用于判断是否有键盘按键被按下。
cv.waitKey(0)
