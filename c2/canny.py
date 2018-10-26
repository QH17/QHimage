#canny边缘检测
import  cv2

#读取图像，并直接转换成灰度图
img = cv2.imread("img.jpg",cv2.IMREAD_GRAYSCALE)

#对图像进行二值化处理
#
# cv2.thershold(
#               InputArray      img,
#               OutputArray     src,
#               double          thresh,
#               double          maxval,
#               int             type
#               )
#
#thresh :设定阈值（一般来说，像素值大于该阈值时像素被填充为白色，否则为黑色）
#
#maxval :当type为THRESH_BINARY或者THRESH_BINARY_INV类型时，
#        需要设定最大值
########################################################
r,src = cv2.threshold(img,255,255,cv2.THRESH_TRIANGLE)

print(r)

#生成一个13x13的卷积核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(13,13))

#生成一个9x9的卷积核
kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))

#生成一个15x15的卷积核
kernel_2 = cv2.getStructuringElement(cv2.MORPH_RECT,(15,15))

#生成一个11x11的卷积核
kernel_3 = cv2.getStructuringElement(cv2.MORPH_RECT,(11,11))

#第一次腐蚀处理
dst = cv2.erode(src,kernel)

#对第一次腐蚀处理的图像进行膨胀处理
dlt = cv2.dilate(dst,kernel_1)

#对第一次膨胀处理后的图像进行第二次腐蚀处理
dst = cv2.erode(dlt,kernel)

#对第二次腐蚀处理的图像进行膨胀处理
dlt = cv2.dilate(dst,kernel_1)

#对第二次膨胀处理后的图像进行第三次腐蚀处理
dst = cv2.erode(dlt,kernel_3)

#对第三次腐蚀处理的图像进行膨胀处理
dlt = cv2.dilate(dst,kernel_2)

#描绘轮廓
#cv2.Canny(
#           InputArray      img,
#           OutputArray     src,
#           double          threshold1,
#           double          threshold2,
#           int             apeertureSize = 3,
#           bool            L2gradient = false
#           )
#
#apeertureSize为sobel算子的孔径大小
#L2gradient默认为false，若想让计算更加精确，选择true。
#一般来说，false就行了。通过改变这个bool值将改变计算算法。
################################################
canny = cv2.Canny(dlt,3,9,3)

cv2.imshow("after",dlt)

cv2.imshow("after canny",canny)

cv2.waitKey(0)