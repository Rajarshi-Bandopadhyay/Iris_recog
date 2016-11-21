from numpy import zeros
from skimage.io import imread,imshow,show
from skimage.color import rgb2grey

import unittest

from imseg import segment

class TestSegment(unittest.TestCase):
     def test_case1(self):
         img1 = rgb2grey(imread('test1.png'))
         i = segment(img1)
         self.assertEqual(len(i[1]),5)
     def test_case2(self):
         img2 = rgb2grey(imread('test2.png'))
         i = segment(img2)
         self.assertEqual(len(i[1]),3)
     def test_case3(self):
         img3 = rgb2grey(imread('test3.png'))
         i = segment(img3)
         self.assertEqual(len(i[1]),2)
     def test_case4(self):
         img4 = rgb2grey(imread('test4.png'))
         i = segment(img4)
         self.assertEqual(len(i[1]),1)
         
         
if __name__ == '__main__':
     unittest.main()
