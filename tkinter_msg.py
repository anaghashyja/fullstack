# TKINTER MSG BOX

from tkinter import *
import tkinter.messagebox

root = Tk()

# tkinter.messagebox.showinfo("title","this is information")
# root.mainloop()

# tkinter.messagebox.showerror("title","error....")
# root.mainloop()

# tkinter.messagebox.showwarning("rose","this is a warning")
# root.mainloop()

# tkinter.messagebox.askquestion("title","r u ready")
# root.mainloop()

# tkinter.messagebox.askokcancel("title","r u ready")
# root.mainloop()

# tkinter.messagebox.askyesno("title","r u ready")
# root.mainloop()

tkinter.messagebox.askretrycancel("title", "continue....")
root.mainloop()
