from skimage.io import imread, imshow, show
from skimage.color import rgb2gray

def bnw(s):
	return rgb2gray(imread(s))

def disp(img):
	imshow(img)
	show()

# Changeable:

from imseg2 import segment
from chk import chk
from superobj import superobj
img = bnw('test2.png')
res, oblst, idn = segment(img)

