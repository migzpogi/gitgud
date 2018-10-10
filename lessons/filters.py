# Filters
# https://www.programiz.com/python-programming/methods/built-in/filter
# Date: Oct. 10, 2018

# Constructs an iterator from elements of an iterable for which a function returns true
# Syntax: filter(function, iterable)

alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def filter_vowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if alphabet in vowels:
        return True
    else:
        return False

filtered = filter(filter_vowels, alphabets)
print(alphabets)
print(list(filtered))