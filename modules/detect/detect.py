import cv2

##################################################################################################
#用于检测正脸的函数
def img_detect_front(filename):
    """
    import array:image contains front faces.
    """
    #将人脸识别的区域设定为正脸
    face_cascade=cv2.CascadeClassifier('detect\\haarcascade_frontalface_default.xml')
    #读取filename中的图像
    img=cv2.imread(filename)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #将实时检测得到的人脸数据传给faces
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    #判断：若faces为空（这里不能用None），则退出该函数
    if faces == ():
        print("front face detection failure！")
        return
    #若检测到人像，则将人像用矩形圈出
    for (x,y,h,w) in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),20)

    cv2.namedWindow('faces Detected!')
    #重新定义图片的大小，缩放为原来的0.2倍
    img = cv2.resize(img,None, fx = 0.2, fy = 0.2,interpolation = cv2.INTER_CUBIC)
    #将图像打印出来
    cv2.imshow('faces Detected!',img)
    cv2.waitKey(0)

###################################################################################################

#用于检测眼部的函数
def img_detect_eye(filename):
    """
    import array:image contains eyes.
    """
    #将人脸识别区域设置为眼部
    eye_cascade=cv2.CascadeClassifier('detect\\haarcascade_eye.xml')
    #读取图像
    img=cv2.imread(filename)
    #转换为灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray,1.3,5)
    #判断：若faces为空（这里不能用None），则退出该函数
    if eyes == ():
        print("eyes detection failure！")
        return
    #若检测到人像，则将人像用矩形圈出
    for (x,y,h,w) in eyes:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),20)
    cv2.namedWindow('eyes Detected!')
    #重新定义图片的大小，缩放为原来的0.2倍
    img = cv2.resize(img,None, fx = 0.2, fy = 0.2,interpolation = cv2.INTER_CUBIC)
    #将图像打印出来
    cv2.imshow('eyes Detected!',img)
    cv2.waitKey(0)

####################################################################################################
#                                 读取视频中的人像信息                                               #
####################################################################################################
def detect_front(cap_num = 0):
    """
    detect_front(cap_num)
    cap_num: select an video path. (default 0)
    """
    #人像识别区域：正脸
    face_cascade = cv2.CascadeClassifier('detect\\haarcascade_frontalface_default.xml')    
    #开启编号为0的摄像头
    camera = cv2.VideoCapture(cap_num)
    #进入循环
    while True:
        #读取摄像头的帧
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #检测面部信息
        faces = face_cascade.detectMultiScale(gray, 1.8, 5)

        #如果面部信息不存在
        if faces == ():
            img = frame
        
        #若面部信息存在
        for(x,y,w,h) in faces:
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10)
        
        #将图像打印出来
        cv2.imshow("frontface Mode",img)
        cv2.waitKey(1)

####################################################################################################

def detect_eye(cap_num = 0):
    """
    detect_eye(cap_num)
    cap_num: select an video path. (default 0)
    """
    eye_cascade = cv2.CascadeClassifier('detect\\haarcascade_eye.xml')
     #开启编号为0的摄像头
    camera = cv2.VideoCapture(cap_num)

    #进入循环
    while True:
        #读取摄像头的帧
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #检测眼部信息
        eyes  = eye_cascade.detectMultiScale(gray,1.5,5,0,(40,40))

        #如果眼部信息不存在
        if eyes == ():
            img = frame
        
        #若眼部信息存在
        for (ex,ey,ew,eh) in eyes:
            img = cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        #将图像打印出来
        cv2.imshow("eyes Mode",img)
        cv2.waitKey(1)
####################################################################################################
#                                 读取视频中的全身信息                                               #
####################################################################################################
def detect_fullbody(cap_num = 0):
    """
    detect_fullbody(cap_num)
    cap_num: select an video path. (default 0)
    """
    #人像识别区域：正脸
    face_cascade = cv2.CascadeClassifier('detect\\haarcascade_fullbody.xml')    
    #开启编号为0的摄像头
    camera = cv2.VideoCapture(cap_num)
    #进入循环
    while True:
        #读取摄像头的帧
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #检测面部信息
        body = face_cascade.detectMultiScale(gray, 1.8, 5)
        #如果面部信息不存在
        if body == ():
            img = frame
        
        #若面部信息存在
        for(x,y,w,h) in body:
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10)

        #将图像打印出来
        cv2.imshow("fullbody Mode",img)
        cv2.waitKey(1)
####################################################################################################
#                                 读取视频中的人像上半身信息                                         #
####################################################################################################
def detect_upperbody(cap_num = 0):
    """
    detect_upperbody(cap_num)
    cap_num: select an video path. (default 0)
    """
    #人像识别区域：正脸
    face_cascade = cv2.CascadeClassifier('detect\\haarcascade_upperbody.xml')    
    #开启编号为0的摄像头
    camera = cv2.VideoCapture(cap_num)
    #进入循环
    while True:
        #读取摄像头的帧
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #检测面部信息
        body = face_cascade.detectMultiScale(gray, 1.8, 5)
        #如果面部信息不存在
        if body == ():
            img = frame
        
        #若面部信息存在
        for(x,y,w,h) in body:
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10)

        #将图像打印出来
        cv2.imshow("upperbody Mode",img)
        cv2.waitKey(1)
########################################################################################
def detect_lowerbody(cap_num = 0):
    """
    detect_lowerbody(cap_num)
    cap_num: select an video path. (default 0)
    """
    #人像识别区域：正脸
    face_cascade = cv2.CascadeClassifier('detect\\haarcascade_lowerbody.xml')    
    #开启编号为0的摄像头
    camera = cv2.VideoCapture(cap_num)
    #进入循环
    while True:
        #读取摄像头的帧
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #检测面部信息
        faces = face_cascade.detectMultiScale(gray, 1.8, 5)

        #如果面部信息不存在
        if faces == ():
            img = frame
        
        #若面部信息存在
        for(x,y,w,h) in faces:
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10)
        
        #将图像打印出来
        cv2.imshow("lowerbody Mode",img)
        cv2.waitKey(1)
