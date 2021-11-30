class A:
    def get1(self):
        print("am A class")
class B:
    def get2(self):
        print("am B class")
class C(A,B):
    def put(self):
        print("yes am inherited A&B")
obj=C()
obj.get1()
obj.get2()
obj.put()

# obj=A()
# obj.get1()
# obj.get2()
# obj.put()
#
# obj=B()
# obj.get1()
# obj.get2()
# obj.put()



