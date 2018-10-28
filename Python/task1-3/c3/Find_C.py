import  cv2

def find(img,x,y):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    dst = cv2.inRange(gray,x,y)

    cv2.imshow("2",dst)

    cnt = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

    c = max(cnt,key = cv2.contourArea)

    ((x,y),radius) = cv2.minEnclosingCircle(c)

    M = cv2.moments(c)
    print(M)
    center = (int(M["m10"]/(0.01+M["m00"])), int(M["m01"]/(0.01+M["m00"])))  
    ptx=int(M["m10"]/(0.01+M["m00"]))
    pty=int(M["m01"]/(0.01+M["m00"]))

    cv2.circle(img,center,20,(255,0,0),3)

    cv2.imshow("after",img)

    cv2.waitKey(0)



img = cv2.imread("t.jpeg")

find(img,200,255)
