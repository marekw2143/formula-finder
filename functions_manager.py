from functions import *
from random import random, randrange, choice

f2 = (Add, Mul, Dec)
f1 = (Cos, Sin)
f0 = (Const, X)

args = (f2, f1)

g_max_depth = 55
max_const = 20

	
def rand_function_const_depth(max_depth):
	return rand_function(max_depth, False)
def rand_function(max_depth, cut_random = True):
	u'''creates random function
		max_depth - max redundance level
		cut_random - whether the max_depth depth will not be reached with 100% probability or not
	'''
	f = None
	if cut_random == True:
		if random() < 0.5: max_depth -= randrange(g_max_depth)
	if max_depth > 1:
		ch = choice(args)
		if ch == f1:
			f = choice(f1)
			f = f(rand_function(max_depth - 1, cut_random))
		elif ch == f2:
			f = choice(f2)	
			f = f(rand_function(max_depth - 1, cut_random), rand_function(max_depth - 1, cut_random))
	else:
		f = choice(f0)
		if f == Const: f = f(randrange(max_const))
		elif f == X: f = f()	
	return f

def split_function(f, p, only_f0 = False, parent = None, child_number = -1, first_call = True):
	u'returns part of the function given as the first argument that is another function'
	if f.__class__ in f0: 
		if parent is not None:
			if child_number == 1: parent.child1 = None
			elif child_number == 2: parent.child2 = None
		return (f, parent, child_number)
	if not first_call and not only_f0 and random() < p:
		if parent is not None:
			if child_number == 1: parent.child1 = None
			elif child_number == 2: parent.child2 = None
		return (f, parent, child_number)
	else:
		ret = None	
		childno = 1
		if f.__class__ in f2:
			if random() < 0.5: ret = f.child1
			else: 
				ret = f.child2
				childno = 2
		elif f.__class__ in f1 or f.__class__ in f0: 
			ret = f.child1
		return split_function(ret, p * 1.5, only_f0, f, childno, False)
