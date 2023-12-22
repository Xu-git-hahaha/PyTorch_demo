#coding=utf-8
import os
import torch
from torch import nn,optim
import torch.nn.functional as F
#from torch.autograd import Variable
from torchvision import datasets, transforms
import pytorch手写字体识别

CUDA = torch.cuda.is_available()
if CUDA:
    lenet = pytorch手写字体识别.LeNet().cuda()
else:
    lenet = pytorch手写字体识别.LeNet()