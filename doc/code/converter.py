


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
		scene = self.builder.get_scene()		
		earlier = self.renderer.render(scene_1)		

		while Ture:

			maks = self.builder.step(earlier)
			later = self.renderer.render(scene)
			reverd = self.reviewer.review(image, earlier, later, mask)
			self.builder.learn(reverd)
			later = earlier

			if self.reviewer.done:
				break






