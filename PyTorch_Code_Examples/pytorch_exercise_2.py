"""import torch
import torch.nn.functional as F

x = torch.tensor([[[1.,2.,3.,4.,5.,6.,7.,8.,9.,10.]]])

kernel = torch.tensor([[[1/3,1/3,1/3]]])

y = F.conv1d(x,kernel)

print(y)
"""

"""import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

x = torch.arange(25,dtype=torch.float).reshape(1,1,5,5)
kernel = torch.ones((1,1,3,3))/9

y = F.conv2d(x,kernel)
plt.imshow(x.squeeze())
plt.imshow(y.squeeze())
plt.show()
"""
