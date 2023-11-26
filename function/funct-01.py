# function : is  a block of code that returns the specific task
# to create a function "def" keyword is used

def say_hi():
    return ('hi world')
print(say_hi())
# simplly calling the function

# function with parameter
def sum(num1,num2):
    sum = num1+num2
    return sum
print(sum(10,20))

# checking the prime number
def is_prime(n):
    # function to check the number is prime or not
    if n in [2,3]:
        return True
    if  n==1 or n%2==0:
        return False
    r = 3
    while r*r<=n:
        if n%r == 0:
            return False
        r+=2
    return True
        
print(is_prime(79) , is_prime(7), is_prime(12) , is_prime(69),is_prime(1),is_prime(2),is_prime(3))

# python function argument 
def even_odd(n):
    if n%2==0:
        return True
    else:
        return False
print(even_odd(1) , even_odd(3) , even_odd(12), even_odd(13))
    
''' type of argument 
    (1) Default arg  : A default argument is a parameter that assumes a default value if a
                          value is not provided in the function call for that argument. 
    (2) Keyword arg  : 
    (3) Positional arg
    (4) Arbitrary arg : In Python Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of 
                        arguments to a function using special symbols. There are two special symbols:
    '''

def default_arg(x , y = 50):
    print('x :' , x)
    print('y :' , y)
default_arg(10)

def keyword_arg(frist , last):
    print("the frist is :" , frist)
    print("the last is :" , last)
    print(frist + last)
keyword_arg(1 , 100)
keyword_arg('Mohd' , 'Alam')


def positional_arg(name , age):
    print('hi i am ', name, 'and my age is ', age)
    print('hi i am ', age, 'and my age is ' ,name)
positional_arg('nitin' , 30)
         

def arbitrary_arg(*argv):
    for avg in argv:
        print(avg)
arbitrary_arg('hi', 'my' , 'name' , 'is' , 'Ramesh')


def arb_kwargs(**kwargs):
    for key , value in kwargs.items():
        print("%s == %s"  % (key , value))
arb_kwargs(frist = 'hello' , second = 'world' , third = 'happy' , forth = 'learning' , fifth = 'python' , sixth = 3)

# 
# docstring : the frist line after the function that discribe the functionality of the function

def even_odd(n):
    """ function to check the number is even or not"""
    if n%2 == 0:
        return 'even'
    else:
        return 'odd'
print(even_odd.__doc__)

# nested function means function within function
def funct1():
    string1 = 'say hi to worls'
    def funct2():
        print(string1)
    funct2()
funct1()

def is_even(n):
    def check():
      if n%2 == 0:
        print('even')
      else:
          print('odd')
    check()    
            
is_even(4)
is_even(3)

