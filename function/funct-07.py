#  *args and **kargs  in python
def fun(*args):
    for i in args:
        print(i)

fun('hello' , 'wellcome' , 'to' , 'jungle')

def funct(*str):
    str_list = []
    for i in str:
        str_list.append(i)
    return str_list
result = funct('hello', 'wellcome' , 'to', 'jungle')
print(result)

        

def funct1(**kwargs):
    for key , value in kwargs.items():
        print("%s == %s" % (key , value))
funct1(frist = 'hello', mid = 'jack' ,last = 'morghan' )