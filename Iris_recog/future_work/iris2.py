from imworks import *
from skimage.io import imread
from skimage.draw import circle
from morph import *

def iris_detect(fname):
	img = bnw(fname)
	
	iris = zeros([img.shape[0],img.shape[1]])
	
	for eh in range(img.shape[0]):
	    for ew in range(img.shape[1]):
	        magnitude = img[eh,ew]
	        if magnitude <= 0.4706 and magnitude > 0.1176:
	            rr,cc = circle(eh,ew,1)
	            iris[rr,cc] = 1
	
	iris = dilate(iris,15)
	iris = erode(iris,8)
	
	return iris
