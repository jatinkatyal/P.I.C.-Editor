""" Filters """
def mars(img):
	print("Sending rocket to mars.")
	img[:,:,1] = img[:,:,2] = 0
	return img

def night_vision(img):
	print("Wearing Night Vision glasses.")
	img[:,:,0] = img[:,:,2] = 0	 
	return img
def night(img):
	print("Turning lights off.")
	img[:,:,0] = img[:,:,1] = 0
	return img
def aquamarine(img):
	print(" Applying Aquamarine effect.")
	img[:,:,0]=0
	return img	
def magenta(img):
	print("Turning everything purple.")
	img[:,:,1]=0
	return img
def pale(img):
	print("Turning everything yellow.")
	img[:,:,2]=0
	return img
def wnb(img):
	print("Going back in time.")
	import numpy
	for i in numpy.arange(img.shape[0]):
		for j in numpy.arange(img.shape[1]):
			if(img[i][j][0] > 0.72*img[i][j][1] and  img[i][j][0] > img[i][j][2]):
				max = img[i][j][0]
			elif(img[i][j][1]>img[i][j][2]):
				max=img[i][j][1]
			else:
				max =img[i][j][2]
			img[i][j][0]= img[i][j][1]= img[i][j][2]=max
	return img
def bnw(img):
	print("Going back in time.")
	import numpy
	for i in numpy.arange(img.shape[0]):
		for j in numpy.arange(img.shape[1]):
			if(img[i][j][0] < 0.72*img[i][j][1] and  img[i][j][0] < img[i][j][2]):
				min = img[i][j][0]
			elif(img[i][j][1]<img[i][j][2]):
				min=img[i][j][1]
			else:
				min =img[i][j][2]
			img[i][j][0]= img[i][j][1]= img[i][j][2]=min
	return img