'''
Encapsulation
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit.
'''

class Base:

    def __init__(self):
        self.a = 'Rohan - 1'
        self.__b = 'Rohan - 2'

class Derived(Base):

    def __init__(self):
        Base.__init__(self)
        print(self.__c)

obj1 = Derived()

obj1.__init__

# Error -> variable c is not access in Derived class