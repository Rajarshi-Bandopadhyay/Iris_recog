Iris
====

This module detects the iris region from an eye image and contains only one function iris_detect().

iris_detect
-----------
This function marks the iris region for an eye image by simple thresholding technique. The pixels which contain the red,green,blue values greater than 30 and less than 120 are marked as pixels corresponding to iris.

    **Parameters**
    
    fname: string
        Name of the image given in string format.

    **Returns**
    
    pupil: 
        A new binary image in which the the iris is marked
        as object(white) and the rest of the region is marked 
        background(black).
