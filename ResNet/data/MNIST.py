import torch
from torch import nn
from torch.utils.data import dataloader, Dataset
from torchvision.transforms import ToTensor
from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd
class MNIST(Dataset):
    def __init__(self, file_path:str, transform=None) -> None:
        self.file_path = file_path
        self.labels = pd.read_csv(self.file_path, usecols=[0])
        self.imgs = pd.read_csv(self.file_path, usecols=list(range(1, 784)))
        
        if transform:
            self.transform = transform

    def __getitem__(self, index):
        # item = self.file[index]
        print(self.labels)
        print(self.imgs)

mnist = MNIST("data/train.csv")
mnist.__getitem__(0)