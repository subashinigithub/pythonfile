'''data=[1,2,3,4,5,6]
new=map(lambda x:x+2,data)
print(list(new))

new1=filter(lambda x:x%2==0,data)
print(list(new1))
def x(a):
    return a+20
print(x(5))

x=lambda a:a+20
print(x(5))
x=lambda a,b:a*b
print(x(5,6))

def myfunc(n):
    return lambda a:a*n
m=myfunc(2)
print(m(11))
print(m(46))

#class
class c1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("this is function")
    def func1(self):
        print(self.name,self.age)

c=c1("ramesh",45)
c.func1()
print(c.age)'''
""" class employee:
    def __init__(self,name,age,salary):
        self.name=name 
        self.age=age
        self.salary=salary
        print("salary is increase in monthly")
    def read(self):
        print(self.name,self.age,self.salary)
    def __str__(self):
        return str(self.name)
obj=employee("rajam",22,100000)
obj.read()
print(obj) """
""" class student:
    def __init__(self,name,age,course,Dob):
        self.name=name
        self.age=age
        self.course=course
        self.Dob=Dob
        print("Student Details")
    def read(self):
        print(self.name,self.Dob)
    def __str__(self):
        return str(self.Dob)
mock=student("suba",24,"cs",2906)
mock.read()
print(mock) """
