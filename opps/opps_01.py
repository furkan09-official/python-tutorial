# creating the class 
class myClass:
    name = 'name'
    roll_no = 0
# creating an object for myClass
def main():
    me = myClass()

# accessing the attributes of myclass using the (.) operator

    me.name = 'Rahul'
    me.roll_no = 120

    me.name = 'mukesh'
    me.roll_no = 121
    print(me.name + " " + str(me.roll_no))
    

# telling python that there is main in program
if __name__ == '__main__':
    main()

