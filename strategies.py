from random import random, choice
from functions_manager import rand_function
from random import randrange

def get_idx(v, population):
	u'returns index of solution from population with the lowest distribuante that is higher or equal to v'
	idx = 0
	for s in population: # TODO: consider whether iterating through i =0 .. len(population) will be beter due to certain ordering in population
		if s.distrib >= v: return idx
		idx += 1
	raise Exception('Solution with s.mistake >= ' + str(v) + ' doesn\'t exist')	

def choose_parent_pairs(population, amount = 1, history = None):
	u'chooses amoutn of pairs to recombine, choose is based on mistake function probability of each parent'
	return[ ( population[get_idx(random(), population)], population[get_idx(random(), population)]) for i in range(amount)]
		
def choose_parent_pairs2(population, amount = 1, history = None):
	ret = []
	tmp = int(amount * 0.6)
	for i in range(amount):
		if i< tmp:
			ret.append(( population[get_idx(random(), population)], population[get_idx(random(), population)]))
		else: ret.append((choice(population), population[get_idx(random(), population)]))
	return ret

def choose_parent_pairs3(population, amount = 1, history = None): 
	return [(choice(population), choice(population)) for i in range(amount)]

def choose_solutions_to_mutate(population, amount):
	return [choice(population) for i in range(amount)]

def choose_solutions_to_mutate_by_prob(population, amount):
	return 

def choose_to_kill(population, amount, history = None):
	u'returns indexes of solutions to be killed'
	amount = len(population) - amount	
	surviwed = []
	repeated = 0
	indexes = range(len(population))
	for i in range(amount):
		found, idx = False, -1
		while not found:	
			idx = get_idx(random(), population)
			if population[idx].protection_age > 0: continue
			if idx not in surviwed:
				found = True
				repeated = 0
				indexes.remove(idx)
			else: 
				repeated += 1
				if repeated == 3:
					idx = indexes.pop(-1)
					repeated = 0
					found = True

		surviwed.append(idx)
	return [i for i in range(len(population)) if i not in surviwed]

from copy import deepcopy
from functions_manager import split_function
from functions_manager import split_function
def create_children(parents, history = None):
	u'returns tuple containing 2 children from 2 parents'
	x, y = parents
	c1, c2 = deepcopy(x), deepcopy(y)
	m1 = split_function(c1.f, 0.25)
	m2 = split_function(c2.f, 0.25)	
	if m1[1] == None or m2[1] == None:
		if m1[1] == None and m2[1]:
			if m2[2] == 1: m2[1].child1 = deepcopy(m1[0])
			elif m2[2] ==2: m2[1].child2 = deepcopy(m1[0])
		elif m2[1] == None and m1[1]:
			if m1[2] == 1: m1[1].child1 = deepcopy(m2[0])
			elif m1[2] ==2: m1[1].child2 = deepcopy(m2[0])
			
	else:
		if m1[2] == 1: # first child
			m1[1].child1 = m2[0]
		else: m1[1].child2 = m2[0]

		if m2[2] == 1:
			m2[1].child1 = m1[0]
		else: m2[1].child2 = m1[0]
	
	return (c1,c2)

from solution import Solution
from functions_manager import rand_function
create_population = lambda amount, max_dept: [Solution(rand_function(max_dept)) for i in range(amount)]
