""" def greet(name):
    def display_name():
        print("hi",name)
    display_name()
greet("raja")
 """
# decorators
'''
def func(x):
    x("just print")
func(input)'''


def outer(x):
    def inner(y):
        return x+y
    return inner
x=outer(2)
y=x(2)
print(y)