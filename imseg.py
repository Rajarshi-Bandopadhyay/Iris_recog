from numpy import zeros
from skimage.io import imread, imshow, show
from skimage.color import rgb2grey

def segment(arg):
	"""
	Segments given binary image into individual regions which are numbered. Each region is an object. The function returns a 2-tuple, whose first member is a new image with every pixel set to 0 if it contains no object, and the objectnumber if there is an object.
	The second member is a dictionary, where each object's number (objects are numbered from 1) is a separate key. length of this dictionary is the number of objects in the image. The dictionary values are lists of 2-tuples containing coordinates of the pixels in the object.
	"""
	res = zeros(arg.shape)
	objlst = {}
	rows = arg.shape[0]
	cols = arg.shape[1]
	nobj = 0
	for x in range(1,rows-1):
		for y in range(1,cols-1):
			if arg[x,y] > 0:
				if arg[x+1,y] > 0 and res[x+1,y] > 0:
					res[x,y] = res[x+1,y]
					objlst[res[x,y]].append((x,y))
				elif arg[x-1,y] > 0 and res[x-1,y] > 0:
					res[x,y] = res[x-1,y]
					objlst[res[x,y]].append((x,y))
				elif arg[x,y+1] > 0 and res[x,y+1] > 0:
					res[x,y] = res[x,y+1]
					objlst[res[x,y]].append((x,y))
				elif arg[x,y-1] > 0 and res[x,y-1] > 0:
					res[x,y] = res[x,y-1]
					objlst[res[x,y]].append((x,y))
				elif arg[x-1,y+1] > 0 and res[x-1,y+1] > 0:
					res[x,y] = res[x-1,y+1]
					objlst[res[x,y]].append((x,y))
				elif arg[x+1,y+1] > 0 and res[x+1,y+1] > 0:
					res[x,y] = res[x+1,y+1]
					objlst[res[x,y]].append((x,y))
				else:
					nobj += 1
					objlst[nobj] = []
					objlst[nobj].append((x,y))
					res[x,y] = nobj
					print((x,y))
				
				# Check for accidentl
	return (res,objlst)

