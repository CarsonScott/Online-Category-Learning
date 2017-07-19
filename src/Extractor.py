class Extractor:

	def __init__(self):
		self.dividers = None

	def __call__(self, distribution, length):	
		self.dividers = []
		last = None


		for p in range(len(distribution)):

			val = distribution[p] > 0
			if p == 0 or last != val:
				self.dividers.append(p)
				last = val
		
		self.dividers.append(length)
		return self.dividers



