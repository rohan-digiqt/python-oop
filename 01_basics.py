class Students:
    def __init__(self, aname, aer, abranch, asubject):
        self.name = aname
        self.er = aer
        self.branch = abranch
        self.subject = asubject

    clg = 'GMIT' # Class Variable

    def printDet(self):
        return f"The Name is {self.name}, Enrollment is {self.er} and Branch  is {self.branch}"

# rohan = Students() '''Instance of Students() class'''

# rohan.name = 'Rohan'
# rohan.er = 44
# rohan.branch = 'Computer'
# rohan.subjects = ['DSA','ADA']  # Instance Variables

# print(rohan.er, rohan.branch, rohan.subjects)
# print(rohan.__dict__)
# print(rohan.clg)
# print(rohan.printDet()) # 'rohan' is automaticly pass as an argument of function


''' Constructor: It is a way to give argunment to class'''

tanmay = Students('Tanmay',55,'Computer',['DE','CPD'])
print(tanmay.subject)