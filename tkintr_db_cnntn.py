from tkinter import *
import pymysql
x=pymysql.connect(host='localhost',user='root',password='asdlab',db='avodha')
cur=x.cursor()
t=Tk()
nm=Entry()
Label(text='Name:').place(x=10,y=10)
nm.place(x=55,y=12)

Label(text='age: ').place(x=10,y=35)
ag=Entry()
ag.place(x=55,y=37)    

def abcd():
    n=nm.get()
    a=ag.get()
    cur.execute('insert into sample1 values(%s,%s)',(n,a))
    x.commit()
    x.close()
    t.destroy()

Button(text='submit',command=abcd).place(x=40,y=65)
t.mainloop()
