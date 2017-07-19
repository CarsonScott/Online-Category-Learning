from Histogram import *
from Function import Gaussian, Logistic

class Estimator:

	def __init__(self, histogram=None):
		self.space = histogram
		self.growth = Gaussian()
		self.decay = Logistic()

		self.g_rate = 0.007
		self.d_rate = 0.003

	def setspace(self, histogram):
		self.space = histogram

	def setgrowth(self, height, std_dev):
		self.growth.setparams(height, None, std_dev)

	def setdecay(self, height, gradient):
		self.decay.setparams(height, 0, gradient)
		self.decay.reflect()

	def setlimit(self, height, gradient):
		self.limit.setparams(height, 0, gradient)

	def plot(self, x):
		self.growth.b = x
		kernel = self.growth.c
		size = self.space.width

		for i in range(x-kernel, x+kernel):
			if i in range(0, size):
				self.space.plot(i, self.growth(i) * self.g_rate)

		for i in range(len(self.space.bins)):
			b = self.space.bins[i]

			if b < 0: b = 0
			if b > 0: b -= self.decay(b) * self.d_rate

			self.space.bins[i] = b

	def __call__(self):
		return self.space.bins