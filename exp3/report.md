# 图像关键点检测及图像拼接
#### 202410315009 人工智能241 孙昭 </div>

## 一、实验目的
图像关键点检测及图像拼接实验报告，基于SIFT特征检测算法和FLANN特征匹配方法，实现两幅图像的特征点提取、匹配和自动拼接，掌握图像配准和融合的基本原理与实现方法。

## 二、实验内容
### 1.导入依赖库
<img width="283" height="77" alt="image" src="https://github.com/user-attachments/assets/be88a1d7-5436-4293-a555-35b2394cbb40" />

### 2.图像初始化和预处理
<p>导入图片，将图像转化为灰度图</p>
<img width="483" height="164" alt="image" src="https://github.com/user-attachments/assets/0d30ad24-b13c-4d22-b889-3f13405e0fc8" />
<P> 初始图1：</P>
<img alt="p1" src="https://github.com/user-attachments/assets/4a03d2d0-efed-4604-8214-2bf6931d11ed" width=50%/>
<p> 初始图2：</p>
<img alt="p2" src="https://github.com/user-attachments/assets/f3823a0a-0fc4-4167-87d7-7842eae18f75" width=50%/>


### 3.关键点检测
<p> 先初始化SIFT检测器并提取特征，再使用FLANN匹配器进行特征匹配，然后应用Lowe's比率测试筛选优质匹配点，最后绘制匹配的SIFT关键点 </p>
<img width="484" height="359" alt="image" src="https://github.com/user-attachments/assets/4d8bb18d-ac1f-44f0-a40c-271cf1c3803f" />
<p> 结果图：</p>
<img width="1274" height="626" alt="image" src="https://github.com/user-attachments/assets/60349047-9b5d-43be-9e58-b2386e72e430" />






