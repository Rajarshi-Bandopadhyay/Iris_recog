import os
import shutil
from hamming import *

'''
This is the main program which takes some inputs and based
on that runs the whole system. 

Parameters
----------
operation: string
    operation = 'insert' means that we need to insert an image
    for a new person.
    Operation = 'check' means that we need to check for an input
    for a given person with the existing database.

person: string
    The name of the person for whom the iamge needs to be inserted 
    or checked.

eye: string
    eye = 'left' means that for the left eye needs to be inserted/checked.
    eye = 'right' means that for the right eye needs to be inserted.checked.

image: string
    The filename of the input image in string format.

'''     

operation = str(input('Operation: Insert or check: ')).lower()
person = str(input('Person name: ')).lower()
eye = str(input('Left eye or right eye: ')).lower()
image = str(input('Insert the image: '))

if operation == 'insert':
    if not os.path.exists('Input_database/'+person+'/'+eye+'.bmp'):
        if not os.path.exists('Input_database/'+person):
            os.makedirs('Input_database/'+person)
        shutil.copy(image, 'Input_database/'+person+'/'+eye+'.bmp')
    else:
        print('Image is already inserted')

	
if operation == 'check':
    if os.path.exists('Input_database/'+person+'/'+eye+'.bmp'):
        verify = \
        same_person_eyes('Input_database/'+person+'/'+eye+'.bmp', image)
        if verify is True:
            print('Verified. The images belong to the same eye.')
        else:
            print('Not verified. The images are of two different eyes.')
    else:
        print('You have not entered your eye image. Please enter earlier')

