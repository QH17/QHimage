# detect 模块

  **版本**   | **兼容性** | **更新日期**
  ----      | -----      | ------
  v1.0      | windows    | 2018-10-26

### 此模块存在的问题：  
在使用此模块之前需要对此模块进行环境变量配置  
此模块目前只在windows中进行过测试  



此检测模块基于HAAR算法  

*** 此模块包括 ***

>`detect`
>>detect_front()  
>>detect_eye()  
>>img_detect_front()  
>>img_detect_eye()  

**此模块的使用方法：**

1.配置环境变量  
在python的安装环境中，site-packages下加入path.pth文件，用记事本打开，并向其中写入模块放置的绝对路径 

2.向.py文件中导入该模块

```python
import detect

detect.detect_front()

```

