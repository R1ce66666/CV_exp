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
创建MLP网络实例并且创建 SGD 优化器
<img width="496" height="89" alt="image" src="https://github.com/user-attachments/assets/f6d03bd3-3570-446b-88d5-a202985924ce" />
### 5.训练和测试模型
训练：将模型切换为 train() 模式；逐个 batch 取数据，把图片拉平成 784 维并送入设备，依次执行 zero_grad、前向传播、cross_entropy、backward、step。</br>
测试：将模型切换为 eval() 模式；在 torch.no_grad() 下跑完整个测试集，累计损失和正确数，据此算出平均损失 test_loss 和准确率 acc。</br>
用 print 输出本轮结果，并把 test_loss、acc 分别追加到 test_loss_list、acc_list，供后面画曲线。</br>
<img width="620" height="490" alt="image" src="https://github.com/user-attachments/assets/3a77836e-a9e0-407d-b87a-27804e53b17e" />
输出：
<img width="307" height="218" alt="image" src="https://github.com/user-attachments/assets/c6319fb8-afa2-41bd-9634-76d323ebf19d" />




