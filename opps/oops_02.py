# method : method is the bunch of code that perform the intended task
# method are created by using the def keyword

class myClass:
    x = 0
    y = 0

    # creating a method called set
    def set(self , x ,y):
        self.x = x
        self.y = y
def main():
    vac = myClass()
    vac.set(5,6)

    print("X: "+ str(vac.x) +  ", Y: "+str(vac.y))

if __name__ == '__main__':
    main()
