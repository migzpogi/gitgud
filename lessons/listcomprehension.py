# List Comprehension
# https://www.pythonforbeginners.com/lists/list-comprehensions-in-python/
# Date: Aug. 30, 2018

### old format

numbers = [1,2,3,4,5,6,7,8,9,10]

odd = []
for n in numbers:
    if n%2:
        odd.append(n)

print(odd)

### new format

odd_new = [n for n in numbers if n%2]
print(odd_new)

### other examples

squares = [n**2 for n in numbers if n%2]
print(squares)