# using *args an **kwargs in python to set the value of object
# *args receives the argument as tuple
# **kwargs receives the argument as dictonary


# (1) Using *args
class car :
    
    def __init__(self, *args):
        self.speed = args[0]
        self.color = args[1]

# creating objects of car class
audi = car(300 , 'Red')
BMW = car(150 , 'Black')
creata = car(200 , 'white')

# printing the color and speed of car
print(audi.color)
print(audi.speed)
print(creata.speed)
print(creata.color)

# (2) Using **kwargs
# creating the class of car
class car:
    def __init__(self,**kwargs):
        self.speed = kwargs['s']
        self.color =kwargs ['c']
# creating a object of class car    
audi = car(s = 200 , c = 'Red')
BMW = car(s = 200 , c = 'Yellow')
City = car(s = 250 , c = 'Black')
print(audi.speed)
print(BMW.color)
print(City.speed)

class employee:
    def __init__(self,*args):
        self.frist_name = args[0]
        self.last_name = args[1]
        self.salary = args[2]

employee1 = employee('johnny' , 'depp' , 5000)
employee2 = employee('ramesh' , 'mathur' , 5000)
employee3 = employee('foolchand' , 'tripathi' , 6000)
employee4 = employee('bablu' , 'pandit' , 500)
employee5 = employee('sweaty' , 'gupta' , 2000)

print(employee1.salary)
print(employee2.frist_name)
print(employee3.last_name)
print(employee4.salary)
print(employee5.last_name)