t=("mom","dad","bro","grndpa")
print(t)
print(type(t))
print(t[1])
print(t[-1])

#convert to tuple for append() like opeartions and convert back to tuple
y=list(t)
y[2]="muthu"
t=tuple(y)
print(t)
print(type(t))

for i in t:
    print(i)
if "dad" in t:
    print("yes")
print(len(t))

t1=("i","love","u")
t3=t+t1
print(t3)

t0=(1,2,3,3,3,3,4,4,5,5,6)
print(t0.count(5))








