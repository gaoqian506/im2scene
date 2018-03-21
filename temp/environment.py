

class Environment:
    def __init__(self):
        self.state = None
        self.done = False
        self.counter = 0
        return

    def start(self):
        return

    def apply(self, actions):
        self.counter += 1
        self.done = self.counter % 3 == 0
        return None
