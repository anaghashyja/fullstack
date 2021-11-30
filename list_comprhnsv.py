# def square():
#     for i in range(10):
#         print(i*i)
# square()

#is in smple syntx

li=[i*i for i in range(10)]
print(li)

letters=[]
for i in "anagha":
    letters.append(i)
print(letters)

letters=[i for i in "anagha"]
print(letters)

even=[]
for i in range(10):
    if i%2==0:
        even.append(i)
print(even)

even=[i for i in range(20)if i%2==0]
print(even)


list=[1,4,5,8]
even=[i**2for i in list if i%2==0]
print(even)