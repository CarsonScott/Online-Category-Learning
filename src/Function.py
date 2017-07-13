e = 2.718281828459

class Function:

	def __init__(self):
		self.a = None
		self.b = None
		self.c = None

	def create(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def __call__(self, x):
		return

class Gaussian(Function):

	def __call__(self, x):
		return self.a * pow(e, -pow(x-self.b, 2) / pow(2 * self.c, 2))

class Logistic(Function):

	def __call__(self, x):
		return self.a / (1+pow(e, -self.c * (x-self.b)))
