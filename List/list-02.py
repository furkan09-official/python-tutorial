# accessing the list elements 
list = [10,20,30,40,50]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

# Accessing the elements using for loop
# for i in list:
#     print(list[i])

# accessing the nested list
list1 = [['China'] ,['India'] ,['USA'] ,['Landon']]
print(list1[3])

list2 =[[1,2,3] , ['A','B','C'], [12,14,20]]
print(list2[0][2])
print(list2[1][0])
print(list2[2][2])

# Accessing the elements using the nested for loop
for i in range(len(list2)):
    for j in range(len(list2)):
        print(list2[i][j])
