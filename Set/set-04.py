# removing the items from set using the built in remove() method
set1 = set([1,2,3,4,'up' , 'bihar' , 'mp'])
set1.remove('bihar')
set1.remove(3)
print(set1)

set2 = set([1,2,3,4,5,6])
for i in range(1,4):
    set2.remove(i)
print(set2)

set3 = set([9,8,7,6,5])
for i in range(1,4):
    set3.discard(i)    #discard() does not show an error if we want to remove the element for the set which is not present but remove does 
print(set3)

# using the pop() method
set4 = set((1,2,3,4,5))
set4.pop()     #if set is unordered then there is no way to determine which element is poped 
print(set4)

set5 = set([1,2,3,4,5])
set5.pop()
print(set5)

# to remove all the eleement form the set clear() method is used
set6 = set([10,20,30,40])
set6.clear()
print(set6)