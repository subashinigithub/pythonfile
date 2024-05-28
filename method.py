""" from math import pi 
class shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
    def fact(self):
        return "I am a two-dimensional shape"
    def __str__(self):
        return self.name
class square(shape):
    def __init__(self,length):
        super().__init__("square")
        self.length=length
    def area(self):
        return self.length**2
    def fact(self):
        return "squares have each angle equal to 90 degrees."
class circle(shape):
    def __init__(self,radius):
        super().__init__("circle")
        self.radius=radius
    def area(self):
            return pi*(self.radius**2)
a=square(4)
b=circle(7)
print(a)
print(a.area())
print(a.fact())
print(b)
print(b.fact())
print(b.area()) """
""" from abc import ABC, abstractmethod
class Bank(ABC):
    def bank_info(self):
        print("welcome to bank")
    @abstractmethod
    def interest(self):
        pass
#subclass/child class of abstractclass
class SBI(Bank):
    def interest(self):
        print("5 percentage")
s=SBI()
s.bank_info()
s.interest()

 """
from abc import ABC,abstractmethod
class Bank(ABC):
    def bank_info(self):
        print("welcome to bank")
    @abstractmethod
    def interest(self):
        pass
class SBI(Bank):
    def balance(self):
        print("balance is 100")
class Sub1(SBI):
    def interest(self):
        print("in sbi bank interest in 5 rupees")
s=Sub1()
s.bank_info()
s.balance()
s.interest()
