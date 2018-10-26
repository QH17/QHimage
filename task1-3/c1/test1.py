import  cv2

img = cv2.imread("A:\\python\\graphics\\1.jpg")

dst = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("before",img)
cv2.imshow("after",dst)

cv2.waitKey(0)