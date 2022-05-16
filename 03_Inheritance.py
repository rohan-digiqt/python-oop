'''
Inheritance

-> Inheritance is the capability of one class to derive or inherit the properties from another class.
'''

# Parent Class

class Person:

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display(self):
        print(self.name)
        print(self.id)
    
    def details(self):
        print(f'My Name is {self.name}')
        print(f'My Id is {self.id}')


#Child Class

class Employee(Person):

    def __init__(self,name,id,salary,post):
        self.name = name
        self.id = id
        self.salary = salary
        self.post = post

        # Parent Class Method
        Person.__init__(self, name, id)

    def details(self):
        print(f'My Name is {self.name}')
        print(f'Id id {self.id}')
        print(f'Post is {self.post}')

a = Employee('Rohan',107,5000,'Software Engineer')

a.display()
a.details()