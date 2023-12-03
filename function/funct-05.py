# python function are first class objects
def shout(text):
    return text.upper()
print(shout('hello'))
# assigning a function to a variable yell
# this assignment dosen't call the function it takes the function object reffered by shout
yell = shout
print(yell('Hello'))


# function can be passed as an argument to another function
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()
def greet(func):
    greeting = func('hi! good morning')
    print(greeting)

greet(shout)
greet(whisper)

# function can return another function
def create_adder(x):
    def adder(y):
        return x + y
    return adder
add_10 = create_adder(40)
print(add_10(10))
