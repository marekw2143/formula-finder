delta = 0.005
def mistake(f, data):
	u'''computes target function
	data - coordinates of function to minimize
	solution for which the target function is beeing computed'''

	ret = 0
	
	add = 1.0 # added when point is't the same as a sample
	ratio = 10.01 # value that difference between original is multipled by

	for p in data:
		diff = abs(f.get_value(p[0]) - p[1]) 

		if diff > delta: ret += add + diff * ratio * 2.5
		elif diff > delta * 0.5:  ret += add + diff * ratio 
		
	return ret


