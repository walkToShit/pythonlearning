import torch.nn  as nn
##import torch. nn.functional as F
import torch
from matplotlib import pyplot as plt
import os, sys
from common_tools import set_seed, transform_invert
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from PIL import Image
import numpy as np

set_seed(1)  # 设置随机种子
n_hidden = 200
max_iter = 2000
disp_interval = 200
lr_init = 0.01


class RMBDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        """
rmb面额分类任务的Dataset
: param data_dir: str,数据集所在路径
: param transform: torch.transform，数据预处理"""
        self.label_name = {"1": 0, "100": 1}
        self.data_info = self.get_img_info(data_dir)  # data_info存储所有图片路径和标签，
        # 在DataLoader中通过index读取样本
        self.transform = transform

    def __getitem__(self, index):
        path_img, label = self.data_info[index]
        img = Image.open(path_img).convert('RGB')  # 0 ~255
        if self.transform is not None:
            img = self.transform(img)  # 在这里做transform，转为tensor等等
        return img, label

    def __len__(self):
        return len(self.data_info)

    @staticmethod
    def get_img_info(data_dir):
        data_info = list()
        for root, dirs, _ in os.walk(data_dir):
            # 遍历类别
            for sub_dir in dirs:
                img_names = os.listdir(os.path.join(root, sub_dir))
                img_names = list(filter(lambda x: x.endswith('.jpg'), img_names))
                # 遍历图片
                for i in range(len(img_names)):
                    img_name = img_names[i]
                    path_img = os.path.join(root, sub_dir, img_name)
                    label = rmb_label[sub_dir]
                    data_info.append((path_img, int(label)))
        return data_info


class LeNet_bn(nn.Module):
    def __init__(self, classes):
        super(LeNet_bn, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.bn1 = nn.BatchNorm2d(num_features=6)

        self.conv2 = nn.Conv2d(6, 16, 5)
        self.bn2 = nn.BatchNorm2d(num_features=16)

        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.bn3 = nn.BatchNorm1d(num_features=120)  # _lin 此处是1D

        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, classes)

    def forward(self, x):
        out = self.conv1(x)
        out = self.bn1(out)
        out = nn.functional.relu(out)

        out = nn.functional.max_pool2d(out, 2)

        out = self.conv2(out)
        out = self.bn2(out)
        out = nn.functional.relu(out)

        out = nn.functional.max_pool2d(out, 2)

        out = out.view(out.size(0), -1)

        out = self.fc1(out)
        out = self.bn3(out)
        out = nn.functional.relu(out)

        out = nn.functional.relu(self.fc2(out))
        out = self.fc3(out)
        return out

    def initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.xavier_normal_(m.weight.data)
                if m.bias is not None:
                    m.bias.data.zero_()
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight.data, 0, 1)
                m.bias.data.zero_()


set_seed()  # 设置随机种子
rmb_label = {"1": 0, "100": 1}
# 参数设置
MAX_EPOCH = 30
BATCH_SIZE = 15
LR = 0.01
log_interval = 10
val_interval = 1

# =====================================step 1/5数据=========================================
dir = os.path.abspath("D:\\saveFile\\allDevWorkspace\\dataSet\\RMB")
split_dir = os.path.abspath(os.path.join(dir, "rmb_split"))
print(split_dir)
if not os.path.exists(split_dir):
    raise Exception(r"数据}不存在，回到lesson-06\l_split_dataset. py生成数据".format(split_dir))
train_dir = os.path.join(split_dir, "train")
valid_dir = os.path.join(split_dir, "valid")
norm_mean = [0.485, 0.456, 0.406]
norm_std = [0.229, 0.224, 0.225]

train_transform = transforms.Compose([transforms.Resize((32, 32))
                                         , transforms.RandomCrop(32, padding=4)
                                         , transforms.RandomGrayscale(p=0.8)
                                         , transforms.ToTensor()
                                         , transforms.Normalize(norm_mean, norm_std), ])
valid_transform = transforms.Compose([transforms.Resize((32, 32))
                                         , transforms.ToTensor()
                                         , transforms.Normalize(norm_mean, norm_std), ])

# 构建MyDataset实例
train_data = RMBDataset(data_dir=train_dir, transform=train_transform)
valid_data = RMBDataset(data_dir=valid_dir, transform=valid_transform)
# 构建DataLoder
train_loader = DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)
valid_loader = DataLoader(dataset=valid_data, batch_size=BATCH_SIZE)
# batch_size (int, optional): how many samples per batch to load

# ==========================step 2/5模型=============================
# net = LeNet(classes=2)     #_lin 验证三种情况 1）只有lenet 2) lenet下初始化权重 3） 只有lenet_bn
net = LeNet_bn(classes=2)
# net.initialize_weights ()


# =============================== step 3/5损失函数============================;
criterion = nn.CrossEntropyLoss()  # 选择损失函数
# =============================== step 4/5优化器=======================================
optimizer = torch.optim.SGD(net.parameters(), lr=LR, momentum=0.9)  # 选择优化器
# optimizer = torch.optim.Adam(net.parameters(),lr=LR)  #选择优化器  Adam 本身已经优化学习率，但是还可继续设置学习率下降策略
# optimizer = torch.optim.RMSprop(net.parameters(),lr=LR)
# optimizer = torch.optim.Adagrad(net.parameters(),lr=LR)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)  # 设置学习率下降策略

# ============================step 5/5训练===============================================
train_curve = list()
valid_curve = list()

iter_count = 0
# 构建SummaryWriter
writer = SummaryWriter(comment='test_your_comment', filename_suffix="_test_your_filename_suffix")

for epoch in range(MAX_EPOCH):
    loss_mean = 0.
    correct = 0.
    total = 0.

    net.train()  # _lin 表示要训练 会把所有的梯度打开
    for i, data in enumerate(train_loader):
        iter_count += 1
        # forward
        inputs, labels = data
        outputs = net(inputs)
        # backward
        optimizer.zero_grad()
        loss = criterion(outputs, labels)
        print(loss)
        loss.backward()
        # update weights
        optimizer.step()
        # 统计分类情况
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).squeeze().sum().numpy()
        # 打印训练信息
        loss_mean += loss.item()
        train_curve.append(loss.item())
        if (i + 1) % log_interval == 0:
            loss_mean = loss_mean / log_interval
            print("Training:Epoch[{:0>3}/{:0>3}] Iteration[{:0>3}/{:0>3}] Loss: {:.4f} Acc: {:.2%} ".format(
                epoch, MAX_EPOCH, i + 1, len(train_loader), loss_mean, correct / total))
            loss_mean = 0.
        # 记录数据，保存于event file
        writer.add_scalars("Loss", {"Train": loss.item()}, iter_count)
        writer.add_scalars("Accuracy", {"Train": correct / total}, iter_count)
    # 每个epoch，记录梯度，权值
    for name, param in net.named_parameters():
        writer.add_histogram(name + '_grad', param.grad, epoch)
        writer.add_histogram(name + '_data', param, epoch)

    scheduler.step()  # 更新学习率
    # validate the model
    if (epoch + 1) % val_interval == 0:
        correct_val = 0.
        total_val = 0.
        loss_val = 0.
        net.eval()  # _lin 表示要验证操作， 不会回传梯度等
        with torch.no_grad():  # _lin 验证集 是验证用的不是训练模型用的 所以不用回传梯度，用no_grad()
            for j, data in enumerate(valid_loader):
                inputs, labels = data
                outputs = net(inputs)
                loss = criterion(outputs, labels)
                _, predicted = torch.max(outputs.data, 1)
                total_val += labels.size(0)
                correct_val += (predicted == labels).squeeze().sum().numpy()
                loss_val += loss.item()
            loss_mean_epoch = loss_val / len(valid_loader)  # 计算一个epoch的loss均值
            valid_curve.append(loss_mean_epoch)  # 记录每个epoch的loss
            print("Valid: \t Epoch[{:0>3}/{:0>3}] Iteration[{:0>3}/{:0>3}] Loss: {:.4f} Acc: {:.2%} ".format(
                epoch, MAX_EPOCH, j + 1, len(valid_loader), loss_mean_epoch, correct_val / total_val))
            # 记录数据，保存于event file
            writer.add_scalars("Loss", {"Valid": loss_mean_epoch}, iter_count)
            writer.add_scalars("Accuracy", {"Valid": correct_val / total_val}, iter_count)
train_x = range(len(train_curve))
train_y = train_curve

train_iters = len(train_loader)
valid_x = np.arange(1, len(valid_curve) + 1) * train_iters * val_interval  # 由于valid中记录的是epoch loss，需要
valid_y = valid_curve
plt.plot(train_x, train_y, label='Train')
plt.plot(valid_x, valid_y, label='Valid')
plt.legend(loc='upper right')
plt.ylabel('loss value')
plt.xlabel('Iteration')
plt.show()
