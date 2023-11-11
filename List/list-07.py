# list comprehension : It is used to create a new list form other iterables like tuple , list , array etc...
# syntax : newList = [expression(element)for element in oldlist ifcondition]

# sqare of all odd numbers
newList = [x**2 for x in range(1,11) if x%2!=0]
print(newList)

# square of all the even number
newList1= [i**2 for i in range(1,101) if i%2==0]
print(newList1)