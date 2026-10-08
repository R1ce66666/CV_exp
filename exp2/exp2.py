#%%
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.util import random_noise
plt.rcParams['font.sans-serif'] = ['SimHei']      # 中文字体，黑体
plt.rcParams['axes.unicode_minus'] = False

#%%
img=cv2.imread(r'C:\Users\14627\Desktop\cj.jpg')
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(b,g,r)=img[100,100]
print(b,g,r)
plt.subplot(1,3,1)
plt.imshow(img)
plt.title('原图')
plt.subplot(1,3,2)
plt.imshow(rgb_img)
plt.title('红蓝反转图')
plt.subplot(1,3,3)
plt.imshow(gray_img,cmap='gray')
plt.title('灰度图像')
plt.show()

# %%
sp_noise_img=random_noise(rgb_img,mode='s&p',amount=0.4)
gau_noise_img=random_noise(rgb_img,mode='gaussian',mean=0.2,var=0.03)
plt.subplot(1,3,1)
plt.imshow(rgb_img)
plt.title('红蓝反转图')
plt.subplot(1,3,2)
plt.imshow(sp_noise_img)
plt.title('椒盐噪点图')
plt.subplot(1,3,3)
plt.imshow(gau_noise_img)
plt.title('高斯噪点图')
plt.show()

# %%
mean_sp=cv2.blur(sp_noise_img,(5,5))
mean_gau=cv2.blur(gau_noise_img,(5,5))

mid_sp=cv2.medianBlur((sp_noise_img*255).astype(np.uint8),5)
mid_gau=cv2.medianBlur((gau_noise_img*255).astype(np.uint8),5)

gau_sp=cv2.GaussianBlur((sp_noise_img*255).astype(np.uint8),(5,5),0)
gau_gau=cv2.GaussianBlur((gau_noise_img*255).astype(np.uint8),(5,5),0)

plt.subplot(2,3,1)
plt.imshow(mean_sp)
plt.title('均值滤波的椒盐噪点图')
plt.subplot(2,3,2)
plt.imshow(mid_sp)
plt.title('中值滤波的椒盐噪点图')
plt.subplot(2,3,3)
plt.imshow(gau_sp)
plt.title('高斯滤波的椒盐噪点图')
plt.subplot(2,3,4)
plt.imshow(mean_gau)
plt.title('均值滤波的高斯噪点图')
plt.subplot(2,3,5)
plt.imshow(mid_gau)
plt.title('中值滤波的高斯滤波图')
plt.subplot(2,3,6)
plt.imshow(gau_gau)
plt.title('高斯滤波的高斯噪点图')
plt.show()

# %%
