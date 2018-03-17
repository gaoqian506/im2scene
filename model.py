
import torch
import torchvision



class Model:
    def __init__(self):
        # self.net = torchvision.models.resnet18()
        self.net1 = torch.nn.Sequential(
            torch.nn.Conv2d(3, 10, 3, padding=1),   # input: 3x200x200 3x400x600
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            torch.nn.Conv2d(10, 15, 3, padding=1),  # input:10x100x100 10x200x300
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            torch.nn.Conv2d(15, 20, 3, padding=1),  # input:15x50x50 15x100x150
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            torch.nn.Conv2d(20, 25, 3, padding=1),  # input:20x25x25 20x50x75
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            torch.nn.Conv2d(25, 30, 3, padding=1),  # input:25x12x12 25x25x37
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2)     # output:30x12x18
        )
        self.net2 = torch.nn.Sequential(
            torch.nn.Dropout(),
            torch.nn.Linear(30*12*18, 1024),
            torch.nn.ReLU(),
            torch.nn.Dropout(),
            torch.nn.Linear(1024, 512),
            torch.nn.ReLU(),
            torch.nn.Dropout(),
            torch.nn.Linear(512, 256),
            torch.nn.ReLU(),
            torch.nn.Dropout(),
            torch.nn.Linear(256, 128),
            torch.nn.ReLU(),
            torch.nn.Dropout(),
            torch.nn.Linear(128, 64),
        )
        print 'net1:', self.net1
        print 'net2:', self.net2
        return

    def step(self, x):
        print('input:', x.data.size())
        x = self.net1(x)
        print('conved:', x.data.size())
        x = x.view(x.size(0), -1)
        print('viewed:', x.data.size())
        x = self.net2(x)
        print('output:', x.data.size())
        return x
        # return

    def learn(self, reverd):
        pass
