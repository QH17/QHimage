#方框滤波函数
import  cv2

#读取图像，存储于 img 中
img = cv2.imread("1.jpg")

#result = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#################################################################
#进行方框滤波
#cv2.boxFilter(
#               InputArray      src,
#               OutputArray     dst,
#               int             ddepth,
#               Size            Ksize,
#               Point           anchor = Point(-1,-1),
#               bool            normalize = true,           归一化处理
#               int             borderType = BORDER_DEFAULT,
#              )
#################################################################
dst = cv2.boxFilter(img, -1, (5,5),normalize=False)

cv2.imshow("before",img)

cv2.imshow("after",dst)

cv2.waitKey(0)