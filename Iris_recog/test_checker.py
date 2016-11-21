import unittest
import os
from hamming import *

class Test_check(unittest.TestCase):
	def test_check1(self):
		for path,subd,files in os.walk('Test_Images'):
			if len(files) > 0:
				for i in files:
					for j in files:
						if i != j:
							verify = same_person_eyes(str(path)+'/'+str(i),str(path)+'/'+str(j))
							print(verify)
	
	
							self.assertEqual(verify,True)
	def test_check2(self):
		for path1,subd1,files1 in os.walk('Test_Images'):
			for path2,subd2,files2 in os.walk('Test_Images'):
				if path1 != path2 and len(files1) > 0 and len(files2) > 0:
					for i in files1:
						for j in files2:
							verify = same_person_eyes(str(path1)+'/'+str(i), str(path2)+'/'+str(j))
							print(verify)
							self.assertEqual(verify,False)
							
							
if __name__ == '__main__':
	unittest.main()
