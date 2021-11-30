from tkinter import *


t=Tk()
t.geometry('500x500')
Label(text='Name: ').place(x=10,y=10)
nm=Entry()
nm.place(x=55,y=12)


p = Image.open("C:\\Users\\AswinAnagha\\Desktop\\tkinter_regform\\background.jpg")
Label(text='age: ').place(x=10,y=35)
ag=Entry()
ag.place(x=55,y=37)    

def abcd():
    import pymysql
    x=pymysql.connect(host='localhost',user='root',password='asdlab',db='avodha')
    cur=x.cursor()
    n=nm.get()
    a=ag.get()
    cur.execute('insert into sample1 values(%s,%s)',(n,a))
    x.commit()
    x.close()
   

Button(text='submit',command=abcd).place(x=50,y=65)


Label(text='UPDATE',fg='red',bg='grey',font=('times new roman',10,'bold')).place(x=50,y=97)

Label(text='Enter  name to update: ',fg='white',bg='brown').place(x=5,y=130)
m=Entry()
m.place(x=140,y=130)


Label(text='Enter new age: ',fg='white',bg='brown').place(x=5,y=157)
z=Entry()
z.place(x=140, y=157)

def upd():
    import pymysql
    x=pymysql.connect(host='localhost',user='root',password='asdlab',db='avodha')
    cur=x.cursor()
    mw=m.get()
    zw=z.get()
    cur.execute('update sample1 set age=%s where name=%s',(zw,mw))
    x.commit()
    x.close()
    t.mainloop()

Button(text='Apply',command=upd).place(x=80,y=200)

t.mainloop()
