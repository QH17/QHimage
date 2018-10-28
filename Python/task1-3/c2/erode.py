#腐蚀处理函数
#
#一般来说，腐蚀处理与膨胀处理都为二值化图像处理函数。
#
#先对图像进行二值化处理，再对图像进行腐蚀或膨胀
##################################################################################
import  cv2

#采集目标图像
img = cv2.imread("1.jpg")

#getStructuringElement() 函数可用于构造一个特定大小和形状的结构元素，用于图像形态学处理.
#
#cv2.getStructuringElement(
#                           int     shape       结构元素的形状
#                           Size    Ksize       结构元素的大小
#                           Point   Anchor      锚点坐标，默认(-1，-1)，位于元素中心
#                          )
#
#这里的shape可以是：
#               MORPH_RECT      (矩形)
#               MORPH_CROSS     (十字星型)
#               MORPH_ELLIPSE   (椭圆)
#对应了三种核的形状
##################################################################################
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
##################################################################################
#erode() 函数用于腐蚀图像
#
#cv2.erode(
#           InputArray      src,                            输入的图像
#           OutputArray     dst,                            输出的图像
#           InputArray      kernel,                         用于处理图像的卷积核
#           Point           anchor = Point(-1,-1),          锚点（默认在图像的中心）
#           int             iterations = 1,                 迭代次数（默认为1，即只腐蚀一次）
#           int             borderType = BORDER_CONSTANT,   边界处理方法
#           const           Scalar & borderValue = morphologyDefaultBorderValue()
#           )
#
#borderType ：
#   大多数用到卷积操作的OpenCV函数都是将给定图像拷贝到另一个轻微变大的图像中，
#   然后自动填充图像边界(通过下面示例代码中的各种方式)。
#   这样卷积操作就可以在边界像素安全执行了(填充边界在操作完成后会自动删除)。
#   BORDER_CONSTANT: 使用常数填充边界 (i.e. 黑色或者 0)
#   BORDER_REPLICATE: 复制原图中最临近的行或者列。
##################################################################################
dst = cv2.erode(img,kernel)

cv2.imshow("before",img)

cv2.imshow("after",dst)

cv2.waitKey(0)
##################################################################################
#                           end of file                                          #
##################################################################################