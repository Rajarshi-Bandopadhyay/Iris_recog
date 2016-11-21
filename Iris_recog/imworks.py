from skimage.io import imread, imshow, show
from skimage.color import rgb2gray

def bnw(s):
	return rgb2gray(imread(s))

def disp(img):
	imshow(img)
	show()


