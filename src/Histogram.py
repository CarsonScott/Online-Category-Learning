from math import floor

class Histogram:

	def __init__(self, width=None, bins=None):
		self.setparams(width, bins)

	def setparams(self, width=None, bins=None):
		self.width = width
		self.bins = []

		for i in range(bins):
			self.bins.append(0)

	def plot(self, x, v):
		self.bins[int(x)] += v
		