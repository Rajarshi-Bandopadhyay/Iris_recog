Morph
=====

This python module does some morphological operations like morphological operations like morphological erosion and morphological dilation. This contains two functions erode() and dilate()

erode
-----
Performs morphological erosion by square mask of size given by input argument.

    **Parameters**
    
    img: 2D matrix
         Input as a matrix corresponding to a particular image
    size: integer
         Positive integer which determines the size of the mask.
         If size = n means the square mask is of size n by n.
	 If size value is not specified then it the value as 3 by default.

    **Returns**
    
    gmi: 2D matrix
         Ouptput the 2D matrix corresponding to morphologically erosed image.


dilate
------
Performs morphological dilation for an image .

    **Parameters**
    
    img: 2D matrix
         Input as a matrix corresponding to a particular image
    size: integer
         Positive integer which determines the size of the mask.
         If size = n means the square mask is of size n by n.

    **Returns**
    
    gmi: 2D matrix
         Ouptput the 2D matrix corresponding to morphologically erosed image.
