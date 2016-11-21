Pupil
=====

This module detects the pupil region from an eye image and contains only one function pupil_detect().

pupil_detect
------------
This function marks the pupil region for an eye image by simple thresholding technique. The pixels which contain the red,green,blue values are less than 30 are marked as pixels corresponding to pupil.

    **Parameters**
    
    fname: string
        Name of the image given in string format.

    **Returns**
    
    pupil: 
        A new binary image in which the the pupil is marked
        as object(white) and the rest of the region is marked 
        background(black).
