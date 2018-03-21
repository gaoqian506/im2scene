

from lib.player import Player
from lib.environment import Environment



def train():

    env = Environment()
    player = Player()

    for episode in range(2):
        env.start()

        while True:
            actions = player.act(env.state)
            reverd = env.apply(actions)
            player.learn(reverd)
            if env.done:
                break
    return


if __name__ == '__main__':
    # if -train
    train()

    # else
    # test()

