# 实验四、MLP-多层感知机
202410315009 人工智能241 孙昭
## 一、实验目的
本实验旨在通过构建多层感知机（MLP, Multi-Layer Perceptron）模型，深入理解神经网络的基本组成与工作原理，掌握其在图像分类任务中的应用。
## 二、实验内容
### 1.导入头文件
Torch:PyTorch 主库，提供张量（Tensor）和自动求导</br>
nn:神经网络模块，用 nn.Linear 建全连接层、nn.Module 作模型基类、nn.GELU作激活</br>
F:函数式接口，F.relu / F.gelu / F.cross_entropy</br>
optim:优化器，optim.SGD、optim.Adam</br>
numpy:数组运算，画混淆矩阵、做统计时用</br>
plt:画图，plt.plot、plt.subplots、plt.show</br>
torchvision:视觉工具包：datasets.MNIST 下载并读取数据，transforms.ToTensor() 把 PIL 图片转成张量并归一化到 0~1</br>
%matplotlib inline:Jupyter 魔法命令，生成的图直接显示在单元格下方，不弹独立窗口
<img width="487" height="191" alt="image" src="https://github.com/user-attachments/assets/0875df07-4f81-4bda-a3dc-5fb90fc8b093" />
### 2.导入数据
导入MNIST手写数字数据集，batch_size=2048 决定每批送 2048 张图，一个 epoch 约 30 个 batch；</br>
• train_loader / test_loader 分别读 6 万张训练集和 1 万张测试集，ToTensor 把图片转成 (1,28,28)、像素缩到 0~1，shuffle 决定每轮是否打乱顺序；</br>
• test_loss_list / acc_list 是空列表，留给后面每个 epoch 记录测试损失和准确率，最后画曲线。</br>
<img width="682" height="437" alt="image" src="https://github.com/user-attachments/assets/a7604b58-3f96-4fd4-be99-c930119d0554" />
### 3.初始化MLP模型
定义这个感知机共有 101,770 个可训练参数：第一层 784×128+128=100,480 个，第二层 128×10+10=1,290 个；此外还有 128 个隐藏单元、10 个输出类别、ReLU 激活、SGD(lr=0.01)、batch 2048。</br>
<img width="386" height="246" alt="image" src="https://github.com/user-attachments/assets/33c77dad-0009-4bb0-bb1a-0a5548feab98" />
### 4.创建模型并配好优化器
创建MLP网络实例并且创建 SGD 优化器</br>
<img width="496" height="89" alt="image" src="https://github.com/user-attachments/assets/f6d03bd3-3570-446b-88d5-a202985924ce" />
### 5.训练和测试模型
训练：将模型切换为 train() 模式；逐个 batch 取数据，把图片拉平成 784 维并送入设备，依次执行 zero_grad、前向传播、cross_entropy、backward、step。</br>
测试：将模型切换为 eval() 模式；在 torch.no_grad() 下跑完整个测试集，累计损失和正确数，据此算出平均损失 test_loss 和准确率 acc。</br>
最后用 print 输出本轮结果，并把 test_loss、acc 分别追加到 test_loss_list、acc_list，供后面画曲线。</br>
<img width="620" height="490" alt="image" src="https://github.com/user-attachments/assets/3a77836e-a9e0-407d-b87a-27804e53b17e" />
<p>输出：</p>
<img alt="image" src="https://github.com/user-attachments/assets/c6319fb8-afa2-41bd-9634-76d323ebf19d" width="50%"/>

### 6.模型评价
用matplotlib绘制损失曲线和准确率曲线</br>
<img width="545" height="335" alt="image" src="https://github.com/user-attachments/assets/0903424a-6730-475f-8ec9-31c0f20f12be" />
<P>输出：</P>
<img width="939" height="327" alt="image" src="https://github.com/user-attachments/assets/2405b8d4-3ab8-41ce-a066-ed483323e3f2" />

### 7.模型优化
加深网络，多加了一个隐藏层，现在是784->512->256->10，中间两层隐藏层的激活函数改为GELU()，优化算法从SGD改为Adam。</br>
<img width="622" height="654" alt="image" src="https://github.com/user-attachments/assets/e481cc05-1389-4c11-953b-874587d60f3d" />
<img width="763" height="515" alt="image" src="https://github.com/user-attachments/assets/2b1c1808-96ad-45c4-ae56-ff62841c4c5a" />
<P>输出：</P>
<img width="467" height="524" alt="image" src="https://github.com/user-attachments/assets/103198d6-0254-4f94-8dab-d57cc8ab9d5e" />

### 8.两模型比较
先绘制前后两个模型的准确率函数在同一个子图去对比</br>
<img width="654" height="470" alt="image" src="https://github.com/user-attachments/assets/0febbae8-c450-43c6-abcb-e90474fe8728" />
<p>再绘制两个模型各自的混淆矩阵</p>
<img width="560" height="573" alt="image" src="https://github.com/user-attachments/assets/c9de50d9-d4c1-45b1-92f5-3bc1a4ba5d5a" />
<p>输出：</p>
<img width="926" height="634" alt="image" src="https://github.com/user-attachments/assets/93cb67ad-e504-4a84-a3e7-3d0c9680dfd3" />

## 三、实验结果与分析
### 1.原始模型结果：
原始模型只有三层，从784 -> 128 -> 10，选用RELU(x)激活函数和SGD优化器。原始模型在10个epoch中的测试损失与测试准确率：损失函数图loss从2.25单调下降到 1.54，准确率函数图 accuracy从27.4% 持续上升到 74.7%，两条曲线走势相反，说明模型确实在通过训练逐步变好，代码逻辑与反向传播正确。
### 2.改进模型结果：
改进模型有四层，784 -> 512 -> 256 -> 10，选用GELU(x)激活函数和Adam优化器。改进后的模型在同样 10 个 epoch 内完成收敛，测试准确率从基线的 74.65% 提升到约 97.9%，训练损失从 1.13 降到 0.08，各项指标全面优于原模型。
### 3.两模型之间对比：
在相同的数据划分、相同的 batch_size=2048 和相同的 10 个 epoch 下，原模型与改进模型的训练结果差异显著。原模型的测试损失由 2.2476 降至 1.5363、准确率由 27.35% 升至 74.65%，两条曲线在第十轮仍保持近似恒定的斜率，未出现平台期，说明其受限于 SGD 的固定步长与每轮仅 30 次的参数更新，处于欠拟合状态；改进模型采用 GELU 激活、增加一层隐藏层并将优化器换为 Adam 后，训练损失在前三个 epoch 内即由 1.13 降至 0.28，最终收敛到 0.08，测试准确率稳定在 97.9% 左右，且训练与测试曲线全程贴合，未出现过拟合。从混淆矩阵看，原模型错误分散，改进模型的对角线数值普遍高于 950，剩余错误集中于 5→3、5→6、4→9 等形近数字，表明改进带来的不仅是 23 个百分点的精度提升，更是特征区分能力的增强；而改进模型在第十轮后曲线已趋于水平，说明该结构在 MNIST 上接近上限，进一步提高精度需要转向卷积网络。</br>
混淆矩阵显示，错误不是均匀分布：数字 5 的错误最多（867 次），数字 1 的错误最少（1124 次）；5→3 有 11 次，3→5 仅 3 次，这是书写习惯造成的单向混淆；4→9 与 9→4 各 7 次，属于两类字形本身相近造成的对称混淆。

## 四、实验总结与心得
通过本次实验，我完整走了一遍用 PyTorch 训练模型的全流程：用 DataLoader 组织数据、用 nn.Module 定义网络、用交叉熵和优化器驱动训练，并在每个 epoch 结束后用测试集评估、记录曲线。最大的收获是把准确率从 74.65% 提到 97.9%，更重要的是弄懂了这两个数字背后的原因：batch_size 决定了每个 epoch 的参数更新次数，2048 的 batch 让 10 个 epoch 总共只有 300 次更新，模型其实还有学习空间，只是训练次数不足；只看准确率容易误判，要把 loss 和 acc 放在一起看。改进阶段把 ReLU 换成 GELU、加一层隐藏层、换用 Adam，我体会到三项改动各自的作用：激活函数影响梯度传播，网络深度影响模型容量，优化器影响收敛速度，三者叠加才有明显效果。同时我也认识到，MLP 在 MNIST 上约 98% 已接近上限，再想提升需要换用卷积网络。





