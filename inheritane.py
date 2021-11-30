# class csstud:
#     def __init__(self,name):
#         self.name=name
#     def getData(self):
#         self.name=input("enter the  ur  name")
#
# class hod(csstud):
#     def __init__(self,hodname):
#         self.hodname=hodname
#     def putData(self):
#         self.hodname=input("enter hod name")
#     def display(self):
#         print("cs stud name is",self.name)
#         print("cs hod name is",self.hodname)
# obj=hod("")
# obj.getData()
# obj.putData()
# obj.display()



class csstud:
    def __init__(self,name,hodname):
        self.name=name
        self.hodname = hodname
    def getData(self):
        self.name=input("enter the  ur  name")

class hod(csstud):


    def putData(self):
        self.hodname=input("enter hod name")
    def display(self):
        print("cs stud name is",self.name)
        print("cs hod name is",self.hodname)
obj=hod("","")
obj.getData()
obj.putData()
obj.display()
