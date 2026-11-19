# 实验五：卷积神经网络
202410315009 人工智能241 孙昭
## 一、实验目的
本实验是基于LeNet的卷积神经网络实验，通过训练MNIST手写数字分类模型并结合可视化，旨在通过构建卷积神经网络，掌握卷积层、池化层和全连接层在图像分类中的作用，理解卷积与池化对图像特征的提取过程。
## 二、实验内容
### 1.导入依赖库
torch库：pytorch的核心基础库，负责张量的定义与运算，提供自动微分功能，支持GPU加速计算。</br>
torch.nn库：pytorch的神经网络模块库，封装各类带可学习参数的网络层，用于搭建网络结构。</br>
torch.nn.functional库：神经网络函数式接口库，提供无参数的运算函数，一般在前向传播中调用。</br>
torch.optim库：优化器库，提供多种参数更新算法，在反向传播后更新网络权重。</br>
torchvision库：pytorch配套的计算机视觉工具库，datasets用于加载公开数据集，transforms用于图像预处理。</br>
matplotlib.pyplot库：绘图可视化库，用于绘制图像、特征图以及损失和准确率曲线。</br>
<img width="404" height="144" alt="image" src="https://github.com/user-attachments/assets/83df17f6-349c-4c83-84a1-4f6a6e97265d" />

### 2.导入MNIST数据集
先设置超参数batch_size为512，然后判断有无GPU加速，若有则GPU加速，若无，则CPU加速。</br>
然后通过 torchvision 的 MNIST 类加载手写数字数据集，再通过 transforms.Compose 封装 ToTensor 操作，将图片转为张量格式，最后送入 DataLoader，按设定的 batch_size 划分批次，shuffle=True 让数据在读取时随机打乱，分别生成训练集加载器 trainloader 和测试集加载器 testloader。</br>
<img width="862" height="146" alt="image" src="https://github.com/user-attachments/assets/4eea6c81-41c5-4c9c-bae1-484d7d3469d5" />

### 3.创建卷积神经网络类
该卷积神经网络的层次结构如下所示：</br>
conv1：二维卷积层，输入通道 1，输出通道 6，卷积核大小 5×5，padding=2，步长默认 1；之后经过 sigmoid 激活，再进行 2×2、步长为 2 的平均池化。</br>
conv2：二维卷积层，输入通道 6，输出通道 16，卷积核大小 5×5，无 padding，步长默认 1；之后经过 sigmoid 激活，再进行 2×2、步长为 2 的平均池化。</br>
flatten：从第 1 维开始展平，把二维特征图转为一维向量，维度变为 5×5×16。</br>
fc1：全连接层，输入维度 5×5×16，输出维度 120，后接 sigmoid 激活。</br>
fc2：全连接层，输入维度 120，输出维度 84，后接 sigmoid 激活。</br>
clf：分类全连接层，输入维度 84，输出维度 10，不额外接激活，用于后续交叉熵损失计算。</br>

<img width="420" height="521" alt="image" src="https://github.com/user-attachments/assets/41067f86-f7f0-4c69-aecd-ca412c2463fe" />

### 4.模型实例化
实例化卷积神经网络，并选择Adam优化器进行优化设</br>
<img width="466" height="83" alt="image" src="https://github.com/user-attachments/assets/b13fd1ed-7011-4bf5-8d25-a913387a6e55" />

### 5.训练与测试
设置总共训练 30 轮，用两个列表保存每轮的测试准确率和测试损失。外层循环遍历每一个 epoch，内层循环读取训练集的批次数据，先把图像和标签迁移到指定设备，清空上一轮的梯度，送入模型得到预测结果，利用交叉熵函数计算损失，通过反向传播计算梯度，再由优化器更新模型参数。训练完成后进入测试阶段，torch.no_grad()关闭梯度计算以节省资源，循环读取测试集数据送入模型推理，累加测试损失并统计预测正确的样本数量，最后计算该轮在测试集上的平均损失与准确率，将指标存入列表并打印输出。</br>
<img width="589" height="485" alt="image" src="https://github.com/user-attachments/assets/80d78c0b-6e48-43c1-a5b4-51fb6cbf8855" />
<p>输出：</p>
<img width="299" height="621" alt="image" src="https://github.com/user-attachments/assets/1076c541-ea56-415a-93f5-6a03c2cfd515" />

### 6.可视化卷积特征图
首先取出输入图像，单独前向经过 conv1、conv2 卷积层并经过 sigmoid 激活，得到两层卷积输出的特征 feature1 和 feature2。</br>
接着选取前 5 张样本，使用 detach 切断计算图、转移到 cpu 并转为 numpy 数组，方便绘图。</br>
然后创建 3 行 5 列的画布，第一行绘制原始输入图片，第二行绘制第一层卷积融合后的特征图，第三行绘制第二层卷积融合后的特征图，关闭坐标轴。</br>
最后展示图像，直观观察卷积网络提取到的图像信息。</br>
<img width="578" height="313" alt="image" src="https://github.com/user-attachments/assets/1ac6d9e8-ecf8-4634-a399-57cd61f27f21" />
<p>输出：</p>
<img width="614" height="547" alt="image" src="https://github.com/user-attachments/assets/e77b035e-b779-4edf-9321-69e5878108de" />

### 7.评价指标
#### 1）损失函数&准确率关于epoch的函数图像
<img width="314" height="275" alt="image" src="https://github.com/user-attachments/assets/f6f54fc7-4881-4724-92b9-d274e4303a2d" />
<p>输出：</p>
<img width="751" height="288" alt="image" src="https://github.com/user-attachments/assets/38c5e2d4-3db5-4205-b810-4ebae69872a1" />

#### 2）混淆矩阵
<img width="683" height="439" alt="image" src="https://github.com/user-attachments/assets/92bc6bf7-0299-4d4e-b81a-1924f2da0f73" />
<p>输出：</p>
<img width="497" height="493" alt="image" src="https://github.com/user-attachments/assets/f1af7095-70ca-44ba-a84c-70681fe8aafa" />

## 三、实验结果与分析
从损失、准确率曲线可以看出：模型在前期（前 6 个 epoch）处于学习停滞状态，损失维持在高位、准确率仅约 11%，接近随机猜测；第 7 轮之后模型快速收敛，损失急剧下降，准确率迅速攀升，后续损失缓慢降低并趋于平稳，测试准确率最终稳定在 98.8% 左右，说明模型具备很强的手写数字识别能力，收敛效果良好，没有明显过拟合。</br>
从混淆矩阵来看：大部分样本都集中在对角线位置，各类数字识别正确率很高；少量错分样本分布在非对角线，比如数字 4 容易被错判为 9、数字 5 识别精度相对偏低，是本模型主要的识别难点。整体上该 LeNet 卷积网络对 MNIST 手写数字分类任务适配性好，分类性能优秀。</br>

## 四、实验总结与心得心得
通过本次实验，我对卷积神经网络（CNN）有了更深一步的了解，明白了卷积核的工作原理，也对卷积核的各种超参数有了一定的了解，对该模型的定义、训练、测试的代码实现更加熟练。</br>
并且可以让我直观理解了卷积神经网络的工作原理。通过损失与准确率曲线，我观察到模型的收敛过程；混淆矩阵直观展现了各类数字的识别差异.</br>
