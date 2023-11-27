#  class method vs static method

# class method
class person:
    def __init__(self , value):
        self.value = value
    def get_value(self):
        return self.value
obj = person('ramesh')
print(obj.get_value())


# class method
class class1:
    
    def __init__(self,name , roll_no):
        self.name = name
        self.roll_no = roll_no
    def get_data(self):
        return self.name , self.roll_no
    # test case 01
obj1 = class1('ramesh',12)
print(obj1.get_data())
#    test case 02
obj1 = class1('suresh',15)
print(obj1.get_data())
#  teat case 03
obj1 = class1('mukesh',10)
print(obj1.get_data())

# static method
class my_class:
    def __init__(self , value):
        self.value = value
    @staticmethod
    def get_max(x , y):
        return max(x,y)
obj2 = my_class(10)
print(my_class.get_max(20,50))
print(my_class.get_max(300 , 60))
          
# program to find the factorial of a given number using static metohd
class factorial:
    def __init(self , value):
        self.value = value
    def the_factorial(n):
        if n == 0 | n == 1:
            return 1
        else:
            return n*factorial.the_factorial(n-1)
        # the test case 01 
result = factorial.the_factorial(50)
print("the factorial of 50: ", result)
