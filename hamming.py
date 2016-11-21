from feature_vec import *


def hamming_check_string(str1, str2):

    '''
    Check the Hamming distance between two strings.

    Parameters
    ----------
    str1, str2: string
        The two input strings between which the Hamming 
        distance needs to be measured.

    Returns
    -------
    hamming_dist: integer
        The Hamming distance between the two strings.
    '''
    hamming_dist = 0
    for i in range(5):
        hamming_dist += int(str1[i] != str2[i])
    return hamming_dist
    

def same_person_eyes(fname1, fname2):

    '''
    Calculate the Hamming distance between all elements 
    of same indices for two faeature vectors and sum them up.
    Based on the sum of the Hamming distance calculated it is 
    determined the two images are for the same eye or not.

    Parameters
    ----------
    fname1, fname2: string
        The filenmaes of the images in string format.

    Returns
    -------
    *True* if the sum of Hamming distances < 1500 
    (i.e. both images are for the same eye.)
    *False* if the sum of Hamming distances > 1500
    (i.e. both images are for different eyes.)

    '''
    code1 = engroup(fname1)
    code2 = engroup(fname2)
    hgroup1, vgroup1 = code1
    hgroup2, vgroup2 = code2
    hamming_dist = 0
    for row in range(13):
        # hgroup1[row] is a list of 32 members
        for col in range(32):
            hamming_dist += hamming_check_string(hgroup1[row][col], hgroup2[row][col])
    for row in range(36):
        # hgroup1[row] is a list of 9 members
        for col in range(9):
            hamming_dist += hamming_check_string(vgroup1[row][col], vgroup2[row][col])
    return (hamming_dist < 1500)

