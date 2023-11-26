# anonymous function : the function without a name
# lambda keyword is used to create a anonymous function
# Note : This function can have any number of arguments but only one expression, which is evaluated and returned.
name_1 = lambda : 'landon , new York '
print(name_1())

is_even = lambda x: "even " if x%2 == 0 else 'odd'
print(is_even(4))
print(is_even(5))

area_of_tringle = lambda base , height: (1/2*base*height) 
# test case 01
print(area_of_tringle(2,3))
# test case 02
print(area_of_tringle(5,4))
# test ace 03
print(area_of_tringle(0,10))

# pass by value , pass by reference
def my_function(x):
    x[0] = 100
    return x
x = [1,40,60,80,100]
my_function(x)
print(my_function(x))


def funct1(x):
    # the path between passed and received is broken
    x = 30
x = 10
funct1(x)
print(x)


def funct2(x):
    x = 30
    return x
x = 10
funct2(x)
print(x)