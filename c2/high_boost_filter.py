#高通滤波器 --- >  高频提升滤波器

#导入cv2
import cv2
#导入 numpy 模块，并命名为 np
import numpy as np
#从 scipy 模块中导入 ndimage() 函数
from scipy import ndimage

#生成一个3×3的卷积矩阵
kernel_3x3 = np.array([[-1,-1,-1],
                        [-1,8,-1],
                        [-1,-1,-1]])

#生成一个5×5的卷积矩阵
kernel_5x5 = np.array([[-1,-1,-1,-1,-1],
                        [-1, 1, 2, 1,-1],
                        [-1, 2, 4, 2,-1],
                        [-1, 1, 2, 1,-1],
                        [-1,-1,-1,-1,-1]])

#读取图像，并转化为灰度图 
#因为cv2.IMREAD_GRAYSCALE = 0
#所以也可以将第二个元素直接写成 0
img = cv2.imread("2.jpg", 0)

#将这个灰度图显示出来
cv2.imshow("img", img)

#将获取的图像与自定义的 3x3卷积矩阵 进行卷积运算。
#convolve ------------> 卷积
kernel_3 = ndimage.convolve(img, kernel_3x3)

#将获取的图像与自定义的 5x5卷积矩阵 进行卷积运算。
kernel_5 = ndimage.convolve(img, kernel_5x5)

#高斯滤波算法
#cv2.GaussianBlur(
#                   InputArray      src,                            #输入的图像数组
#                   OutputArray     dst,                            #输出的图像数组
#                   Size            Ksize,                          #卷积核的大小（核的宽度与高度可以不同，但一定要为正奇数或0）
#                   double          sigmaX,                         #表示核在X轴方向的标准偏差
#                   double          sigmaY = 0,                     #表示核在Y轴方向的标准偏差，当该值为0时，表示与sigmaX取同样的值
#                   int             borderType = BORDER_DEFAULT)    #边框样式
blurred = cv2.GaussianBlur(img, (11,11), 0)

#将高斯滤波得到的图像与读取的图像相减
g_hpf = img - blurred

#显示使用 3x3卷积核 结果下的图像
cv2.imshow("3x3", kernel_3)

#显示使用 5x5卷积核 结果下的图像
cv2.imshow("5x5", kernel_5)

#显示高斯滤波与原图相减后得到的图像
cv2.imshow("g_hpf", g_hpf)

cv2.waitKey(0)