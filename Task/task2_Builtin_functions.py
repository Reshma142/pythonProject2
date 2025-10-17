# List of Builtin Functions

# 1.Numeric and Type Conversion Functions
"""
abs(x)	Returns the absolute value of a number
round(x, n)	Rounds a number to n decimal places
pow(x, y)	Returns x raised to the power y
divmod(x, y)	Returns a tuple (quotient, remainder)
int(x)	Converts to an integer
float(x)	Converts to a float
complex(x, y)	Returns a complex number
bool(x)	Converts to a Boolean value
bin(x)	Converts an integer to a binary string
oct(x)	Converts an integer to an octal string
hex(x)	Converts an integer to a hexadecimal string
"""
# 2. String and Character Functions

'''
chr(x)	Returns the character for the given Unicode code
ord(x)	Returns the Unicode code for a character
str(x)	Converts to a string
format(x, spec)	Formats a value according to the format specifier
'''
# 3.Sequence and Collection Functions
'''
len(x)	Returns the number of items
max(x)	Returns the largest item
min(x)	Returns the smallest item
sum(x)	Returns the sum of elements
sorted(x)	Returns a sorted list
reversed(x)	Returns a reverse iterator
enumerate(x)	Returns an enumerate object (index, value)
zip(a, b, ...)	Combines multiple iterables element-wise
all(x)	Returns True if all elements are true
any(x)	Returns True if any element is true
'''
# 4. Type Checking and Information Functions
'''
type(x)	Returns the type of an object
isinstance(x, type)	Checks if an object is an instance of a type
id(x)	Returns the unique ID of an object
dir(x)	Returns a list of attributes/methods of an object
vars(x)	Returns the __dict__ attribute of an object
help(x)	Displays the documentation for an object
callable(x)	Checks if the object is callable (like a function)
'''
# 5.Object and Variable Management
'''
delattr(obj, name)	Deletes an attribute from an object
getattr(obj, name)	Returns the value of a named attribute
setattr(obj, name, value)	Sets the value of a named attribute
hasattr(obj, name)	Checks if the object has a named attribute
'''
# 6.Input/Output Functions
'''
print()	Prints output to the console
input()	Takes user input as a string
open(filename, mode)	Opens a file and returns a file object
'''
# 7.Functional Programming Tools
'''
map(func, iterable)	Applies a function to all elements
filter(func, iterable)	Filters elements based on a condition
reduce(func, iterable)	Applies a function cumulatively (from functools)
lambda	Creates anonymous functions
'''
# 8.Miscellaneous
'''
range(start, stop, step)	Generates a sequence of numbers
eval(expression)	Evaluates a Python expression (string)
exec(code)	Executes Python code dynamically
globals()	Returns the global symbol table
locals()	Returns the local symbol table
compile(source, filename, mode)	Compiles source code into a code object
'''