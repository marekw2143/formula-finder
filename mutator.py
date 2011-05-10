from random import random, choice
from functions_manager import rand_function
from random import randrange
MAX_FUNC_DEPTH = 20
from strategies import *
from functions_manager import f0, f1, f2
from xray import Doctor

class Mutator(object):
	def __init__(self, population, normalizator, options, functions):
		u'''	f_choose_kill - returns indexes of solutions to be killed
			f_choose_parent - returns list of pairs parent to make children
			f_create_children - creates tuple of children from 2 parents
			population - list of solutions'''
		self.population = population
		self._normalizator = normalizator

		self._children_ratio = options.children_ratio

		self._f_choose_parent = functions.f_choose_parent
		self._f_choose_kill = functions.f_choose_to_kill
		self._f_create_children = functions.f_create_children
			
		
	def make_children(self):		
		u'creates children, stores them in private field _childrenj'
		self._normalizator.compute_distribuante(self.population)
		self.population.sort()
		protection_amount = 3
		c = 0
		for i in range(protection_amount): 
			
			self.population[-1 - c].protection_age = protection_amount - i
			print 'self.population[',-1-c,'].protection_age: ', self.population[-1-c].protection_age,' f: ', self.population[-1-c].f
			c += 4
			
		amount = int(self._children_ratio * len(self.population))
		pairs = self._f_choose_parent(self.population, amount)
		self._children = []
		for p in pairs:
			for ch in self._f_create_children(p):
				self._children.append(ch)	
		
	
	def kill_unused(self):
		u'kills some elements of population, inserting in their place newly created children'
#		self.population.sort() #used to display five best solutions
		self._normalizator.compute_distribuante(self.population)
		to_kill = self._f_choose_kill(self.population, len(self._children))
		if len(self._children) != len(to_kill): raise Exception('inproper working _f_choose_kill, len(self._children): ')
		for i in range(len(self.population)):
			if i in to_kill and self.population[i].protection_age <=0 : self.population[i] = self._children.pop(-1)
		
	def change_random(self):
		u'changes random solutions by brand new solutions'
		if random() < 0.1:
			for i in range(randrange(int(0.3 * len(self.population)))):
				idx = randrange(len(self.population))
				if self.population[idx].protection_age > 0: continue
				self.population[idx] = Solution(rand_function(MAX_FUNC_DEPTH))



	def mutate(self):
		u'mutates randomly selected elements of population'
		doctor = Doctor()
		for s in choose_solutions_to_mutate(self.population, int(0.4 * len(self.population))):
			if s.protection_age > 0: continue
			if s.f.__class__ in f0: s.f = doctor.get_new_function(s.f)
			else: doctor.mutate_gen(*doctor.choose_gen_to_mutate(s.f))

	def change_age(self):
		u'decreases age of all population elements'
		for s in self.population: 
			s.generation_no -= 1
			s.protection_age -= 1
				



from functions_manager import rand_function_const_depth
if __name__ == '__main__':
	f = rand_function_const_depth(3)
	print 'f: ', f
	doctor = Doctor()
	ch1 = doctor.choose_gen_to_mutate(f)
	ch2 = doctor.choose_gen_to_mutate(f)
	print 'ch1: (',ch1[0],', ',ch1[1],')'
	doctor.mutate_gen(*ch1)
	print 'f: ', f
	
	

