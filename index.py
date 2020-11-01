import tkinter as tk
import PIL
from PIL import ImageTk, Image
import webbrowser
url = 'try.html'

def OpenUrl(url):
    webbrowser.open_new(url)
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
root = tk.Tk()
root.geometry("400x400")
root.configure(bg="#ddebc5")
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


label1 = tk.Label(root, text="Online Crime Branch India",
               font=("Times New Roman", 24),
               justify=tk.CENTER, fg="brown", bg="#ddebc5")

label1.place(x=555, y=18)
logolbl = tk.Label(root, image=logophoto,justify=tk.CENTER, bg="#ddebc5", fg="white")
logolbl.place(x=460, y=000)
frame_btn = tk.Frame(root, bg="#a86d32", height=400, width=500)
frame_btn.place(x=140, y=200)
frame_map = tk.Frame(root, bg="#a86d32", height=550, width=550)
frame_map.place(x=850, y=150)
searchphoto = ImageTk.PhotoImage(Image.open('images/search.png')) 
reportphoto = ImageTk.PhotoImage(Image.open('images/report.png')) 
accphoto =   ImageTk.PhotoImage(Image.open('images/acc.png')) 
hlphoto =   ImageTk.PhotoImage(Image.open('images/hl.png')) 

reportbtn = tk.Button(frame_btn,text="   Report Crime", height=2, width=30,bg="#ede779", font=("Times New Roman",11, "bold"))
reportbtn.place(x=40, y=80)
reportbtn.config(image=reportphoto,compound=tk.LEFT, width=400, height=30)

helpline_btn = tk.Button(frame_btn, text="  Launch Helpline", height=2, width=30, bg="#ede779", font=("Times New Roman",11, "bold"))
helpline_btn.place(x=40, y=140)
helpline_btn.config(image=hlphoto,compound=tk.LEFT, width=400, height=30)
acc_btn = tk.Button(frame_btn, text="   Login/Signup", height=2, width=30, bg="#ede779", font=("Times New Roman", 11, "bold"))
acc_btn.place(x=40, y=200)
acc_btn.config(image=accphoto,compound=tk.LEFT, width=400, height=30)

search_btn = tk.Button(frame_btn, text="  Find Nearest Branch", height=2, width=30, bg="#ede779", font=("Times New Roman", 11, "bold"))
search_btn.place(x=40, y=250)
search_btn.config(image=searchphoto,compound=tk.LEFT, width=400, height=30)

crime_stats = tk.Label(frame_map, text="Crime Stats Of India", justify=tk.CENTER, fg="white", bg="#a86d32", font=("Times New Roman", 14, "bold"))
crime_stats.place(x=195, y=15)
map_img = ImageTk.PhotoImage(Image.open("images/map_crime.jpg"))
map_button = tk.Button(frame_map, image=map_img, compound='center', borderwidth=0, bg="#ede779", fg="#ede779", command=lambda aurl=url:OpenUrl(aurl))
map_lbl = tk.Label(frame_map, image=map_img,justify = tk.CENTER, width=400, compound='center', bg="#ede779", fg="#ede779")
map_button.place(x=50,y=40)
CreateToolTip(map_button, text = 'Click to view detailed \n'' crime rate statistics of \n''India..')
#canva = tk.Canvas(root, width=400, height=300,borderwidth=1)
#canva.place()
#canva.create_image(image=map_img)
root.mainloop()