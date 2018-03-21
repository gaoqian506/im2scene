


from model import ModelList

class Object:
	def __init__(slef):
		return



class CreatorObject(Object):
	"""docstring for ClassName"""
	def __init__(self):
		super(CreatorObject, self).__init__()
		self.model = ModelList.creator_model
		return

	def tend(self, image, snapshots):
		return self.model.predict(image, snapshots)

	def perform(self, action):
		# perform action respectively
		return
	def learn(self, reverd):
		self.model.backward(reverd)
		return
		