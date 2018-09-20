# Lambdas
# https://www.w3schools.com/python/python_lambda.asp
# Date: Sep 20, 2018

# Lambda is a small anonymous function
# Can take any number of arguments, but can only have 1 expression

# Syntax: lambda arguments : expression

x = lambda a : a + 10
print(x(10))

y = lambda a, b, c : print('Your arguments are: {}, {} and {}'.format(a, b, c))
y('Migz', 1, ['Estrella', 24])

# Why use lambda functions?

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))