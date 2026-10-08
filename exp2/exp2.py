#%%
#导入依赖库
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.util import random_noise

#%%
#获取颜色通道参数
img=cv2.imread(r'C:\Users\14627\Desktop\cj.jpg')
(b,g,r)=img[500,750]
print(b,g,r)
plt.imshow(img)
plt.title('原图')
plt.savefig(r'E:\mycode\python\exp_CV\exp2/original.jpg',dpi=300)
plt.show()

#%%
#红蓝反转
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
plt.title('红蓝反转图')
plt.savefig(r'E:\mycode\python\exp_CV\exp2\rgb_image.jpg', dpi=300, bbox_inches='tight')
plt.show()

#%%
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img,cmap='gray')
plt.title('灰度图像')
plt.savefig(r'E:\mycode\python\exp_CV\exp2\gray_image.jpg', dpi=300, bbox_inches='tight')
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
plt.savefig(r'E:\mycode\python\exp_CV\exp2\noise_image.jpg', dpi=300, bbox_inches='tight')
plt.show()

# %%
#均值滤波
mean_sp=cv2.blur(sp_noise_img,(5,5))
mean_gau=cv2.blur(gau_noise_img,(5,5))
#中值滤波
mid_sp=cv2.medianBlur((sp_noise_img*255).astype(np.uint8),5)
mid_gau=cv2.medianBlur((gau_noise_img*255).astype(np.uint8),5)
#高斯滤波
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
plt.title('中值滤波的高斯噪点图')
plt.subplot(2,3,6)
plt.imshow(gau_gau)
plt.title('高斯滤波的高斯噪点图')
plt.savefig(r'E:\mycode\python\exp_CV\exp2\blur_image.jpg', dpi=300, bbox_inches='tight')
plt.show()


# %%
