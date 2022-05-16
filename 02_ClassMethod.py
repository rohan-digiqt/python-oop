class Students:
    def __init__(self, aname, aer, abranch, asubject):
        self.name = aname
        self.er = aer
        self.branch = abranch
        self.subject = asubject

    clg_fee = 70000 # Class Variable

    def printDet(self):
        return f"The Name is {self.name}, Enrollment is {self.er} and Branch  is {self.branch}"

    # Class Method
    def change_fee(cls, newclg):
        cls.clg_fee = newclg

rohan = Students('Rohan',44,'Computer',['DS','DBMS'])
tanmay = Students('Tanmay',55,'Computer',['DBMS','DM'])
print(rohan.clg_fee)
print(tanmay.clg_fee)

rohan.change_fee(69000)
print(rohan.clg_fee)
print(tanmay.clg_fee)