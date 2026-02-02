import torch
import torch.nn.functional as F

x = torch.tensor([[[1.,2.,3.,4.,5.,6.,7.,8.,9.,10.]]])

kernel = torch.tensor([[[1/3,1/3,1/3]]])

y = F.conv1d(x,kernel)

print(y)