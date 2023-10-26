#  deletion of a character form the string

string = "I am very very hungry"
# del string[0]    showes an error
# del string
# print(string)

string1 = string[0:2] + string[4::]
print(string1)

greeting = 'Happy birthday to you tum jio hazaro saal saal me din ho -1'
list = list(greeting)
for i in list:
    if(i%2==0):
        print(i)
