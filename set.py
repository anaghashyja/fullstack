# set1={"a","b","c","d"}
# print(set1)
#
# for i in set1:
#     print(i)
#
# print("b" in set1)
#
# set1.add("e")
# print(set1)
#
# set1.update(["f","g"])
# print(set1)
#
# print(len(set1))
#
# set2={"f","g","m"}
# set2.remove("g")
# set2.discard("m")
# print(set2)
#
# set3={"f","g","m"}
# set3.pop()
# print(set3)
#
# set2.clear()
# print(set2)

# set4={"f","g","m"}
# del set4
# print(set4)

#CONSTRUCTOR
# set5=set(("aa","bb","cc"))
# print(set5)

set0={"1","2","3"}
set9={"c","d"}
#set10=set0.union(set9)
set10=set0|set9
print(set10)

set9.update(set0)
print(set9)

seta={"1","5","9"}
setb={"5","2"}
# setz=setb-seta
setz=seta-setb
print(setz)

lis=[1,2,4,6,2]
print(set(lis))
t=(sorted(lis))
print(t[::-1])

