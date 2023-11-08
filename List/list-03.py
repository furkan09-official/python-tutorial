#  taking the input of a python list
# number = input('enter the list elements as integers:')
# list = number.split()
# print(list)


# string = input('enter the string:')
# list  = string.split()
# print(list)

# number1 = input(':')
# list1 = number1.strip().split()
# print(list1)

# getting the list as an user input

# creating a empty list
list = []
# taking the range of list fronm user
n = int(input("enter the size of list :"))

for i in range(0, n):
    element = int(input())
    list.append(element)
print(list)
