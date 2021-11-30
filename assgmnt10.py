class laptop:
    def getspec1(self):
        print("laptop class")
class desktop:
    def getspec2(self):
        print("desktop class")
class Computer(laptop,desktop):
    def displayspec(self):
        print("laptop is wieghtless and easy to carry.....\n desktops have heavy weight so, it doesn't carry easy")
obj=Computer()
obj.getspec1()
obj.getspec2()
obj.displayspec()
