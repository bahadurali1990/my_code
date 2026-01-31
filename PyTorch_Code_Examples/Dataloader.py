"""import numpy as np
import torch

from torch.utils.data import dataset
from torch.utils.data import dataloader

class TensorCustomData(dataset):

    def __init__(self,features,labels):

        self.features = torch.from_numpy(features).float()
        self.labels = torch.from_numpy(labels).float()
        self.n_samples = self.features.shape[0]

    def __getitem__(self, index):

        return self.features[index],self.labels[index]

    def __len__(self):

        return self.n_samples
"""
##-----------------------------------Examples of some In-build datasets-------------------------------------
import torch
import matplotlib.pyplot as plt
from torchvision.datasets import Caltech101
from torchvision import transforms
from torch.utils.data import DataLoader
from torch.utils.data import random_split

transform = transforms.Compose([transforms.Resize((224,224)),transforms.ToTensor(),transforms.Normalize((0.5,), (0.5,))])

datasets  = Caltech101(root='/Users/ahad/MNIST/Image_dataset1',transform=transform)

train_size =  int(0.8*len(datasets))
test_size  =  int(len(datasets)-train_size)

train_datasets , test_datasets = random_split(datasets,[train_size,test_size])

train_loader = DataLoader(train_datasets,shuffle=True,batch_size=32)
test_loader  = DataLoader(test_datasets,shuffle=True,batch_size=32)




















