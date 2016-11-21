from imworks import *
from skimage.io import imread
from skimage.draw import circle
from morph import *

def pupil_detect(fname):
	img = bnw(fname)
	
	pupil = zeros([img.shape[0],img.shape[1]])
	
	for eh in range(img.shape[0]):
	    for ew in range(img.shape[1]):
	        magnitude = img[eh,ew]
	        if magnitude <= 0.1176:
	            rr,cc = circle(eh,ew,1)
	            pupil[rr,cc] = 1
	
	pupil = erode(pupil,15)
	pupil = dilate(pupil,8)
	
	return pupil
