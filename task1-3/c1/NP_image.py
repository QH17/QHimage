import  cv2
import  numpy   as  np
import  os

#字节数：900
random = bytearray(os.urandom(900))

#flat数组中随机生成900个字节
flat   = np.array(random)

#将flat的形状变为30X30      30*30 = 900
gray   = flat.reshape(30,30)
cv2.imwrite("gray.jpg",gray)

#将flat的形状变为1X3        10*30*3 = 900
bgr    = flat.reshape(10,30,3)
cv2.imwrite("bgr.png",bgr)