# Adding the new element into set buy using the built in add() function
# Note : list can not be added to set because list are mutable but tuple can be added because tuple are immutabl

set1 ={1,2,3,4}
set1.add(5)
# set.add('six' , 'seven')         add takes only one arguement at a time
set1.add('six')
set1.add((6,7))           #adding a tuple 
print(set1)

# adding the multiple elements at a time using loop
set2 = {1,2,3}
for i in range(1,6):
    set2.add(i)
print(set2)

# Adding multiple element at a time using update() method
# the update method accept the list , string , tuple as well as other set as an argument
set3 = set([1,2,3,4,(4,5)])
set3.update([5,7])
print(set3)