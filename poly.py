class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a cat.my name is {self.name}.I am {self.age}years old.")
    def make_sound(self):
        print("meow")
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a dog.my name is {self.name}.I am {self.age}years old.")
    def make_sound(self):
        print("bark")

cat1=cat("kitty",2)
dog1=dog("fluffy",4)
for animal in(cat1,dog1):
    animal.make_sound()
    animal.info()