# remve element from the list by remove(value) method
List = [1,2,3,4,5,6,7,7]
List.remove(7)
List.remove(2)                            #remove method remove the first occurance of element 
print(List)                                 # remove method only remove one element at a time




# remove the range of element from the list usisg for loop
list = [1,2,3,4,5,6,7,8,9,0]
for i in range(0,len(list)):
    list.remove(i)
print(list)

# pop(index) method                         #by default pop()removes the last element of the list
list1 = [1,2,3,4,5,6]
list1.pop(4)
list1.pop(1)
print(list1)

list2 = [1,2,3,4,5,6,8]
i = 0
while(i<=len(list2)):
    list2.pop(i)
    i+=1
print(list2)