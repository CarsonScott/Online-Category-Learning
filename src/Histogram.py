from math import floor

class Histogram:

	def __init__(self, width, bins):
		self.width = width
		self.bins = []
		for i in range(bins):
			self.bins.append(0)

	def __call__(self, x, v):
		print(floor(x/self.width) * self.width)
		self.bins[int(x)] += v
