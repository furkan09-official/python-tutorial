# deletion/ updation from the string
# the updstion and deletion form the string is not allowed because in python string are immutable

# updation of a character (1) usign list converrsion   (2) usign slicing method

string1 = 'hello i am student'
print(string1)
list1 = list(string1)
list1[1] = 'p'
print("".join(list1))

string3 = string1[0:2] + "p" + string1[3::]
print(string3)

string4 = string1[0:5] + " hi " + string1[6::]
print(string4)

# updating the whole string by assiging that string to a new string

string = "Ram is a good boy"
print('intial string :' , string)

string = " The Ram is a mahapurush"
print("updates string :" , string)
