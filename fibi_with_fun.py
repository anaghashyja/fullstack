#FIBINACII SEQUENCE
n=int(input('Enter no of terms: '))   
def fib(x):
    x1=0
    x2=1

    c=0

    if(x<=0):
          print('plz input a valid value')
    elif(x==1):
                print('fibonacci series',x2)
    else:
                print('FIBONACCI  SEQUENCE\n----------------------------------------')
                while c<x:
                         print(x1,end=' ')
                         n=x1+x2
                         x1=x2
                         x2=n 
                         c+=1
            
fib(n)
