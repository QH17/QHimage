import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

kernel_2 = np.ones((2,2),np.uint8)
kernel_3 = np.ones((3,3),np.uint8) 
kernel_4 = np.ones((4,4),np.uint8)

#cap.set(cv2.cv.CV_CAP_PROP_FPS,60)
while(1):
    #得到一帧图像
    ret, frame = cap.read()
    
    #转换成灰度图
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #将灰度化以后的帧显示出来
    cv2.imshow("gray", gray)

    #对灰度在240到255之间的像素进行掩模处理
    mask = cv2.inRange(gray,240,255)

    #腐蚀和膨胀处理
    erosion = cv2.erode(mask,kernel_4,iterations = 1)  
    erosion = cv2.erode(erosion,kernel_4,iterations = 1)  
    dilation = cv2.dilate(erosion,kernel_4,iterations = 1)  
    dilation = cv2.dilate(dilation,kernel_4,iterations = 1)

    #将图像显示出来
    cv2.imshow("capture", mask)

    #中心设为None（复位）
    center = None

    #开始寻找轮廓
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    #如果没有找到（长度小于等于0）
    if len(cnts) <= 0:           
        print('not find')

    #如果找到
    if len(cnts) > 0:

        #取最大轮廓
        c = max(cnts, key = cv2.contourArea)

        #寻找最小包围圆
        ((x,y), radius) = cv2.minEnclosingCircle(c)

        #计算图像矩，并以字典形式返回
        M = cv2.moments(c)
        
        #求出中心点（置位）
        center = (int(M["m10"]/(0.01+M["m00"])), int(M["m01"]/(0.01+M["m00"])))  
        
        #求出重心坐标
        ptx=int(M["m10"]/(0.01+M["m00"]))
        pty=int(M["m01"]/(0.01+M["m00"]))

        print(ptx)
        print(pty)
        if radius > 0:  
            cv2.circle(frame, center, 5, (0, 255, 0), -1)  
        else:
            cv2.putText(frame,' ', cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        cv2.imshow('frame',frame)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 
