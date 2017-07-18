from Function import Step
from random import randrange as rr

class Kernel:

	def __init__(self):
		self.width = None
		self.step = None
		self.position = None
		self.space = []

	def create(self, width, step):
		self.width = width
		self.step = step

		for i in range(self.width*2):
			self.space.append(int())

	def update(self, limit):
		self.position += self.step
		if self.position+int(self.width/2) <= limit:
			return True
		return False

	def __call__(self, x):
		y = []
		self.position = 0

		running = True
		while running:
			c = 0
			for i in range(self.position- int(self.width/2), self.position+int(self.width/2)):
				self.space[c] = x[i]
				c += 1

			y.append(self.function(self.space))

			running = self.update(len(x))

		return y

	def function(self, x):
		return

class Contrast(Kernel):

	def __init__(self, threshold):
		super().__init__()
		self.threshold = threshold

	def setstep(self, height, center):
		self.step.create(height, center, None)

	def function(self, x):
		l = None
		u = None
		for i in range(len(x)):
			if i == 0:
				l = x[i]
				u = x[i]
			else:
				if x[i] < l: l = x[i]
				if x[i] > u: u = x[i]
		
		return self.threshold(u-l)
