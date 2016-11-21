Hamming
=======

This python module is for checking the Hamming distance between two eye images. If the Hamming disatnce is too large means that the eye images are for different eyes aor different persons. If the Hamming distance is small means that the two eye images are for the same eye or the same person. This module contains two functions hamming_check_string() and same_person_eyes().


hamming_check_string
--------------------
        Check the Hamming distance between two strings.

	**Parameters**
	
	str1, str2: string
	    The two input strings between which the Hamming 
	    distance needs to be measured.

	**Returns**
	
	hamming_dist: integer
	    The Hamming distance between the two strings.


same_person_eyes
----------------
	Calculate the Hamming distance between all elements 
	of same indices for two faeature vectors and sum them up.
	Based on the sum of the Hamming distance calculated it is 
	determined the two images are for the same eye or not.

	**Parameters**

	
	fname1, fname2: string
	     The filenmaes of the images in string format.

	**Returns**
	

	*True* if the sum of Hamming distances < 1500 
	(i.e. both images are for the same eye.)

	*False* if the sum of Hamming distances > 1500
	(i.e. both images are for different eyes.)

