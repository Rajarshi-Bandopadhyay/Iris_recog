Feature_vec
===========

This python module is used for extracting the feature correspaonding to an iris of a particular eye. This python module contains only one function engroup().

engroup
-------

	Generate the feature vector correspoonding to an iris 
        by using the rectangular iris image generated from 
        rectangulate.py;
	From the normalized eye image obtained in the rectangle function
	of rectangulate.py, the algorithm proposed by Jong Gook Ko et. al.
	is used to obtain a set of feature vectors. These feature vectors
	vary slightly among different images of the same eye, but show
	wide variation among different eyes.
	
	**Parameters**
        
	fname: string
	     The name of the image in string format.

	**Returns**
	
	[Horizontal groups, Vertical groups]
	Horizontal groups: A list of sequences of feature vectors
	evaluated along the rows
	Vertical groups: A list of sequences of feature vectors 
	evaluated along the columns.
