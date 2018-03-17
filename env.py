
class Env:
    def __init__(self):
        self.counter = 0
        return

    def evaluate(self, action):
        self.counter += 1
        return

    def done(self):
        return self.counter % 5 == 0
