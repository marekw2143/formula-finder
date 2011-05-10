def mprint(txt): print txt

def print_population(base_text = None):
	if base_text: print base_text
	print '\tsolutions:'
	for s in population:
		print '\t\t', s

def get_total_mistakes(population):
	suma = 0.0
	for s in population:
		suma += s.compute_mistake()
	return suma

