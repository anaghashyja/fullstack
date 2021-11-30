dict0={2:"shyja",3:"rk",4:"kuchan"}
print(dict)

dict1=dict0.copy()
print(dict1)

print(dict0.get(4))

print(dict0.get(6,"key not found"))

print(dict0[2])

dict0[4]="grndpa"
print(dict0)

for x in dict0:
    print(x)

for x in dict0:
    print(dict0[x])

if 2 in dict0:
    print("available")

print(len(dict0))

dict0[4]="new"
print(dict0)

dict0.pop(2)
print(dict0)

dict0.popitem()
del dict0[3]
print(dict0)

mydic=dict(dict1)
print(mydic)

new=dict(a="car",b="world",c=2000)
print(new)

