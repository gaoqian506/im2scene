
from data import Data
from model import Model
from env import Env



def train():

    # init Data
    data = Data('data/image/box.jpg')
    # init model
    model = Model()
    # init env
    env = Env()

    for episode in range(2):

        print("new episode begins...")
        # load image
        image = data.load_image()

        while True:
            # model.step
            action = model.step(image)
            # env.eval
            reverd = env.evaluate(action)
            # model.learn
            model.learn(reverd)

            if env.done():
                print("have down")
                break

    return


if __name__ == '__main__':
    # if -train
    train()

