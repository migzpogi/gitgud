# Maps
# http://book.pythontips.com/en/latest/map_filter.html
# https://www.w3schools.com/python/ref_func_map.asp
# Date: Sep 21, 2018

# Map applies a function to all the items in an input list
# map(function_to_apply, list_of_inputs)

# Traditionally...

items = [1,2,3,4,5]
squared = []
for i in items:
    squared.append(i**2)

print(squared)

# Using map

items = [1,2,3,4,5]
def square(x):
    return x**2
squared = list(map(square, items))
print(squared)

# Using map and lambda

items = [1,2,3,4,5]
squared = list(map(lambda x: x**2, items))
print(squared)

# More examples
def myfunc(a, b):
    return a + b

x = list(map(myfunc, (1,2), (3,4)))
print(x)