class stud:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getData(self):
        self.name=input("enter ur name")
        self.mark=input("enter ur mark")
    def putData(self):
        print(self.name,"\n",self.mark)
obj=stud('','')
obj.getData()
obj.putData()
