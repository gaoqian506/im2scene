

from object import CreatorObject


class Scene:
	def __init__(self):
		self.objects.add(CreatorObject())
		return

	def next_ojbect(self):
		self.index += 1
		if self.index >= objects.count:
			self.index = 0
		return objects[self.index]



