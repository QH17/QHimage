import  numpy  as  np
import  cv2

#建立一个3X3的矩阵，其值为0
img = np.zeros((3,3), dtype=np.uint8)

#将这个3X3的矩阵打印到控制台
print("the value of img is:\n")
#灰度图
print(img)
print("\n")
#返回图像的行和列           .shape -> （行，列，通道数）若只有一个通道，则隐藏第三项
print(img.shape)

#将这个矩阵的格式转换成B-G-R格式
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

print("the value of BGR img is:\n")
#BGR图
print(img)
print("\n")
print(img.shape)

#将img保存为BGR格式图像
cv2.imwrite("storage.jpg",img)
