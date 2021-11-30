# from tkinter import *
# root=Tk()
# root.mainloop()

# from tkinter import *
# root=Tk()
# label1=Label(root,text="helloworld")
# label1.pack()
# root.mainloop()


# from tkinter import *
# root=Tk()
# label1=Label(root,text="helloworld")
# label2=Label(root,text="hai python")
# label1.pack()
# label2.pack()
# root.mainloop()

# OR

# from tkinter import *
# root=Tk()
# Label(root,text="helloworld").pack()
# Label(root,text="hai python").pack()
# root.mainloop()


# from tkinter import *
# root=Tk()
# Label(root,text="helloworld",bg="cyan").pack()
# Label(root,text="hai python",fg="red").pack()
# root.mainloop()



# BUTTON
# from tkinter import *
# root=Tk()
# Button(text="sign up",bg="cyan").pack()
# Button(text="logout",bg="red").pack()
# root.mainloop()

# from tkinter import *
# root=Tk()
# f=Frame(root)
# f.pack()
# def fun():
#     print("gd mng")
# def cancel():
#     print(" its cancelled")
#
# Button(text="sign up",bg="cyan",command=fun).pack()
# Button(text="logout",bg="red",command=cancel).pack()
# root.mainloop()



# TKINTER GRID

# from tkinter import *
# root=Tk()
#
# Label(root,text="username").grid(row=0,column=0)
# Label(root,text="password").grid(row=1,column=0)
# Entry(root).grid(row=0,column=1)
# Entry(root).grid(row=1,column=1)
#
# root.mainloop()



# SELF ADJASCENT WIDGET

# from tkinter import *
# root=Tk()
# Label(root,text="x direction",bg="cyan").pack(fill=X)
# Label(root,text="y direction",bg="yellow").pack(side=LEFT,fill=Y)
# root.mainloop()



# TKINTER CLASS

# from tkinter import *
# root=Tk()
# class demo():
#     def __init__(self,minnu):
#         frame=Frame(minnu)
#         frame.pack()
#         self.printmsg=Button(frame,text="hello",command=self.printmsg)
#         self.printmsg.pack()
#         Button(frame, text="exit",command=frame.quit).pack()
#     def printmsg(self):
#         print("helloo...mngzzz")
#
# obj=demo(root)
#
# root.mainloop()



