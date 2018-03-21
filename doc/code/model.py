

import torch


class CreatorModel(torch.nn.Model)
	def __init__(self):
		super(CreatorModel, self).__init__()

		# input is a scene-state, including ref-image, shapshots
        self.conv1 = torch.nn.Conv2d(3, 6, 5)
        self.pool = torch.nn.MaxPool2d(2, 2)
        self.conv2 = torch.nn.Conv2d(6, 16, 5)
        self.fc1 = torch.nn.Linear(16 * 5 * 5, 120)
        self.fc2 = torch.nn.Linear(120, 84)
        self.fc3 = torch.nn.Linear(84, 10)

	def forward(self, state):

		x = combine(state.image, state.snapshots)

        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

	def backward(self, reverd):
		self.net.backward(reverd)    





class ModelList():
	creator_model = CreatorModel()




'''

class Model()
	def __init__(self):
		super(Model, self).__init__()
		self.net = None
		return


	def forward(self, input):
		return self.net.predict(input)
	def backward(self, reverd):
		self.net.backward(reverd)
'''