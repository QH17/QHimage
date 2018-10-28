import  cv2

gray = cv2.imread("3.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow("gray",gray)
#
#cv2.inRange(
#           InputArray      src,
#           InputArray      lowerb,
#           InputArray      upper,
#           OutputArray     dst
#           )
##########################################
mask = cv2.inRange(gray,254,255)

cv2.imshow("mask",mask)

cv2.waitKey(0)
