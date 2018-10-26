#均值滤波函数
import  cv2

img = cv2.imread("2.jpg")

#########################################################################
#cv2.blur(
#           InputArray      src,        输入的图像
#           OutputArray     dst,        输出的图像
#           Size            Ksize,      卷积核大小
#           Point           Anchor = (-1,-1),           锚点坐标
#           int             borderType=BORDER_DEFAULT   边界类型
#        )
#
#将核的锚点放在该特定位置的像素上，同时，核内的其他值与该像素邻域的各像素重合；
#将核内各值与相应像素值相乘，并将乘积相加；
#将所得结果放到与锚点对应的像素上；
#对图像所有像素重复上述过程。
#
#########################################################################
dst = cv2.blur(img,(5,5))

cv2.imshow("before", img)

cv2.imshow("after", dst)

cv2.waitKey(0)
