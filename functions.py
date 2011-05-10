# optimizations with cache must be done only when child elemens doesn't change, if they change, the singnal should be connected to then to delete cache
from math import cos, sin

class Function(object):
	pass

class Function2(Function):
	def __init__(self, child1, child2):
		self.child1, self.child2 = child1, child2
#		self._child1, self._child2 = child1, child2
#		self._cache = {}
	def __str__(self, op): return '( ' + str(self.child1) + op + str(self.child2) + ' )'
#	def getchild1(self): return self._child1
#	def setchild1(self, val):
#		self._cache = {}
#		self._child1 = val
#	def getchild2(self): return self._child2
#	def setchild2(self, val):
#		self._cache = {}
#		self._child2 = val
#	child1 = property(getchild1, setchild1, None)
#	child2 = property(getchild1, setchild1, None)

class Function1(Function):
	def __init__(self, child1):
		self.child1 = child1
#		self._cache = {}
	def __str__(self, op): return op + '( ' + str(self.child1) + ' )'

class Add(Function2):
	def get_value(self, x):	return self.child1.get_value(x) + self.child2.get_value(x)
	def __str__(self): return super(Add, self).__str__('+')
class Dec(Function2):
	def get_value(self, x): return self.child1.get_value(x) - self.child2.get_value(x)
	def __str__(self): return super(Dec, self).__str__('-')

class Mul(Function2):
	def get_value(self, x):
		return self.child1.get_value(x) * self.child2.get_value(x)
		
	def __str__(self): return super(Mul, self).__str__('*')

class Pow(Function2):
	def get_value(self, x): return int(self.child1.get_value(x)) ^ int(self.child2.get_value(x))
	def __str__(self): return super(Pow, self).__str__('^')

class Const(Function):
	def __init__(self, val):self.val = val
	def get_value(self, x): return self.val
	def __str__(self): return str(self.val)

class X(Function):
	def __init__(self):pass
	def get_value(self, x):return x
	def __str__(self): return 'x'

class Cos(Function1):
	def get_value(self, x):
		return cos(self.child1.get_value(x))
	def __str__(self): return super(Cos, self).__str__('cos')

class Sin(Function1):
	def get_value(self, x):
		return sin(self.child1.get_value(x))
	def __str__(self): return super(Sin, self).__str__('sin')

