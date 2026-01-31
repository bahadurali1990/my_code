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
import torch.nn as nn
import torch.optim as optim


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

print(f"Number of classes are {len(datasets.categories)}")

##-----------------------------------------------Define the CNN Model----------------------------------------

class ImageClass(nn.Module):

    def __init__(self,Num_of_Class=102):

        super(ImageClass,self).__init__()

        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)

        self.pool = nn.MaxPool2d(2, 2)

        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)

        self.fc1 = nn.Linear(64 * 32 * 32, 256)

        self.fc2 = nn.Linear(256, Num_of_Class)

    def forward(self,x):

        x = self.pool(torch.relu(self.conv1(x)))

        x = self.pool(torch.relu(self.conv2(x)))

        x = x.view(-1, 64 * 32 * 32)

        # flatten

        x = torch.relu(self.fc1(x))

        x = self.fc2(x)

        return x

model = ImageClass(len(datasets.categories))

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

















