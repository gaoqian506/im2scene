


from builder import Builder
from renderer import Renderer
from reviewer import Reviewer



class Converter:
	def __init__(self):
		self.builder = Builder()
		self.renderer = Render()
		self.reviewer = Reviewer()
		return

	def learn(self, image):
		self.builder.init()
		self.renderer.init()

		scene_1 = self.builder.get_scene()
		snapshots_1 = self.renderer.render(scene_1)

		self.builder.step(snapshots)

		scene_2 = self.builder.get_scene()
		snapshots_2 = self.renderer.render(scene_2)






