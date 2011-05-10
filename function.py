POPULATION_COUNT = 500
MAX_FUNC_DEPTH = 14
ITERATIONS = 200

from pdb import set_trace
from functions import *
from functions_manager import split_function
def create_test_data():
	u'returns (function, function table)'
	f = Add(Sin(Add(Mul(Const(5),Dec(X(),Const(3))),Const(7))), Const(5))
	f = Mul(Cos(X()), Add(Sin(X()), Mul(Const(4), X())))
	return (f, [(i, f.get_value(i)) for i in range(100)])

class FunctoionContainer(object):
	def __init__(self, f_choose_parent, f_choose_to_kill, f_create_children):
		self.f_choose_parent = f_choose_parent
		self.f_choose_to_kill = f_choose_to_kill
		self.f_create_children = f_create_children

class Options(object):
	def __init__(self, children_ratio):
		self.children_ratio = children_ratio


from mutator import Mutator
from strategies import choose_parent_pairs2, choose_to_kill, create_children, create_population
from qa import mistake
from normalizator import Normalizator
import sys
def write_init_data(file, function, data):
    set_trace()
    to_write = 'aproximated function: %s\npoints: %s' % (function, '\n'.join([str(d) for d in data]))
    file.write(to_write)
    file.write('\nITERATION_NUMBER:MISTAKE:FUNCTION\n\n')
    
def write_population_data(file, iteration, solution, mistake):
    file.write(str(iteration))
    file.write(':')
    file.write(str(mistake))
    file.write(':')
    file.write(str(solution.f))
    file.write('\n')
def main():
    global POPULATION_COUNT, ITERATIONS, MAX_FUNC_DEPTH
    file = open('data.txt', 'w')
    if len(sys.argv) == 3: ITERATIONS = int(sys.argv[1])
    if len(sys.argv) == 3: POPULATION_COUNT = int(sys.argv[2])

    f, data = create_test_data()
    write_init_data(file, f, data)

    population = create_population(POPULATION_COUNT, MAX_FUNC_DEPTH)
    normalizator = Normalizator(data, mistake)

    functions = FunctoionContainer(choose_parent_pairs2, choose_to_kill, create_children)
    options = Options(0.4)	
    mutator = Mutator(population, normalizator, options, functions)


    print 'population: '
    #for s in population: print 'm: ', mistake(s.f, data), '\t\ts.f: ', s.f
    for i in range(ITERATIONS):
        print 'population ' + str(i) + ' : '
        for j  in range(5):
            s = population[(j+1)*(-1)]
            print 'm: ', mistake(s.f, data), '\t\ts.f: ', s.f
            if j == 1: # ITERATION_NUMBER:MISTAKE:FUNCTION
                write_population_data(file, i, s, mistake(s.f, data))
        mutator.make_children()
        mutator.kill_unused()
    #	mutator.change_random()
        mutator.change_age()
        mutator.mutate()
        normalizator.compute_distribuante(population)
        population.sort()
    file.close()
        
	
if __name__ == '__main__':
	main()
