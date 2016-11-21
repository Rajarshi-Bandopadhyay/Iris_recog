class superobj:
	def __init__(self, name):
		self.points = []
		self.name = float(name)
		self.points.append(name)
		self.stpnt = -1
	
	def readlist(self, oblst):
		rem = []
		for n, i in enumerate(oblst):
			if i[0] == self.points[-1]:
				self.points.append(i[1])
				if self.stpnt == -1: self.stpnt = n
			else: rem.append(i)
		return rem
