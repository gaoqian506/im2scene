


from scene import Scene


class Builder:
	def __init__(self):
		self.scene = Scene()
		return

	def step(self, snapshots):
		self.object = self.scene.next_object()
		action = object.tend(snapshots)
		self.scene.perform(action)
		return

	def learn(self, reverd):
		self.object.learn(reverd)
		return



