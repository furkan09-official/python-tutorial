# incorrect python function
def func():
    pass
# we can use pass statement in while , if and else also

# returning multiple values from the function

# (1) using "class" method
class test:
    def __init__(self):
        self.str = 'learing python'
        self.x = 100
def func():
    return test()
print(func().str)
print(func().x)

class person:
    def __init__(self) :
        self.name = 'mayank'
        self.age = 20
        self.section = "A"
def func1():
    return person()

print(func1().name)
print(func1().age)
print(func1().section)

# (2) using tuple metho()

def func2():
    name = 'mayank'
    age = 20
    section = 'A'
    return name,age,section
print(func2())
# assigning returning tuple
name , age , section = func2()
print(name)
print(age)
print(section)

# returning values using list 
def func3():
    name = 'mayank'
    age = 20
    section = 'A'
    return [name , age , section]
print(func3())

# using dictionary
def func4():
    d = dict()
    d[str] = 'mayank'
    d[age] = 20
    return d
d  = func4()
print(d)

