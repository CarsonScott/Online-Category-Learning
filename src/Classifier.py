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
		dividers = self.detector.dividers
		
		if x < dividers[0]: x = dividers[0]
		if x > dividers[len(dividers)-1]: x = dividers[len(dividers)-1]

		for i in range(len(dividers)-1):
			if x in range(dividers[i], dividers[i+1]):
				return i

	def __call__(self, x):
		self.plotter.plot(x)
		if len(self.abstraction) > 0: 
			return self.select(x)
		return []
	
	def update(self):
		self.distribution = self.plotter()
		self.generalization = self.filter(self.distribution)

		length = len(self.distribution)
		self.abstraction = self.detector(self.generalization, length)
