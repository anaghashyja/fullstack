# from tkinter import *
# root=Tk()
#
#
# mymenu=Menu(root)
# root.config(menu=mymenu)
#
# submenu=Menu(root)
#
# mymenu.add_cascade(label="File",menu=submenu)
# submenu.add_command(label="save")
# submenu.add_separator()
# submenu.add_command(label="exit")
#
# newmenu=Menu(mymenu)
# mymenu.add_cascade(label="edit",menu=newmenu)
# mymenu.add_command(label="undo")
# mymenu.add_command(label="redo")
#
#
# root.mainloop()



from tkinter import *
root=Tk()
def fun():
    print("am saved")


mymenu=Menu(root)
root.config(menu=mymenu)

submenu=Menu(root)

mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="save",command=fun)
submenu.add_separator()
submenu.add_command(label="exit",command=root.quit)

newmenu=Menu(mymenu)
mymenu.add_cascade(label="edit",menu=newmenu)
mymenu.add_command(label="undo",command=fun)
mymenu.add_command(label="redo",command=fun)


root.mainloop()




