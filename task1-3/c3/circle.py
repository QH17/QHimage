import  cv2

img = cv2.imread("2.JPG")

#用来画圆的函数：
#cv2.rectangle(
#               InputArray      img,
#               Point           center,
#               int             Radius,
#               Scalar          color,
#               int             thickness = None,              
#               LineType = None,
#               shift    = None
#           )
#
##########################################################
src = cv2.circle(img,(200,200),50,(0,0,0),3)

cv2.imshow("circle",src)

cv2.waitKey(0)