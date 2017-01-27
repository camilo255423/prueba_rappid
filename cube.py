
class Cube:
	def __init__(self,N):
		self.matrix=[[[0 for x in xrange(N)] for y in xrange(N)] for y in xrange(N)]
	def update_matrix(self,x,y,z,W):
	    self.matrix[x-1][y-1][z-1]=W
	    
	def query_matrix(self,x1,y1,z1,x2,y2,z2):
		sum = 0
		for x in xrange(x1-1,x2):
			for y in xrange(y1-1,y2):
				for z in xrange(z1-1,z2):
					sum = sum + self.matrix[x][y][z]
		return sum
