# Properties vs. Getter and Setters
# From: https://www.python-course.eu/python3_properties.php
# Date: Aug. 30, 2018


# private attribute vs public attribute

class A:
    def __init__(self, x, y):
        self.__x = x
        self.y = y

a = A(1, 2)
# print(a.x) : will produce an AttributeError
print(a.y)

########## ########## ########## ########## ##########

# java-esque way in designing a class with getters and setters to encapsulate the
# private attribute self.__x

class P:
    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x


p1 = P(100)
print(p1.get_x())
p1.set_x(99)
print(p1.get_x())

########## ########## ########## ########## ##########

# pythonic way of class P

class B:
    def __init__(self, x):
        self.x = x

b = B(69)
print(b.x)
b.x = 169
print(b.x)

########## ########## ########## ########## ##########

# implementation change using getters, setters

class C:
    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

c1 = C(-1)
print(c1.get_x())
c2 = C(69)
print(c2.get_x())
c3 = C(1001)
print(c3.get_x())


########## ########## ########## ########## ##########

# implementation change using properties

class D:
    def __init__(self, x):
        self.__x = x
        self.__y = 10

    @property
    def a(self):
        return self.__y

    @a.setter
    def a(self, a):
        self.__y = a

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

d = D(1)
print(d.x)
d.x = 1001
print(d.x)
print(d.a)
d.a = 9
print(d.a)