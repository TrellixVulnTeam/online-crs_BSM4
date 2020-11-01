import tkinter as tk
import PIL
from PIL import ImageTk, Image
from tkinter import ttk
import mysql.connector
import string

#string to array
def stAr(arr):
    arrx = arr.split(',')
    return arrx
#string comparison
def comp(a, b):
    return [c for c in a if c.isalpha()] == [c for c in b if c.isalpha()]



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


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 5
        y = y + cy + self.widget.winfo_rooty() +7
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "10", "normal"))
        label.place(x=0,y=0)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
#connect to db
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Dreamers29",
database="crime_report")
curs = mydb.cursor()

root = tk.Tk()

search_var = tk.StringVar()

root.geometry("400x400")
root.configure(bg="#ddebc5")
style = ttk.Style(root)
root.title("Online Crime Branch")
root.iconbitmap('images/justice_logo.ico')
crs_menu = tk.Menu(root)
root.config(menu=crs_menu)
file_menu = tk.Menu(crs_menu)
crs_menu.add_cascade(label="File",menu=file_menu)

file_menu.add_separator()
file_menu.add_command(label="Quit", command=root.quit)

image2 = Image.open('bg.jpg')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
root.geometry('%dx%d+0+0' % (w,h))
logophoto = ImageTk.PhotoImage(Image.open('images/logo.png')) 
labelText = tk.StringVar()


label1 = tk.Label(root, text="Know Your Police Station",
               font=("Times New Roman", 24),
               justify=tk.CENTER, fg="brown", bg="#ddebc5")

label1.place(x=555, y=18)
logolbl = tk.Label(root, image=logophoto,justify=tk.CENTER, bg="#ddebc5", fg="white")
logolbl.place(x=460, y=000)
frame_srch = tk.Frame(root, bg="#a86d32", height=600, width=800)
frame_srch.place(x=300, y=150)


searchphoto = ImageTk.PhotoImage(Image.open('images/search.png')) 
reportphoto = ImageTk.PhotoImage(Image.open('images/report.png')) 
accphoto =   ImageTk.PhotoImage(Image.open('images/acc.png')) 
hlphoto =   ImageTk.PhotoImage(Image.open('images/hl.png')) 
locphoto = ImageTk.PhotoImage(Image.open('images/pin.png'))
style.configure("Placeholder.TEntry", foreground="#8b8b8c")

#srch_in = tk.Entry(root)
srch_in = PlaceholderEntry(frame_srch, "Enter your location", textvariable=search_var)
srch_in.place(x=230, y=20, height=35, width=250)
#logic
res_dict = {
    "pid": -1,
    "sttn_name":"",
    "dist":"",
    "city":"",
    "state":"",
    "pc":"",
    "des":"",
    "contact": "",
    "email":""
}
found = ""

jdbool = False
def searchSttn():
    jd=""
    num = -1
    global jdbool
    global found
    loc_db = search_var.get()
    print(loc_db)
    curs.execute("SELECT * FROM stations")
    res = curs.fetchall()
    n = len(res)
    for i in range(0,n):
        (result) = res[i]
        jd = stAr(result[6])
        for c in jd:
            print(c, loc_db)
            if comp(loc_db, c):
                num = i
                print(num)
                jdbool = True
                print("found")
                break
    if jdbool:
        (result) = res[num]
        global res_dict
        res_dict["pid"] = result[0]
        res_dict["sttn_name"] = result[1]
        res_dict["dist"]  = result[2]
        res_dict["city"] = result[3]
        res_dict["state"] = result[4]
        res_dict["pc"] = result[5]
        curs.execute("SELECT * FROM sttn_contact WHERE pid=%(pid)s",{'pid':res_dict["pid"]})
        res_ctt = curs.fetchone()
        (res_x) = res_ctt
        print(res_x)
        res_dict["des"] = res_x[3]
        res_dict["contact"] = res_x[2]
        res_dict["email"] = res_x[4]
        address = res_dict["dist"] + ", " + res_dict["city"] + ", " + res_dict["state"] 
        frame_res = tk.Frame(root, bg="#ede779", height=300, width=450)
        frame_res.place(x=480, y=300)
        ps = tk.Label(frame_res, text=res_dict["sttn_name"], bg="#ede779", font=("Times New Roman", 14, "bold"))
        ps.place(x=20, y=45)
        add = tk.Label(frame_res, text=address, bg="#ede779", font=("Times New Roman", 12) )
        add.place(x=20, y=80)
        contact = tk.Label(frame_res, text=res_dict["contact"], bg="#ede779", font=("Times New Roman", 12))
        contact.place(x=20, y=105)
        email = tk.Label(frame_res, text=res_dict["email"], bg="#ede779", font=("Times New Roman", 12) )
        email.place(x=20, y=130)
        designation  = tk.Label(frame_res, text=res_dict["des"], bg="#ede779", font=("Times New Roman", 12))
        designation.place(x=20, y=155)
    else:
        found = "No nearby police station found!"
        frame_res = tk.Frame(root, bg="#ede779", height=400, width=350)
        frame_res.place(x=400, y=300)
        nf = tk.Label(frame_res, text=found, bg="#ede779", font=("Times New Roman", 14))
        nf.place(x=20, y=45)


search_btn = tk.Button(frame_srch, height=2, width=30, bg="#ede779", font=("Times New Roman", 11, "bold"), command=lambda: searchSttn())
search_btn.place(x=490, y=20)
search_btn.config(image=searchphoto,compound=tk.LEFT, width=30, height=30)
loc_btn = tk.Button(frame_srch, height=2, width=30, bg="#ede779", font=("Times New Roman", 11, "bold"))
loc_btn.place(x=540, y=20)
loc_btn.config(image=locphoto,compound=tk.LEFT, width=30, height=30)

    

    

#crime_stats = tk.Label(frame_srch, text="Crime Stats Of India", justify=tk.CENTER, fg="white", bg="#a86d32", font=("Times New Roman", 14, "bold"))
#crime_stats.place(x=195, y=15)

#canva = tk.Canvas(root, width=400, height=300,borderwidth=1)
#canva.place()
#canva.create_image(image=map_img)
root.mainloop()