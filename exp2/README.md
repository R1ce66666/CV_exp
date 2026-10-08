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
<div align="center"> <img alt="blur_image" src="https://github.com/user-attachments/assets/0b055348-b111-42f0-b1c4-c651bd6b889f" width=70%> </div>

## 三、实验结果及分析
### 1. 原始图像与颜色空间转换
使用 OpenCV 读取图像，其默认存储顺序为 BGR，直接用 matplotlib 显示会出现色彩错乱。转换为 RGB 后，色彩与现实一致。
### 2. 噪声添加效果
椒盐噪声为随机黑白噪点，局部破坏明显。高斯噪声服从正态分布，在整张图均匀出现，图像整体轻微模糊。对比可见，椒盐噪声是局部独立干扰，高斯噪声为全局连续扰动。
### 3. 滤波去噪效果
均值滤波依靠邻域平均平滑图像，抑制高斯噪声效果较好，但易模糊边缘，难以清除椒盐噪点。<br>
中值滤波采用邻域取中值，去除椒盐噪声效果突出，边缘保留能力更强，对高斯噪声仅有有限抑制。<br>
高斯滤波使用高斯核加权平均，处理高斯噪声效果最优，平滑效果自然，但对椒盐噪声效果差。<br>
### 总体分析
噪声类型决定滤波方案：椒盐噪声适合中值滤波，可剔除极值噪点并保护边缘；高斯噪声适合均值或高斯滤波进行全局平滑。

## 四、实验小结
本实验完成彩色图像读取、BGR转RGB、灰度图显示，并给图像添加椒盐噪声和高斯噪声。使用均值滤波、中值滤波、高斯滤波去除噪声产生出不同的效果。
实验结果表明：中值滤波去除椒盐噪声效果最好，可较好保留图像边缘；均值滤波适合高斯噪声；高斯滤波也适合高斯噪声
这次实验让我直观体会到不同噪声的特点以及各类滤波算法的适用场景。亲手实现滤波时，整体加深了对图像滤波原理的理解，也锻炼了代码调试能力，为后续学习图像处理打下基础。












