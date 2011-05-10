class Solution(object):
	u'''f - approximation
		mistake - mistake of the approximation
		distrib - used by mutator, computed by normalizator
		generation_no - age when was genrated
		protection_age - generations that must be before the solution can be killed'''

	def __init__(self, f, gen_no = -1, protection_age = -1):
		self.f = f
		self.mistake = None
		self.distrib = None
		self.generation_no = gen_no
		self.protection_age = protection_age

	def __cmp__(self, other):
		return cmp(self.mistake, other.mistake)

	def __str__(self):
		return 'mistake: ' + str(self.mistake) + ' function: ' + str(self.f)

