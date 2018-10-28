import  cv2         as  cv
import  numpy       as  np

#读取1.jpg文件，将信息保存到变量img中
img = cv.imread("2.jpg")

#将img中的RGB格式图像转换为灰度图
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#分别输出转换前和转换后的图像
cv.imshow("before",img)
cv.imshow("after",gray)

cv.waitKey(0)

#注意：若img读取的图像不为灰度图，则cvtColor（）不能使用COLOR_GRAY2HSV 或COLOR_GRAY2BGR等
#cv.cvtColor()中的两个成员分别是：1、由图像转换成的Mat类信息
#                               2、色彩空间转换码


#cvtColor(InputArray    src,       // 输入的原始图像
#         OutputArray   dst,       // 输出的图像
#         int           code,      // 色彩空间转换码
#         int           dstCn = 0) // 目标图像的通道数
#
#