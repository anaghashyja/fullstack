def fun(a):
    print(a+2)
fun(3)

x=lambda a:a+2
print(x(8))

x=lambda a,b:a*b
print(x(5,10))

x=lambda a,b:a*b+100
print(x(5,10))

x=lambda a,b,c:a*b+100+c
print(x(5,10,50))

def mul(n):
    return lambda a:a*n
num1=mul(15)
print(num1(2))

num2=mul(10)
print(num2(8))