# Adding the elements to the python list
list =[]
print(list)
list.append(1)
list.append(2)
list.append(3)
print(list)

# we cannot add multiple elements at a time
# list.append(1,2)
# but using loop we can
n= int(input('enter the size of list :'))
list1 =[]
while n>0:
    list1.append(n)
    n-= 1
print(list1)


# using for loop
for i in range(0,n):
    list1.append(i)
print(list1)

# append the tuple in list
list2 = []
list2.append((2,3,4,1))
print(list2)
                                                # note: append() and extend() can add element at the end
# 
# Adding the list and tuple in list
list2 =[]
list3 =['happy' , 'birthday']
tuple = ('12/20/2002')
list2.append(list3)
list2.append(tuple)
list2.append([list3 , tuple])
print(list2)

list2.append((list3 , tuple))
print(list2)

# list2.append({list3 , tuple})
# print(list2)

# using the incert method(position , value)
list4 = [2,4,6,8]
list4.insert(4,10)
list4.insert(5,'John banega Don')
print(list4)

# using the extend() method
list5 =[2,3,4]
list5.extend(4)
list5.extend('chingum ke changul se bachna muskil hai')
print(list5)