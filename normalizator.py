class Normalizator():

	def __init__(self, data, mistake_function):
		self.data = data
		self.f_mistake = mistake_function

	def _compute_mistakes(self):
		for s in self.population:	
			s.mistake = self.f_mistake(s.f, self.data)
	
	def _invert_mistakes(self):
		for s in self.population:
			try:
				s.mistake = 1.0 / s.mistake
			except ZeroDivisionError:
				s.mistake = 100000

	def _normalize_mistakes(self):
		u'normalize target function'
		suma = 0.0 
		for s in self.population:
			suma += s.mistake

		# normalize mistake
		for s in self.population:
			s.mistake /= suma

	def _compute_distribuante(self):
		last = 0.0
		for s in self.population:
			s.distrib = s.mistake
			s.distrib += last
			last = s.distrib
	
	def compute_distribuante(self, population):
		self.population = population
		self._compute_mistakes()
		self._invert_mistakes()
		self._normalize_mistakes()
		self._compute_distribuante()
