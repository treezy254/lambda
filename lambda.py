# Lambda Calculus
"""
map()
filter()
reduce()

sort(), sorted(), min(), max()

func
"""
# identity function

def identity(x):
	return x

lambda x: x

"""
The keyword: lambda
A bound variable: x
A body: x"""

lambda x: x + 1

# Reduction is a lambda calculus strategy to compute the value of the expression.
(lambda x: x + 1)(2)

add_one = lambda x: x + 1
add_one(2)

# similar to:
def add_one(x):
	return x + 1

# Multi-argument function
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')

# -------

# Anonymous Functions

lambda x, y : x + y

(lambda x, y: x + y)(2, 3)

# Higher order functions
high_ord_func = lambda x, func: x + func(x)
high_ord_func(2, lambda x: x * x)

high_ord_func(2, lambda x: x + 3)


# Functions
import dis
add = lambda x, y: x + y
type(add)

dis.dis(add)

add_one


import dis
def add(x, y): reurn x + y 
type(add)

dis.dis(add)

add 

# ------------------

# No Statements
# lambda functions cant contain any statements

# Single Expressions
(lambda x : (x % 2 and 'odd' or 'even'))(3)

# Arguments
"""
Position Arguments
Named arguments(kwargs)
variable list of arguments (varagrs)
variable list of keyword arguments
keyword-only arguments
"""
(lambda x, y, z: x + y + z)(1, 2, 3)

(lambda x, y, z=3: x + y + z)(1, 2)

(lambda x, y, z=3: x + y + z)(1, y=2)

(lambda * args: sum(args))(1, 2, 3)

(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)

(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)


# Decorators
def some_decorator(f):
	def wraps(*args):
		print(f"calling function '{f.__name__}' ")
		return f(args)
	return wraps


@some_decorator
def decorated_function(x):
	print(f"With argument '{x}'")


# Defining a decorator
def trace(f):
	def wrap(*args, **kwargs):
		print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
		return f(*args, **kwargs)

	return wrap


# Applying decorator to a function
@trace
def add_two(x):
	return x + 2


# calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x:x ** 2))(3))

list(map(trace(lambda x: x*2), range(3)))

# CLosure
""" A closure is a function where every free varible, everything except parameters used in that function isbound to a specific value defined in the enclosing scope of that function."""
def outer_func(x):
	y = 4
	def inner_func(z):
		print(f"x = {x}, y = {y}, z = {z}")
		return x + y + z
	return inner_func


for i in range(3):
	closure = outer_func(i)
	print(f"closure({i+5}) = {closure(i+5)}")


# Similarly
def outer_func(x):
	y =- 4
	return lambda z: x + y + z

for i in range(3):
	closure = outer_func(i)
	print(f"closure({i+5}) = {closure(i+5)}")


# =-------

# Python Classes

class Car:
	""" car with methods as lmbda function"""
	def __init__(self, brand, year):
		self.brand = brand
		self.year = year

	brand = property(lambda self: getattr(self, '_brand'),
					lambda self, value: setattr(self, '_brand', value))

	year = property(lambda self: getattr(self, '_year'),
					lambda self, value: setattr(self, '_year', value))

	__str__ = lambda self: f'{self.brand} {self.year}' # 1: error E731

	honk = lambda self: print('Honk!')


	# timeit

	from timeit import timeit
	timeit("factorial(999)", "from math import factorial", number=10)

	from math import factorial
	timeit(lambda: factorial(999), number=10)


	# Map
	"""The built in function map() takes a function as a first argument ad applies it toeah of the elements of its second argument, an iterable.
	Map() returns an iterator corresponding to the transformed collection."""

	list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))

	# Filter
	""" The built-in function filter(), another classic functional construct, can be converted into a list comprehension.
	It takes a predicate as a first argument and an iterable as a second argument.
	It builds an iterator containing all the elemnts of the initial collection that satisfies the predicate function.
	"""
	even = lambda x: x%2 == 0
	list(filter(even, range(11)))

	[x for x in range(11) if x%2 == 0]

	# Reduce

	""" Its first two arguments are respectively a function and an iterable.
	reduce() applies the function and accumulates the result that is returned when the iterable is exhausted."""

	import functools
	pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
	functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0)

	# similarly
	pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
	sum(x[0] for x in pairs)

	# also
	pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
	sum(x for x, _ in pairs)

	