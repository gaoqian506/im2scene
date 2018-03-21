

import torch
from lib.config import Config




class CreatorModel(torch.nn.Module):
    """
    a CreatorModel is responsible for create secene objects like box
    shpere etc..

    the input is image and shapshots of the scene

        the size and channels should be defined in cfg structure

    the output is the action of creator

    for example, create a box at the position: x, y, x


    """

    def __init__(self):
        super(CreatorModel, self).__init__()
        channels = (1 + Config.SnapshotCount) * 3
        self.encoder = torch.nn.Sequential(
            torch.nn.Conv2d(channels, 10, 3, padding=1),  # input: 3x200x200 3x400x600
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
            torch.nn.MaxPool2d(2, 2)  # output:30x12x18
        )

    def forward(self, state):
        x = self.encoder(state)
        return x


"""

        # input is a scene-state, including ref-image, shapshots
        channels = (1+Config.SnapshotCount)*3
        self.conv1 = torch.nn.Conv2d(channels, 20, 3, padding=1)
        self.pool = torch.nn.MaxPool2d(2, 2)
        self.conv2 = torch.nn.Conv2d(20, 30, 3, padding=1)
        self.fc1 = torch.nn.Linear(16 * 5 * 5, 120)
        self.fc2 = torch.nn.Linear(120, 84)
        self.fc3 = torch.nn.Linear(84, 10)
        
        x = state # combine(state.image, state.snapshots)
        x = self.pool(torch.nn.functional.relu(self.conv1(x)))
        x = self.pool(torch.nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = torch.nn.functional.relu(self.fc1(x))
        x = torch.nn.functional.relu(self.fc2(x))
        x = self.fc3(x)
        
    #     return state

	# def backward(self, reverd):
     #    pass
	# 	# self.net.backward(reverd)        
"""


