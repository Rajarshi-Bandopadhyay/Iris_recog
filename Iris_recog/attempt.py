# This program uses a threshold detector to detect the position of the pupil.
# The location of the pupil is stored first in a binary image, and then superimposed over the 
# original image as a test of the algorithm's accuracy.
# Some patient iteration was required to obtain the thresholds which segregate the eyeball, 
# but the eyebrows remain part of the image

import cv2
from PIL import Image
from numpy import zeros, arange
from skimage.filters import canny
from skimage.io import imshow, show
from matplotlib.pyplot import figure, show
from skimage.transform import hough_circle
from skimage.color import rgb2grey
from skimage.feature import peak_local_max, canny
import cv2 as cv
from sys import argv

if len(argv) < 2:
	print('No input file specified.')
	exit()
fname = argv[1]

img = cv2.imread(fname)

orig = zeros(img.shape)
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		for k in range(3):
			orig[i,j,k] = img[i,j,k] / 255

pos1 = zeros([img.shape[0],img.shape[1]])
im = Image.open(fname)
pix = im.load()
#cv2.imshow('detected Edge',img)

height, width = img.shape[:2]

#print(height,width)
height=height-1
width=width-1
count=0
#print(pix[width,height])
#print(pix[0,0])
for eh in range(height):
    for ew in range(width):
        r,g,b=pix[ew,eh]
        if r<=30 and g<=30 and b<=30:
            #print(eh,ew)
            cv2.circle(img,(ew,eh),1,(0,255,0),1)
            cv2.circle(pos1,(ew,eh),1,255,1)

fig = figure()
ii = fig.add_subplot(221)
dp = fig.add_subplot(222)
oi = fig.add_subplot(223)
ii.imshow(orig)
dp.imshow(pos1, cmap="Greys")
oi.imshow(img)
show()
