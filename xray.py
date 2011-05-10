from random import random, randrange
from functions_manager import f0, f1, f2

class Doctor(object):
	u'responsible for mutating genoms'
	def get_new_function(self, f):
		u'returns mutated version of function f'
		from functions import *
		from random import randrange
		max_range = 20
		if f.__class__ == X: return Mul(Const(randrange(max_range)), X())
		elif f.__class__ == Const: return Const(randrange(max_range))

	def choose_gen_to_mutate(self, f, parent = None, childno = -1):
		u'returns: (parent function, child number to mutate) where parent_function.childnumber is in the f0'
		if not f and parent and childno:
			if childno == 1: f = parent.child1
			elif childno ==2: f = parent.child2

		if f.__class__ in f0: return (parent, childno)
		elif f.__class__ in f1: return self.choose_gen_to_mutate(f.child1, f, 1)
		elif f.__class__ in f2:
			if random() < 0.5: return self.choose_gen_to_mutate(f.child1, f, 1)	
			else: return self.choose_gen_to_mutate(f.child2, f, 2)

	def mutate_gen(self, parent, childno):
		u'changes parents cihldren with number childno, that children must be in f0'
			
		max_range = 20
		
		f = None # reference to child function
		if childno == 1: f = parent.child1
		elif childno == 2: f = parent.child2
		
		new_f = self.get_new_function(f)
		if childno == 1: parent.child1 = new_f
		elif childno == 2: parent.child2 = new_f



