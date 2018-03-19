
import cv2
# from skimage import io
import numpy as np
import torch

from torch.autograd import Variable



class Data:
    def __init__(self, path):
        self.path = path

    def load_image(self):
        # return io.imread(self.path).astype(np.float32)/255.0
        image = cv2.imread(self.path).transpose(2, 0, 1).astype(np.float32)/255.0
        variable = Variable(torch.from_numpy(image)).unsqueeze(0)
        print(variable.data.size())
        return variable

