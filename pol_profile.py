import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import PIL
from PIL import ImageTk, Image
import webbrowser
import string

class pol_prof:
    def __init__(self, root):

        self.rootp = tk.Toplevel(root)
        self.rootp.title("Branch Status")
        self.rootp.geometry('1350x1000+0+0')
        self.rootp.iconbitmap('images/justice_logo.ico')

        #self.rootp.configure(background = "grey")
        self.bg_icon=tk.PhotoImage(file=r"images/check_bg.png")
        self.lb_bg=tk.Label(self.rootp,image=self.bg_icon,)
        self.lb_bg.place(x=0,y=0,relwidth=1,relheight=1)
        self.label3=tk.Label(self.rootp,text="Check Your Branch",font=("times new roman",40,"bold"),border=10,relief=tk.GROOVE,bg="yellow")
        self.label3.place(x=450,y=0)
        self.cont = tk.Frame(self.rootp, bg="white", height=460, width=1000)
        self.cont.place(x=200, y=200)
        self.p =   ImageTk.PhotoImage(Image.open('images/police_badge.png')) 
        self.plabel = tk.Label(self.cont, image=self.p, compound=tk.LEFT)
        self.plabel.place(x=-2, y=-2)
        self.pname = tk.Label(self.cont, text="Name", font=("times new roman",20), bg="white")
        self.pname.place(x=635, y=10)
        self.add = tk.Label(self.cont, text="Address: ", font=("times new roman",15, "bold"), bg="white")
        self.add.place(x=515, y=100)
        self.padd = tk.Label(self.cont, text="Sushant Lok, Gurgaon, 122002", font=("times new roman",15), bg="white")
        self.padd.place(x=600, y=100)
        self.state = tk.Label(self.cont, text="State: ", font=("times new roman",15, "bold"), bg="white")
        self.state.place(x=515, y=160)
        self.pstate = tk.Label(self.cont, text="Haryana", font=("times new roman",15), bg="white")
        self.pstate.place(x=580, y=160)
        self.jd = tk.Label(self.cont, text="Jurisdiction: ", font=("times new roman",15, "bold"), bg="white")
        self.jd.place(x=515, y=210)
        self.pjd = tk.Label(self.cont, text="Gurgaon, Sushant Lok 1, Sector-43", font=("times new roman",12), bg="white")
        self.pjd.place(x=625, y=213)
        self.des = tk.Label(self.cont, text="Designation : ", font=("times new roman",15, "bold"), bg="white")
        self.des.place(x=515, y=270)
        self.pdes = tk.Label(self.cont, text="DCP", font=("times new roman",15), bg="white")
        self.pdes.place(x=650, y=270)
        self.ctt = tk.Label(self.cont, text="Contact : ", font=("times new roman",15, "bold"), bg="white")
        self.ctt.place(x=515, y=330)
        self.pctt = tk.Label(self.cont, text="0124-66448822", font=("times new roman",15), bg="white")
        self.pctt.place(x=610, y=330)
        self.em = tk.Label(self.cont, text="Email Id : ", font=("times new roman",15, "bold"), bg="white")
        self.em.place(x=515, y=390)
        self.pem = tk.Label(self.cont, text="police@gmail.com", font=("times new roman",15), bg="white")
        self.pem.place(x=610, y=390)





root = tk.Tk()
obj = pol_prof(root)
root.mainloop()
