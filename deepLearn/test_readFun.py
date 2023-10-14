import torch.nn as nn

import torch

from collections import OrderedDict
import random
import numpy as np
import os
from PIL import Image
from torchvision import transforms
from common_tools import set_seed, transform_invert
from matplotlib import pyplot as plt

from torch.utils.tensorboard import SummaryWriter

from torch.utils.data import Dataset
from torch.utils.data import DataLoader

import torchvision.utils as vutils


LR= 0.1
iteration = 10
max_epoch = 200
weights = torch. randn((1),requires_grad=True)
target = torch.zeros ((1))
gamma =0.95

print("---------自定义调整策略--所以两个策略则有两个返回值------------------------")
lr_init = 0.1
weights_1 = torch.randn ((6,3,5,5))
weights_2 = torch.ones ((5,5))
optimizer = torch.optim.SGD([{'params': [weights_1]},{'params': [weights_2]}],lr=lr_init)
#optimizer = torch.optim.SGD([[weights_1],[weights_2]],lr=lr_init)  #_lin 这种写法是不行的
#params (iterable): iterable of parameters to optimize or dicts defining parameter groups
# 多个参数 只能用字典的形式
lambda1 = lambda epoch: 0.1**(epoch // 20) #_lin 整除
lambda2 = lambda epoch: 0.95**epoch

scheduler_lr = torch.optim.lr_scheduler. LambdaLR(optimizer,lr_lambda=[lambda1,lambda2])
lr_list,epoch_list = list(), list()
for epoch in range (max_epoch):
    lr_list.append(scheduler_lr.get_last_lr())
    epoch_list.append(epoch)
    for i in range(iteration):
        loss = torch. pow ((weights - target),2)
        loss. backward()
        optimizer. step()
        optimizer.zero_grad()
    scheduler_lr.step()
plt.plot(epoch_list,lr_list,label="Exponential LR Scheduler\ngamma:{}".format(gamma))
plt.xlabel("Epoch")
plt.ylabel ("Learning rate")
plt.legend()
plt.show()
print(lr_list)