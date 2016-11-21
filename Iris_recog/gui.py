from tkinter import *
import os
from hamming import *
import shutil

root = Tk()

Label(root, text='Do you want to insert or check? ').grid(row=0, column=0, columnspan=2)
operation = IntVar()
Radiobutton(root, text = "Insert new", padx = 20, variable = operation, value = 0).grid(row=1, column=0)
Radiobutton(root, text = "Check", padx = 20, variable = operation, value =1).grid(row=2, column=0)

Label(root, text='Please enter the name of the owner of this eye: ').grid(row=3, column=0)
person = StringVar()
Entry(root, textvariable=person).grid(row=4, column=0, columnspan=2)

Label(root, text = "Please specify which eye:").grid(row=5,column=0)
eye = IntVar()
Radiobutton(root, text = "right", padx = 20, variable = eye, value = 1).grid(row=7, column=0)
Radiobutton(root, text = "left", padx = 20, variable = eye, value =0).grid(row=6, column=0)

Label(root, text='Please enter the path of the image file: ').grid(row=8, column=0)
image = StringVar()
Entry(root, textvariable=image).grid(row=9, column=0, columnspan=2)

def proceed():
	owner = person.get()
	if eye.get() == 0: lr = 'left'
	if eye.get() == 1: lr = 'right'
	if operation.get() == 0:
		if not os.path.exists('Input_database/'+owner+'/'+lr+'.bmp'):
			if not os.path.exists('Input_database/'+owner):
				os.makedirs('Input_database/'+owner)
			shutil.copy(image,'Input_database/'+owner+'/'+lr+'.bmp')
		else:
			print('Image is already inserted')
	
	if operation.get() == 1:
		if os.path.exists('Input_database/'+owner+'/'+lr+'.bmp'):
			verify = same_person_eyes('Input_database/'+owner+'/'+lr+'.bmp',image.get())
			if verify == True:
				print('Verified. The images belong to the same eye.')
			else:
				print('Not verified. The images are of two different eyes.')
		else:
			print('You have not entered your eye image. Please enter earlier')

Button(root, text="Proceed", command=proceed).grid(row=10, column=0)

root.mainloop()
