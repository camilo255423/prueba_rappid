import unittest

from parse_input import *

class TestInputMethods(unittest.TestCase):
	def test_parse_update_string(self):
	    input_string='UPDATE 2 2 2 4' 
	    x,y,z,W = parse_input_update(input_string)

	    self.assertEqual(x, 2)
	    self.assertEqual(y, 2)
	    self.assertEqual(z, 2)
	    self.assertEqual(W, 4)

	def test_parse_query_string(self):
	    input_string='QUERY 1 1 1 3 3 3' 
	    x1,y1,z1,x2,y2,z2 = parse_input_query(input_string)
	    
	    self.assertEqual(z1, 1)
	    self.assertEqual(y1, 1)
	    self.assertEqual(z1, 1)
	    
	    self.assertEqual(z2, 3)
	    self.assertEqual(y2, 3)
	    self.assertEqual(z2, 3)
	    
if __name__ == '__main__':
    unittest.main()