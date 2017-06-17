""" These are the functions of transformation """

def crop(image,coordX,coordY):
	print("Scissors..., Ouch!")
	x=coordX
	y=coordY
	print("cutting with scissors")
	return image[x/4:-x/4,y/4:-y/4]
	
def flip(image,choice):
	import numpy
	if choice==1:
		print("I am on the roof.")
		return numpy.flipud(image)
	elif choice==2:
		print("Is that a mirror?")
		return numpy.fliplr(image)
	else: print("Invalid option")

def rotate(image,angle):
	print("Swirl!!!")
	from scipy import ndimage
	return ndimage.rotate(image, angle, reshape=False)