import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

transform = transforms.Compose([ transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,)) ])


train_dataset = datasets.MNIST(root="/Users/ahad/",download=True,train=True,transform=transform)
test_dataset = datasets.MNIST(root="/Users/ahad/",download=True,train=False,transform=transform)


print(train_dataset.data.shape)
print(train_dataset.targets.shape)


print(test_dataset.data.shape)
print(test_dataset.targets.shape)



train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)


class SimpleNN(nn.Module):
    def __init__(self):

        super(SimpleNN,self).__init__()

        self.fc1 = nn.Linear(in_features=(28*28),out_features=128)

        self.fc2 = nn.Linear(in_features=128,out_features=64)

        self.fc3 = nn.Linear(in_features=64,out_features=10)

    def forward(self,x):

        x = x.view(-1,28*28)

        x = torch.relu(self.fc1(x))

        x = torch.relu(self.fc2(x))

        x = self.fc3(x)

        return x

model = SimpleNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(),lr=0.001)


epochs = 5
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        optimizer.zero_grad()
        # reset gradients
        outputs = model(images)

        # forward pass

        loss = criterion(outputs, labels)
        # compute loss loss.backward()

        # backpropagation

        optimizer.step()
        # update weights

        running_loss += loss.item()

        print(f"Epoch {epoch+1}, Loss: {running_loss/len(train_loader):.4f}")










