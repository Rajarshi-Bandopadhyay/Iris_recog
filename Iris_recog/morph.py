from numpy import zeros

def erode(img, size=3):
	pad = int(size/2)
	gmi = zeros([img.shape[0]-2*pad,img.shape[1]-2*pad])
	for i in range(gmi.shape[0]):
		for j in range(gmi.shape[1]):
			result = True
			for u in range(-pad,pad+1):
				for v in range(-pad,pad+1):
					if img[i+u+pad,j+v+pad] == 0: result = False
			gmi[i,j] = int(result)
	return gmi

def dilate(img, size=3):
	pad = int(size/2)
	gmi = zeros([img.shape[0]-2*pad,img.shape[1]-2*pad])
	for i in range(gmi.shape[0]):
		for j in range(gmi.shape[1]):
			result = False
			for u in range(-pad,pad+1):
				for v in range(-pad,pad+1):
					if img[i+u+pad,j+v+pad] == 1: result = True
			gmi[i,j] = int(result)
	return gmi
