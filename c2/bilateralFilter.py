#双边滤波
import  cv2

img = cv2.imread("1.jpg")

######################################################################
#进行双边滤波
#cv2.bilateralFilter(
#                   InputArray      src,
#                   OutputArray     dst,
#                   int             d,              滤波时选取的空间距离参数
#                   double          sigmaColor,     滤波时选取的颜色差值范围，
#                   double          sigmaSpace,     空间坐标中的sigma值，值越大，则参与滤波的像素越多
#                   int             borderType = BORDER_DEFAULT
#                   )
#
#   sigmaColor:     这个值决定了周围有哪些点能参与滤波计算，
#                   与当前像素点的像素值差值小于这个sigma值的像素将参与滤波运算。
#                   当取 255 时，当前像素点周围的所有点都将参与运算。
######################################################################
dst = cv2.bilateralFilter(img, d = 9, sigmaColor = 255, sigmaSpace = 0)

cv2.imshow("before", img)

cv2.imshow("after", dst)

cv2.waitKey(0)
