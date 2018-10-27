# detect 模块

  **版本**   | **兼容性** | **更新日期** | **维护者**  
  ----      | -----      | ------ | -------
  `v1.0`    | windows    | 2018-10-26   | 1700402116  
  `v1.8`    | windows    | 2018-10-26   | 1700402116 

### 此模块存在的问题：  
在使用此模块之前需要对此模块进行环境变量配置  
此模块目前只在windows中进行过测试  



此检测模块基于HAAR算法  

***此模块包括***  

>`detect`
>>detect_front()：`调用摄像头进行正脸检测`  
>>detect_eye()：`调用摄像头进行眼部检测`  
>>detect_upperbody():`检测人物上半身`  
>>detect_lowerbody():`检测人物下半身`  
>>img_detect_front(filename)：`输入图像，对图像中的人进行正脸检测`  
>>img_detect_eye(filename)：`输入图像，对图像中的人进行眼部检测`  


**此模块的使用方法：**

1.配置环境变量  
在python的安装环境中，`site-packages`下加入`path.pth`文件，用记事本打开，并向其中写入模块放置的绝对路径 

2.向.py文件中导入该模块

```python
import detect

detect.detect_front()

```
#### v1.2更新内容
`v1.2`增加了两个新的函数用于检测人物的上半身和下半身，同时对模块中已有的函数进行了优化  
当前版本加入了一个带默认值的参数`cap_num`，该参数用于选择摄像头，默认值为0，设备上有多组摄像头时  
可以通过改变cap_num的值来切换用于读取图像的摄像头

v1.0版本的函数：
```python
def detect_front()
def detect_eye()
```
----

v1.2版本的函数：  
```python
def detect_front(cap_num = 0)
def detect_eye(cap_num = 0)
```
