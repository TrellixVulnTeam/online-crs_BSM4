import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class login_page:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1350x700+0+0")

        self.bg_icon = tk.PhotoImage(file=r"images/check_bg.png")
        self.user_icon = tk.PhotoImage(file=r"images/logo.png")
        self.name_icon = tk.PhotoImage(file=r"images/usericon.png")
        self.passw_icon = tk.PhotoImage(file=r"images/pass2.png")
        lb_bg = tk.Label(self.root, image=self.bg_icon, )
        lb_bg.place(x=0, y=0, relwidth=1, relheight=1)
        Button1=tk.Button(self.root,text="Incident detail",bg="blue",activebackground="red",activeforeground="yellow",font=("times new roman",30,"bold"),command=self.login)
        Button1.grid(row=0,column=0,columnspan=3)
        Button2=tk.Button(self.root,text="suspect details:",bg="blue",activebackground="red",activeforeground="yellow",font=("times new roman",30,"bold"),command=self.suspect)
        Button2.grid(row=0,column=4)
        Button3=tk.Button(self.root,text="complaint details",bg="blue",activebackground="red",activeforeground="yellow",font=("times new roman",30,"bold"),command=self.form)
        Button3.grid(row=0,column=5)
    def form(self):
        Frame2=tk.Frame(self.root,bg="white")
        Frame2.place(x=400,y=150)
        self.phone = tk.PhotoImage(file=r"images/phone.png")
        self.place = tk.PhotoImage(file=r"images/icons8-location-24.png")
        self.mobile_no = tk.StringVar()
        self.uname = tk.StringVar()
        self.state = tk.StringVar()
        self.district = tk.StringVar()
        self.police_station = tk.StringVar()
        self.relation = tk.StringVar()
        self.email_id=tk.StringVar()

        tk.Label(Frame2, text="Name:", image=self.name_icon, compound=tk.LEFT, bg="white",
              font=("times new roman", 20, "bold")).grid(row=1, column=0, padx=40, pady=20)
        tk.Entry(Frame2, bd=5, relief=tk.GROOVE, textvariable=self.uname, font=("", 15)).grid(row=1, column=1,
                                                                                        padx=20)
        tk.Label(Frame2, text="Mobile no", image=self.phone, compound=tk.LEFT, bg="white",
              font=("times new roman", 20, "bold")).grid(row=2, column=0, padx=40, pady=20)
        tk.Entry(Frame2, bd=5, relief=tk.GROOVE, textvariable=self.mobile_no, font=("", 15)).grid(row=2, column=1,
                                                                                            padx=20)
        tk.Label(Frame2, text="State:", image=self.place, compound=tk.LEFT, bg="white",
              font=("times new roman", 20, "bold")).grid(row=3, column=0, padx=40, pady=20)
        state = tk.StringVar()
        choose_state = ttk.Combobox(Frame2, text="**state**", textvariable=state, font=("times new roman", 20, "bold"))

        choose_state['values'] = (
        '**select select**', 'Andra Pradesh', 'Hyderabad', 'Amaravati', 'Arunachal Pradesh', 'Itangar', 'Assam',
        'Dispur', 'Bihar', 'Patna', 'Chhattisgarh', 'Raipur', 'Goa', 'Panaji', 'Gujarat', 'Gandhinagar', 'Haryana',
        'Chandigarh', 'Himachal Pradesh', 'Shimla', 'Jammu and Kashmir', 'Srinagar and Jammu', 'Jharkhand', 'Ranchi',
        'Karnataka', 'Bangalore', 'Kerala', 'Thiruvananthapuram', 'Madya Pradesh', 'Bhopal', 'Maharashtra', 'Mumbai',
        'Manipur', 'Imphal', 'Meghalaya', 'Shillong', 'Mizoraz', 'Aizawi', 'Nagaland', 'Kohima', 'Orissa',
        'Bhubaneshwar', 'Punjab', 'Chandigarh', 'Rajasthan', 'Jaipur', 'Sikkim', 'Gangtok', 'Tamil Nadu', 'Chennai',
        'Telagana', 'Hyderabad', 'Tripura', 'Agartala', 'Uttaranchal', 'Dehradun', 'Uttar Pradesh', 'Lucknow',
        'West Bengal', 'Kolkata')
        choose_state.grid(row=3, column=1, padx=40, pady=40)
        choose_state.current(0)

        l1 = tk.Label(Frame2, text="DISTRICT:", compound=tk.LEFT, bg="white", font=("times of roman", 20, "bold"))
        l1.grid(row=4, column=0, padx=40,pady=20)
        txt_district = tk.Entry(Frame2, textvariable=self.district,bd=5, relief=tk.GROOVE,font=("times new roman",20,"bold") )
        txt_district.grid(row=4, column=1, padx=20)

        l2 = tk.Label(Frame2, text="Police_station:",bg="white", font=("times of roman", 20, "bold"))
        l2.grid(row=5, column=0, padx=40, pady=20)
        ploice=tk.Entry(Frame2, textvariable=self.police_station,bd=5,relief=tk.GROOVE,font=("times new roman", 20, "bold"))
        ploice.grid(row=5, column=1, padx=20)
        l3 = tk.Label(Frame2, text="relationship with the victim", bg="white",font=("times of roman", 20, "bold"))
        l3.grid(row=6, column=0, padx=40, pady=20)
        text_incident =tk.Entry(Frame2, bd=5, relief=tk.GROOVE, textvariable=self.relation,
                              font=("times new roman", 20, "bold"))
        text_incident.grid(row=6, column=1, padx=20)
        tk.Label(Frame2, text="email id", bg="white",font=("times new roman", 20, "bold")).grid(row=7, column=0, padx=40, pady=20)
        tk.Entry(Frame2, bd=5, relief=tk.GROOVE, textvariable=self.email_id, font=("", 15)).grid(row=7, column=1,padx=20)




    def login(self):
        logoFrame = tk.Frame(self.root, bg="white", width=600, height=300)
        logoFrame.place(x=200, y=150)
        self.uname = tk.StringVar()
        self.pas = tk.StringVar()
        self.cat=tk.StringVar()
        self.time=tk.StringVar()
        self.place=tk.StringVar()
        category=tk.Label(logoFrame,text="category of complaint*",font=("times new roman",20,"bold"),bg="white")
        category.grid(row=1,column=0)
        catent=tk.Entry(logoFrame, bd=5, relief=tk.GROOVE, textvariable=self.cat, font=("", 15))
        catent.grid(row=1, column=1)
        username = tk.Label(logoFrame, text="approximate timing and date of incident/recieving/viewing of content *", bg="white",
                         font=("times new roman", 20, "bold"))
        username.grid(row=2, column=0)
        txtuser = tk.Entry(logoFrame, bd=5, relief=tk.GROOVE, textvariable=self.time, font=("", 15))
        txtuser.grid(row=2, column=1)
        userpass = tk.Label(logoFrame, text="where did the incident occur?", bg="white",font=("times new roman", 20, "bold"))
        userpass.grid(row=3, column=0)
        txtpass = tk.Entry(logoFrame, bd=5, relief=tk.GROOVE, textvariable=self.place, font=("", 15))
        txtpass.grid(row=2, column=1,padx=10)
        ent=tk.Entry(logoFrame,bd=3,relief=tk.GROOVE,textvariable=self.place,font=("",15))
        ent.grid(row=3,column=1)

        btn1 = tk.Button(logoFrame, text="submit", bg="blue", fg="white", font=("times new roman", 20, "bold"),command=self.log_in)
        btn1.grid(row=5, columnspan=2, pady=20)
    def suspect(self):
        logoFrame = tk.Frame(self.root, bg="white", width=600, height=300)
        logoFrame.place(x=200, y=150)
        self.uname = tk.StringVar()
        self.pas = tk.StringVar()
        self.cat = tk.StringVar()
        self.time = tk.StringVar()
        self.place = tk.StringVar()
        self.var=tk.StringVar()
        self.addr=tk.StringVar()
        sus=tk.Label(logoFrame, text="Please share the details of the suspect.Any information will be kept confidential amd may help during investigation", font=("times new roman", 10, "bold"),
                         bg="light blue")
        sus.grid(row=1, column=0)
        category = tk.Label(logoFrame, text="suspect_name", font=("times new roman", 20, "bold"),
                         bg="white")
        category.grid(row=2, column=0)
        catent = tk.Entry(logoFrame, bd=5, relief=tk.GROOVE, textvariable=self.cat, font=("", 15))
        catent.grid(row=2, column=1)
        username = tk.Label(logoFrame, text="id_number:",
                         bg="white",
                         font=("times new roman", 20, "bold"))
        username.grid(row=3, column=0)
        txtuser = tk.Entry(logoFrame, bd=5, relief=tk.GROOVE, textvariable=self.time, font=("", 15))
        txtuser.grid(row=3, column=1)
        Btn=tk.Button(logoFrame,text="ADD",bg="blue",font=("times new roman",20,"bold"),fg="white")
        Btn.grid(row=4,columnspan=2)







    def log_in(self):
        if self.uname.get() == "" or self.place.get() or self.cat.get() or self.time.get()  == "" :
            messagebox.showerror("error", "All field required")
        elif self.uname.get() == "aishwarya" and self.pas.get() == "ishu":
            messagebox.showinfo("successful", f"welcome {self.uname.get()} ")
        else:
            messagebox.showerror("invalide", "invalide Username or Password")


root = tk.Tk()
obj = login_page(root)
root.mainloop()