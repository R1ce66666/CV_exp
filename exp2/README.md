# <div align="center"> 实验二 图像增强 </div>
<p> <div align='right'> 202410315009 人工智能 孙昭 </div> </p>

##  一、实验目的
学会OpenCV的基本使⽤⽅法，利⽤OpenCV等计算机库对图像进⾏平滑、滤波等操作，实现图像增强。

## 二、实验内容
### 2.1导入图像滤波相关依赖包
1.OpenCV库：计算机视觉与图像处理<br>
2.scikit-image库：图像增强与分析，random_noise ⽤于给图像添加噪声<br>
3.NumPy库：科学计算的基础库<br>
4.Matplotlib库：绘图与数据可视化<br>

下图即为导入依赖库的代码：
<div align="center"> <img width="381" height="134" alt="image" src="https://github.com/user-attachments/assets/1820ef8b-6920-4ebb-a756-91a253bcb96f" /> </div>

### 2.2 读取原始图像并进⾏⾊彩空间转换
读取计算机本地图像⽂件，获取并输⼊【500，750】处像素点的BGR参数并输出,通过下⾯的输出结果可以看到，【500,750】像素点的RGB为【109 74 54】，表示为红褐色，通过图像可以看出该点在人物嘴唇的部分。
如下图所示：
<div align="center"> <img width="545" height="185" alt="image" src="https://github.com/user-attachments/assets/876966ec-7a10-4d89-b146-5a0e221241e8" /></div>
输出：
<div align="center"> <img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/bc113b73-6089-4fce-88c4-4dd9bf10e7bb" /> </div>
然后测试⼀下cv2中颜⾊空间变换的效果，这⾥的cv2.cvtColor就是颜⾊空间转换，cv2.COLOR_BGR2RGB代表的是将原始图像BGR格式转换成RGB格式，蓝⾊和红⾊互换，因为把'B'和'R'通道互换了，所以这是⼀个红蓝的颜⾊反转:
<div align="center"> <img width="752" height="154" alt="image" src="https://github.com/user-attachments/assets/12dec91b-f581-47c3-ac7f-8a4e07380070" /> </div>
红蓝反转图：
<div align="center"> <img width="400" height="400" alt="rgb_image" src="https://github.com/user-attachments/assets/ebdd20f6-9c31-446f-abaa-a60066468f49" /> </div>
cv2.COLOR_BGR2GRAY是将原始图像的RBG格式转换为灰度图，将三维的RGB通道映射为⼀维的灰度通道

如下图所示：
<div align="center"> <img width="752" height="160" alt="image" src="https://github.com/user-attachments/assets/3dcb81cf-5ea3-4ae4-8d8e-ea7ef9621318" /> </div>
灰度图像：
<div align="center"> <img width="400" height="400" alt="gray_image" src="https://github.com/user-attachments/assets/6f252a6a-9819-4588-b8fa-cc30ae773954" /> </div>

### 2.3 添加噪声
这⾥在原始图像的基础上添加噪声，引⼊了两个API⽅法，椒盐噪声和⾼斯噪声，通过对⽐可以发现，椒盐噪声和⾼斯噪声的本质不同，椒盐噪声表现为像素会随机替换为⽩⾊或者⿊⾊像素（灰度通道），在RGB通道表现为像素变成随机彩⾊点，⽽⾼斯噪声会在每个像素上添加随机偏差，服从⾼斯分布
如下图所示：
<div align="center"> <img width="760" height="307" alt="image" src="https://github.com/user-attachments/assets/03c00c1b-c0eb-4676-8669-964d3caeb011" /> </div>
噪声对比图：
<div align="center"> <img alt="noise_image" src="https://github.com/user-attachments/assets/14ab446d-737b-4364-8808-42db6277927b" width=70%> </div>

### 2.4 图像滤波
将图像认为产⽣噪声后，⽤OpenCV的三个API滤波⽅式进⾏对⽐，分别对椒盐滤波和⾼斯滤波使⽤【均值滤波】，【中值滤波】，【⾼斯滤波】，对⽐每个最适合的滤波⽅式。
如下图所示：
<div align="center"> <img width="680" height="586" alt="image" src="https://github.com/user-attachments/assets/e98c7dd9-edf1-49a8-a493-5cb990094785" /> </div>
滤波对比图：
<div align="center"> <img alt="blur_image" src="https://github.com/user-attachments/assets/82690221-c75f-4a40-b699-029d429e62d8" width=70%> </div>

## 三、实验结果及分析










