



class Player:

    def __init__(self):
        return

    def act(self, state):
        x1 = image_encoder.encode(state.image)
        x2 = render_encoder.encode(state.render)
        for obj in state.objs:
            x = obj_encoder.encode(obj)
            y = decoder.decode(x1, x2, x)
            y = decoder.decode(x1, x2, )

        return None

    def learn(self, reverd):
        return
