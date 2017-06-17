""" Class for image """

class Image:
	''' class to store image '''
	
	def __init__(self,path):
		import os
		from skimage import io
		self.img = io.imread(os.path.join(path))
		
	def show_img(self):						#shows self
		import matplotlib.pyplot as plt
		plt.imshow(self.img)
		plt.axis('off')
		plt.show()
		
	def show(self,image):						#shows arguement
		import matplotlib.pyplot as plt
		plt.imshow(image)
		plt.axis('off')
		plt.show()

	def get_img(self):
		import numpy
		return numpy.copy(self.img)
	
	def set_img(self,image):
		self.img=image
		
	def get_img_shape(self):
		return self.img.shape