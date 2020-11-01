import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import PIL
from PIL import ImageTk, Image
import webbrowser
import string
#user/plice


class chose:
    def __init__(self, root):
        self.rootc = root
        self.rootc.title('User Type')
        self.rootc.geometry("1300x1300")
        
        self.bg_icon=tk.PhotoImage(file=r"images/check_bg.png")
        lb_bg=tk.Label(self.rootc,image=self.bg_icon,)
        lb_bg.place(x=0,y=0,relwidth=1,relheight=1)
        frame2=tk.Frame(self.rootc,bg="white")
        frame2.place(x=420,y=10)
        label3=tk.Label(self.rootc,text="REGISTERATION PAGE",font=("times new roman",40,"bold"),border=10,relief=tk.GROOVE,bg="yellow")
        label3.place(x=400,y=0)
        self.cont = tk.Frame(self.rootc, bg="white", height=300, width=800)
        self.cont.place(x=320, y=250)
        self.userbtn = tk.Button(self.cont, text="Register as a User", height=2, width=30, bg="#f56042", font=("Times New Roman", 11, "bold"))
        self.userbtn.place(x=250, y=50)
        self.branch = tk.Button(self.cont, text="Register your branch", height=2, width=30, bg="#f56042", font=("Times New Roman", 11, "bold") )
        self.branch.place(x=250, y=120)

root=tk.Tk()
obj_home = chose(root)
#obj=login_page(root)

root.mainloop()