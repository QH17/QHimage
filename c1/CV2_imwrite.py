import  cv2     as  cv

#将 1.jpg 的信息读取到变量 img 中
img = cv.imread("1.jpg")

#将 img 变量中的图片信息保存为一个 write.jpg 的图像
cv.imwrite("write.jpg",img)

#用变量wrt读取write.jpg的信息
wrt = cv.imread("write.jpg")

#将wrt中所含的图像信息打印出来
cv.imshow("write",wrt)

cv.waitKey(0)

