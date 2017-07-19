class Extractor:

	def __init__(self):
		self.classes = None

	def __call__(self, distribution, factor):
		self.classes = ([])

		active = False
		current = [None, None]

		distribution.append(0)

		p = 0
		for p in range(len(distribution)):
			if active and not distribution[p]:
				active = False
				current[1] = p

			if not active and distribution[p]:
				active = True
				current[0] = p

			if not active and current[0] != None and current[1] != None:
				self.classes.append(current)
				current = [None, None]


		return self.classes



