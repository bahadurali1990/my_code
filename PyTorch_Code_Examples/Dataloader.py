import numpy as np
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




