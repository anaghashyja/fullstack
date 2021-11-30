import tkinter
import tkinter.messagebox
from PIL import ImageTk, Image
from subprocess import call

t = tkinter.Tk()
t.title('college')
t.geometry('400x400')

p = Image.open("C:\\Users\\AswinAnagha\\Desktop\\tkinter_regform\\background.jpg")
p = p.resize((800, 800))
p = ImageTk.PhotoImage(p)

pic = tkinter.Label(t, image=p)
pic.place(x = 0, y=0)

a = tkinter.Label(text="KMCT CEW", bg="violet", fg="white", font=('bradely hand itc', 25, 'bold'))
a.place(x=233, y=0)

b = tkinter.Label(text="student name", bg="grey", fg="white", font=('bradely hand itc', 13, 'bold'))
b.place(x=50, y=100)

e = tkinter.Entry(width=30)
e.place(x=270, y=100)

c = tkinter.Label(text="department name", bg="grey", fg="white", font=('bradely hand itc', 13, 'bold'))
c.place(x=50, y=170)
f = tkinter.Entry(width=30)
f.place(x=270, y=170)


def abcd():
    name = e.get()
    department = f.get()

    if (name == "" or department == ""):
        tkinter.messagebox.showerror('error', 'plzz fill..')
    else:

        import pymysql
        x = pymysql.connect(host='localhost', user='root', password='asdlab', db='jasmine')
        cur = x.cursor()
        cur.execute("insert into college values('" + name + "','" + department + "')")
        x.commit()
        x.close()

        tkinter.messagebox.showinfo("thank u", 'successflly rgsterd')
        t.destroy()

        call(['python', 'new.py'])


k = tkinter.Button(text="submit", bg="orange", fg="black", font=('bradely hand itc', 18, 'bold'), command=abcd)
k.place(x=233, y=250)

t.mainloop()
