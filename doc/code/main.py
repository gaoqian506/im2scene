


from lib.imageloader import ImageLoader
from lib.converter import Converter



def train():

	image_loader = ImageLoader('data/images')
	converter = Converter()
	for i in range(epochs):
		image = image_loader.load_image()
		converter.learn(image)


# main -train
if __name__ == 'main':
	if '-train':
		train()