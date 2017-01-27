

def parse_input_update(string_operation):
	string_operation = string_operation.split(' ')
	x = int(string_operation[1])
	y = int(string_operation[2])
	z = int(string_operation[3])
	W = int(string_operation[4])
	return x,y,z,W
def parse_input_query(string_operation):
	string_operation = string_operation.split(' ')
	x1 = int(string_operation[1])
	y1 = int(string_operation[2])
	z1 = int(string_operation[3])
	x2 = int(string_operation[4])
	y2 = int(string_operation[5])
	z2 = int(string_operation[6])
	return x1,y1,z1,x2,y2,z2
