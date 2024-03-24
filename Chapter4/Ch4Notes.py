print("Chapter 4 second run through\n")

'''
# pg 122
def outer():
    test = 1  # outer scope
    def inner():
        test=2  #  inner scope
        print('inner:', test)
    inner()
    print('outer:', test)

print("Standard scoping")
test = 0   #  Global scope
outer()
print('global:', test)
print("\n")



# pg 123
def outer():
    test = 1  # outer scope
    def inner():
        nonlocal test
        test=2  #  inner scope
        print('inner:', test)
    inner()
    print('outer:', test, "Notice 'outer' now gets the 'inner' value.")
print("Here we have 'nonlocal test' command inside inner()")
test = 0   #  Global scope
outer()
print('global:', test)
print("\n")


# pg 124
def outer():
    #global test
    test = 1  # outer scope
    def inner():
        #global test
        nonlocal test
        test=2  #  inner scope
        print('inner:', test)
    inner()
    print('outer:', test)
print("Here we have 'global test' command inside inner()")
test = 0   #  Global scope
outer()
print('global:', test, "Notice that 'global' now gets the 'inner' value.")
print("\n")



x=[1,2,3]
def func(y):
    y[1] += 42
    y = 'Something Else'
    print(y, "This is inside the function")
    

print(x, "This is X before calling func()")
func(x)
print(x, "This is X after calling func()")
func(x)
print(x, "This is X after calling func() a second time")


def func(a, b, c):
    print("In func() ", a, b, c)

func(1,2,3)
a=11
b=22
c=33
func(a=a, c=c, b=b)

myIter = (444,555)
func(*myIter,123)

myDict = { 'b': 1111, 'c': 2222, 'a': 3333}
func(**myDict)


# This is part of the programming assignment from Reliable Robotics  Kayla VanderPutten
class A:
    def __init__(self):
        self.x = 10
        self.y = 100

class B(A):
    def __init__(self, x:int):
        self.x = x
        super().__init__()

a = A()
b = B(100)

print(a.x, " Here is first line")
print(b.x, "  Here is second line")
'''

def func(a,b,c,d,e,f):
    print(a,b,c,d,e,f)

func(1, *(2,3), f=6, *(4,5))
func(*(1,2), e=5, *(3,4),f=6)
func(1, **{'b':2, 'c':3}, d=4, **{'e':5, 'f':6})
func(c=3, *(1,2),**{'d':4},e=5, **{'f':6})
print("")
func(1, **{'b':2, 'c':3}, **{'e':5, 'f':6} , d=4)
func(f=6,e=5,*(1,2),  *(3,4))
# func(f=6,e=5,  *(3,4),*(1,2))  # did 3 4 1 2 5 6
func(c=3, *(1,2), **{'f':6},e=5,**{'d':4})
# func(c=3, **{'f':6},e=5,**{'d':4}, *(1,2))  # SyntaxError: iterable argument unpacking follows keyword argument unpacking

print("\n\nEnd of exercise")
