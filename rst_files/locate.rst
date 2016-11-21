Locate
======

This python module is for creating detecting the center of the iris cum pupil and detects the outer radius of the iris and the radius of the iris. This module contain only one function named locate().

locate
------
	Give the center in 2D coordinate of the iris cum 
        pupil and and the radius of the pupil and the outer
        radius of the iris.

        **Parameters**
        
        fname: string
             The name of the image file in string format.

        **Returns**
        
        A list with three elements. 
        First element is the radius of the pupil.
        Second element is the outer radius of the iris.
        Third element is a tuple which contains x_coordiante a
        and y_coordinate of the center respectively. All of the values are
	in floats.
