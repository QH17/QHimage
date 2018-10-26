import  cv2

def find(img,x,y):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    dst = cv2.inRange(gray,x,y)

    cv2.imshow("2",dst)

    cnt = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

    c = max(cnt,key = cv2.contourArea)

    ((x,y),radius) = cv2.minEnclosingCircle(c)

    M = cv2.moments(c)

    center  =  (int(M["m10"]/(0.01+M["m00"])), int(M["m01"]/(0.01+M["m00"])))
    ptx     =   int(M["m10"]/(0.01+M["m00"]))
    pty     =   int(M["m01"]/(0.01+M["m00"]))

    print(center)
    print(ptx)
    print(pty)

    cv2.circle(img,center,5,(255,0,0),5)

    cv2.imshow("after",img)


cap = cv2.VideoCapture(1)

while True:

    retval,frame = cap.read()

    #find(frame,253,255)

    cv2.imshow("1",frame)

    cv2.waitKey(1)
