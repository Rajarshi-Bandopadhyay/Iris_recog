from skimage.io import imread
from skimage.color import rgb2grey
from skimage.filters import canny
from matplotlib.pyplot import figure, show
from sys import argv

if len(argv) < 2:
	print('No image file provided as argument.')
	exit()
fname = argv[1]

img = rgb2grey(imread(fname))
edge = canny(img)

fig = figure()
ii = fig.add_subplot(121)
oi = fig.add_subplot(122)

ii.imshow(img, cmap="Greys_r")
oi.imshow(edge, cmap="Greys_r")
show()
