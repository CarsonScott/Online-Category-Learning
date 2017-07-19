from Histogram import Histogram
from Propagator import Propagator
from Extractor import Extractor
from Estimator import Estimator

class Classifier:

	def __init__(self, histogram):
		self.distribution = []		
		self.generalization = []	
		self.abstraction = []

		self.filter = Propagator()
		self.plotter = Estimator()
		self.detector = Extractor()
		self.plotter.setspace(histogram)

	def setgrowth(self, height, sd):
		self.plotter.setgrowth(height, sd)

	def setdecay(self, height, grad):
		self.plotter.setdecay(height, grad)

	def select(self, x):
		classes = []

		i = 0
		for c in self.detector.classes:
			if x in range(c[0], c[1]): classes.append(i)
			i += 1

		return classes

	def __call__(self, x):
		self.plotter.plot(x)
		if len(self.abstraction) > 0: 
			return self.select(x)
		return []
	
	def update(self):
		self.distribution = self.plotter()
		self.generalization = self.filter(self.distribution)

		factor = int(len(self.generalization) / len(self.distribution))
		self.abstraction = self.detector(self.generalization, factor)
