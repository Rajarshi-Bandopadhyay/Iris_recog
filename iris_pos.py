from pupil import *
from iris import *
from numpy import zeros
from skimage import draw

if len(argv) < 2:
	print('No filename entered as command line argument.')
	exit()

fname = argv[1]
pupil_img = pupil_detect(fname)
rows = pupil_img.shape[0]
cols = pupil_img.shape[1]

for col in range(cols):
	col = cols - 1 - col
	if sum(pupil_img[:,col]) > 0:
		east_mark = col
		break

for col in range(east_mark):
	col = east_mark - 1 - col
	if sum(pupil_img[:,col]) == 0:
		west_mark = col
		break

for row in range(rows):
	row = rows - 1 - row
	if sum(pupil_img[row,:]) > 0:
		south_mark = row
		break

for row in range(south_mark):
	row = south_mark - 1 - row
	if sum(pupil_img[row,:]) == 0:
		north_mark = row
		break

center_x = (west_mark + east_mark) / 2
center_y = (north_mark + south_mark) / 2

lines = zeros([rows,cols])
rr, cc = draw.line(south_mark,east_mark,north_mark,east_mark)
lines[rr,cc] = 1	
rr, cc = draw.line(south_mark,west_mark,north_mark,west_mark)
lines[rr,cc] = 1
rr, cc = draw.line(south_mark,west_mark,south_mark,east_mark)
lines[rr,cc] = 1	
rr, cc = draw.line(north_mark,west_mark,north_mark,east_mark)
lines[rr,cc] = 1	
rr, cc = draw.circle(center_y,center_x,3)
lines[rr,cc] = 1

full_color = zeros([rows,cols,3])
for i in range(rows):
	for j in range(cols):
		full_color[i,j,0] = pupil_img[i,j]
		full_color[i,j,1] = lines[i,j]
disp(full_color)

iris_img = iris(fname)
disp(iris_img)
