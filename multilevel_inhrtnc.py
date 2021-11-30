class A:
    def __init__(self,name,hodname):
        self.name=name
        self.hodname = hodname
    def getData(self):
        self.name=input("enter the  ur  name")

class B(A):


    def putData(self):
        self.hodname=input("enter hod name")
    def display(self):
        print("cs stud name is",self.name)
        print("cs hod name is",self.hodname)

class C(B):
    def fun3(self):
        print("thi is c class")

class D(C):
    def fun4(self):
        print("thi is D class")

obj=D("","")
obj.getData()
obj.putData()
obj.display()
obj.fun3()
obj.fun4()