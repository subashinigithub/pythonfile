""" class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
class student(person):
    pass
x=student("mike","olsen")
x.printname() """
""" class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
class student(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        person.__init__(self,fname,lname)
        self.graduationyear=2019
x=student("mike","olsen")
print(x.graduationyear)
x.printname() """

""" class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
x=student("mike","olsen",2019)
print(x.graduationyear)
 """
#multilvl inh
""" class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class college(person):
    def __init__(self,fname,lname,college):
        super().__init__(fname,lname)
        self.college=college
    def printn(self):
        print(self.firstname,self.lastname,self.college)
class student(college):
    def __init__(self, fname, lname,class1,degree):
        super().__init__(fname,lname,class1)
        self.degree=degree
mani=student("mani","kandan","abc","msc")
mani.printname()
mani.printn()
print(mani.degree)"""
#multilvl
class base1():
    def __init__(self):
        self.str1="a"
        print("base1")
class base2():
    def __init__(self):
        self.str2="b"
        print("base2")
class derived(base1,base2):
    def __init__(self):
        base1.__init__(self)
        base2.__init__(self)
        print("derived")
    def printstrs(self):
        print(self.str1,self.str2)
ob=derived()
ob.printstrs()
        
    






