
from lib.model import CreatorModel
from lib.config import Config
from lib.renderer import Renderer
from lib.scene import Scene
import torch

if __name__ == '__main__':

    test_model = False
    test_renderer = True

    if test_model:
        model = CreatorModel()
        height = Config.ImageHeight
        width = Config.ImageWidth
        channels = (1+Config.SnapshotCount)*3
        state = torch.autograd.Variable(torch.rand(1, channels, height, width))
        print(state.data.size())
        output = model.forward(state)
        print(output.data.size())

    if test_renderer:
        renderer = Renderer()
        scene = Scene()

        renderer.render(scene)




