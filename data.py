
import cv2
import numpy as np

class Data:
    def __init__(self, path):
        self.path = path

    def load_image(self):
        return cv2.imread(self.path).astype(np.float32)/255.0
