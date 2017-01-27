
from parse_input import *
from cube import *

T = int(raw_input()) 
for n_case in xrange(1,T+1):
	dimensions_input = raw_input()
	dimensions = dimensions_input.split()
	N = int(dimensions[0])
	M = int(dimensions[1])
	cube = Cube(N)

	for i in xrange(1,M+1):
		string_operation = raw_input()
		operation = string_operation.split(' ')[0]
		if operation=='UPDATE':
			x,y,z,W = parse_input_update(string_operation)
			cube.update_matrix(x,y,z,W)
		elif operation=='QUERY':
			x1,y1,z1,x2,y2,z2= parse_input_query(string_operation)

			print cube.query_matrix(x1,y1,z1,x2,y2,z2)
		else:
			raise ValueError('UNDEFINED OPERATION: '+operation)
