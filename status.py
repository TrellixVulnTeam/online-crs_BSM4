import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import PIL
from PIL import ImageTk, Image
import webbrowser
import string
class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, style = "Placeholder.TEntry", **kwargs)
        self.placeholder = placeholder
        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
    def _clear_placeholder(self, e):
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            self["style"] = "TEntry"
    def _add_placeholder(self,e):
        if not self.get():
            self.insert("0", self.placeholder)
            self["style"] = "Placeholder.TEntry"

class status:
    def __init__(self, root):
        self.rootstat = tk.Toplevel(root)
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dreamers29",
        database="crime_report")
        self.curs = self.mydb.cursor()
        self.search_var = tk.StringVar()
        self.rootstat.geometry("700x700")
        self.rootstat.configure(bg="#ddebc5")
        self.style = ttk.Style(self.rootstat)
        self.rootstat.title("Online Crime Branch")
        self.rootstat.iconbitmap('images/justice_logo.ico')
        self.crs_menu = tk.Menu(self.rootstat)
        self.rootstat.config(menu=self.crs_menu)
        self.file_menu = tk.Menu(self.crs_menu)
        self.crs_menu.add_cascade(label="File",menu=self.file_menu)

        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=self.rootstat.quit)

        self.image2 = Image.open('bg.jpg')
        self.image1 = ImageTk.PhotoImage(self.image2)
        
        self.logophoto = ImageTk.PhotoImage(Image.open('images/logo.png')) 
        self.labelText = tk.StringVar()


        self.label1 = tk.Label(self.rootstat, text="Check Complaint Status",
               font=("Times New Roman", 24),
               justify=tk.CENTER, fg="brown", bg="#ddebc5")

        self.label1.place(x=185, y=18)
        self.logolbl = tk.Label(self.rootstat, image=self.logophoto,justify=tk.CENTER, bg="#ddebc5", fg="white")
        self.logolbl.place(x=80, y=000)
        self.frame_srch = tk.Frame(self.rootstat, bg="#a86d32", height=300, width=600)
        self.frame_srch.place(x=40, y=150)
        self.searchphoto = ImageTk.PhotoImage(Image.open('images/search.png')) 
        self.locphoto = ImageTk.PhotoImage(Image.open('images/pin.png'))
        self.style.configure("Placeholder.TEntry", foreground="#8b8b8c")
        self.srch_in = PlaceholderEntry(self.frame_srch, "Enter complaint number", textvariable=self.search_var)
        self.srch_in.place(x=150, y=20, height=35, width=250)
        self.status = ''
        #logic
        self.search_btn = tk.Button(self.frame_srch, height=2, width=30, bg="#ede779", font=("Times New Roman", 11, "bold"), command=lambda: self.searchSttn())
        self.search_btn.place(x=405, y=20)
        self.search_btn.config(image=self.searchphoto,compound=tk.LEFT, width=30, height=30)
        #self.loc_btn = tk.Button(self.frame_srch, height=2, width=30, bg="#ede779", font=("Times New Roman", 11, "bold"))
        #self.loc_btn.place(x=540, y=20)
        #self.loc_btn.config(image=self.locphoto,compound=tk.LEFT, width=30, height=30)
    def searchSttn(self):
        cid = self.search_var.get()
        self.curs.execute("SELECT stat FROM complaints WHERE id=%(cid)s", {"cid":cid})
        self.res = self.curs.fetchone()
        if self.res:
            (st) = self.res
            self.status = st[0]

            self.frame_res = tk.Frame(self.rootstat, bg="#ede779", height=100, width=450)
            self.frame_res.place(x=90, y=260)
            self.ps = tk.Label(self.frame_res, text=self.status, bg="#ede779", font=("Times New Roman", 14, "bold"))
            self.ps.place(x=20, y=30)
        else:
            self.found = "No complaint found!"
            self.frame_res = tk.Frame(self.rootstat, bg="#ede779", height=300, width=350)
            self.frame_res.place(x=90, y=260)
            self.nf = tk.Label(self.frame_res, text=self.found, bg="#ede779", font=("Times New Roman", 14))
            self.nf.place(x=20, y=45)
root = tk.Tk()
obj = status(root)
root.mainloop()