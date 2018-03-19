
from renderer import Renderer
from appreciator import Appreciator2D, Appreciator3D

import torch

class Env:
    def __init__(self):
        self.counter = 0
        self.renderer = Renderer()
        self.appreciator2d = Appreciator2D()
        self.appreciator3d = Appreciator3D()
        return

    def evaluate(self, image, scene):
        self.counter += 1
        reverd3d = self.appreciator3d.appreciate(scene)
        rendered = self.renderer.render(scene)
        reverd2d = self.appreciator2d.appreciate(image, rendered)
        print 'reverd:', reverd2d+reverd3d
        return reverd2d+reverd3d

    def done(self):
        return self.counter % 5 == 0
