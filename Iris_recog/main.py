import os
import shutil
from hamming import *

operation = str(input('Operation: Insert or check: ')).lower()
person = str(input('Person name: ')).lower()
eye = str(input('Left eye or right eye: ')).lower()
image = str(input('Insert the image: '))

if operation == 'insert':
	if not os.path.exists('Input_database/'+person+'/'+eye+'.bmp'):
		if not os.path.exists('Input_database/'+person):
			os.makedirs('Input_database/'+person)
		shutil.copy(image,'Input_database/'+person+'/'+eye+'.bmp')
	else:
		print('Image is already inserted')
		
		
if operation == 'check':
	if os.path.exists('Input_database/'+person+'/'+eye+'.bmp'):
		verify = same_person_eyes('Input_database/'+person+'/'+eye+'.bmp',image)
		if verify == True:
			print('Verified. The images belong to the same eye.')
		else:
			print('Not verified. The images are of two different eyes.')
	else:
		print('You have not entered your eye image. Please enter earlier')

