from Function import *
from Histogram import *
from random import randrange as rr

class Classifier:

	def __init__(self, histogram):
		self.space = histogram
		self.growth = Gaussian()
		self.decay = Logistic()

		self.g_rate = 0.05
		self.d_rate = 0.01

	def setgrowth(self, height, stddev):
		self.growth.create(height, None, stddev)

	def setdecay(self, height, steep):
		self.decay.create(height, 0, steep)

	def plot(self, x):
		self.growth.b = x
		kernel = self.growth.c
		size = self.space.width

		for i in range(x-kernel, x+kernel):
			if i >= 0 and i < size:
				self.space(i, self.growth(i) * self.g_rate)

	def update(self):
		for i in range(len(self.space.bins)):
			b = self.space.bins[i]

			if b > 0: b -= self.decay(b) * self.d_rate
			if b < 0: b = 0

			self.space.bins[i] = b
