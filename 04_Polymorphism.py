'''
Polymorphism

-The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types.

'''

'''
Method Overloading

- Method Name Same but Argu. diffrent
- Python doesn't support method overloading
'''

'''
Method Overriding

- Same Name, Same Argu, But Diffrent class
'''

class c1:

    def cal(self,a,b):
        print(a+b)

class c2(c1):

    def cal(self,a,b):
        print(a-b)

a = c2()

a.cal(10,5)