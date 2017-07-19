from Function import Step

class Propagator:

	def __init__(self, a=None, b=None, c=None, d=None, e=None):
		self.setparams(a, b, c, d, e)

	def setparams(self, a=None, b=None, c=None, d=None, e=None):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.e = e

	def getlimit(self):
		return self.b + self.e + int(self.d/2)

	def move(self):
		self.b += self.e

	def __call__(self, x):
		self.b = 0

		run = True
		out = []

		while run:
			self.move()

			l = self.b-int(self.d/2)
			u = self.b+int(self.d/2)
			set = []

			for i in range(l, u):
				set.append(x[i])

			run = self.getlimit() < len(x)
			val = self.function(set)
			out.append(val)

		return out

	def function(self, x):
		l = x[0]
		u = x[0]

		for i in range(len(x)):
			if x[i] < l: l = x[i]
			if x[i] > u: u = x[i]
	
		step = Step(self.a, self.c)
		return step(u-l)

