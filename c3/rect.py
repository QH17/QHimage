import cv2

img = cv2.imread("1.jpg")


#用来画矩形的函数：
#cv2.rectangle(
#               InputArray      img,
#               Point           pt1,
#               Point           pt2,
#               Scalar          color,
#               int             thickness = None,              
#               LineType = None,
#               shift    = None
#           )
#
#该函数通过确定对角线来画矩形。
##########################################################
src = cv2.rectangle(img,(100,100),(140,140),(0,0,255),3)

cv2.imshow("1",src)

cv2.waitKey(0)