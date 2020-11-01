import tkinter as tk
import PIL
from PIL import ImageTk, Image
import webbrowser
import mysql.connector
from tkinter import ttk

#creating db connection 
class reg_police:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title('Register your branch')
        try:
            self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dreamers29",
            database ="crime_report")
            self.curs = self.mydb.cursor()
        except: 
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Dreamers29")
            self.curs = self.mydb.cursor()
            self.curs.execute("CREATE DATABASE crime_report")
        self.check1 = "SHOW TABLES LIKE 'stations'"
        self.curs.execute(self.check1)
        self.result = self.curs.fetchone()
        if self.result:
            print("table exist")
        else:
            print("table doesn't exist")
            self.curs.execute("CREATE TABLE stations (id int AUTO_INCREMENT PRIMARY KEY, sttn_name VARCHAR(255), district VARCHAR(255), city VARCHAR(255), state VARCHAR(255), pincode VARCHAR(66), jurisdication VARCHAR(255))")
        self.check2 = "SHOW TABLES LIKE 'sttn_contact'"  
        self.curs.execute(self.check2)
        self.result1 = self.curs.fetchone()
        if self.result1:
            print("table for contact exists")
        else:
            print("table doesn't exist")
            self.curs.execute("CREATE TABLE sttn_contact (id int AUTO_INCREMENT PRIMARY KEY, pid int NOT NULL, designation VARCHAR(255), contact VARCHAR(66), email VARCHAR(66))")
        self.name_var = tk.StringVar()
        self.dist_var = tk.StringVar()
        self.city_var = tk.StringVar()
        self.state_var = tk.StringVar()
        self.pc_var = tk.StringVar()
        self.jd_var = tk.StringVar()
        self.ot_var = tk.StringVar()
        self.ct_var = tk.StringVar()
        self.des_var = tk.StringVar()
        self.ctt_var = tk.StringVar()
        self.email_var = tk.StringVar()

        self.window.geometry('1350x1000+0+0')
        #self.window.configure(background = "grey")
        self.bg_icon=tk.PhotoImage(file=r"images/check_bg.png")
        self.lb_bg=tk.Label(self.window,image=self.bg_icon)
        self.label3=tk.Label(self.window,text="REGISTERATION PAGE",font=("times new roman",40,"bold"),border=10,relief=tk.GROOVE,bg="yellow")
        self.label3.place(x=336,y=0)
        self.cont = tk.Frame(self.window, bg="white", height=400, width=800)
        self.cont.place(x=400, y=200)

        self.name = tk.Label(self.cont,text = "Name of Police Station", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.name.grid(row = 0,column = 0, padx=40,pady=10)
        self.district = tk.Label(self.cont ,text = "District", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.district.grid(row = 1,column = 0, padx=40,pady=10)
        self.city = tk.Label(self.cont ,text = "City", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.city.grid(row = 2,column = 0, padx=40,pady=10)
        self.state = tk.Label(self.cont ,text = "State", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.state.grid(row = 3,column = 0, padx=40,pady=10)
        self.pc = tk.Label(self.cont ,text = "Pincode", compound=tk.LEFT,bg="white",font=("times new roman",16,))
        self.pc.grid(row = 4,column = 0, padx=40,pady=10)
        self.jd = tk.Label(self.cont,text = "Jurisdiction", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.jd.grid(row = 5,column = 0, padx=40,pady=10)

        self.contact = tk.Label(self.cont, text="Phone no.", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.contact.grid(row= 8, column = 0, padx=40,pady=10)
        self.des = tk.Label(self.cont, text="Designation: ", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.des.grid(row=9, column=0, padx=40,pady=10)
        self.email = tk.Label(self.cont, text="Email id", compound=tk.LEFT,bg="white",font=("times new roman",16))
        self.email.grid(row=10, column=0, padx=40,pady=10)



        self.name_in = tk.Entry(self.cont, textvariable=self.name_var, bd=5, relief=tk.GROOVE,)
        self.name_in.grid(row = 0,column = 1,padx=20)
        self.district_in = tk.Entry(self.cont, textvariable=self.dist_var, bd=5, relief=tk.GROOVE,)
        self.district_in.grid(row = 1,column = 1, padx=20)
        self.city_in = tk.Entry(self.cont, textvariable=self.city_var, bd=5, relief=tk.GROOVE,)
        self.city_in.grid(row = 2,column = 1, padx=20)
        self.state_in=ttk.Combobox(self.cont,textvariable=self.state_var,font=("times new roman",13))

        self.state_in['values']=('Select state','Andra Pradesh','Hyderabad', 'Amaravati','Arunachal Pradesh','Itangar','Assam','Dispur','Bihar','Patna','Chhattisgarh','Raipur','Goa','Panaji','Gujarat','Gandhinagar','Haryana','Chandigarh','Himachal Pradesh','Shimla','Jammu and Kashmir','Srinagar and Jammu','Jharkhand','Ranchi','Karnataka','Bangalore','Kerala','Thiruvananthapuram','Madya Pradesh','Bhopal','Maharashtra','Mumbai','Manipur','Imphal','Meghalaya','Shillong','Mizoraz','Aizawi','Nagaland','Kohima','Orissa','Bhubaneshwar','Punjab','Chandigarh','Rajasthan','Jaipur','Sikkim','Gangtok','Tamil Nadu','Chennai','Telagana','Hyderabad','Tripura','Agartala','Uttaranchal','Dehradun','Uttar Pradesh','Lucknow','West Bengal','Kolkata')
        self.state_in.grid(row=3, column=1, padx=20)
        self.state_in.current(0)
        self.pc_in = tk.Entry(self.cont, textvariable=self.pc_var, bd=5, relief=tk.GROOVE,)
        self.pc_in.grid(row = 4,column = 1, padx=20)
        self.jd_in = tk.Entry(self.cont, textvariable=self.jd_var, bd=5, relief=tk.GROOVE,)
        self.jd_in.grid(row = 5,column = 1, padx=20)

        self.des_in = tk.Entry(self.cont, textvariable=self.des_var, bd=5, relief=tk.GROOVE,)
        self.des_in.grid(row = 8,column = 1,padx=20)
        self.ctt_in = tk.Entry(self.cont, textvariable=self.ctt_var, bd=5, relief=tk.GROOVE,)
        self.ctt_in.grid(row = 9,column = 1, padx=20)
        self.email_in = tk.Entry(self.cont, textvariable=self.email_var, bd=5, relief=tk.GROOVE,)
        self.email_in.grid(row = 10,column = 1, padx=20)
        self.btn = tk.Button(self.cont ,text="Submit", bg="white",fg="blue",font=("times new roman",14,"bold"), command=lambda:self.onSubmit())
        self.btn.grid(row=11,column=1, pady=20)

    #function
    def onSubmit(self):
        self.name_db=self.name_var.get() 
        self.dist_db =self.dist_var.get() 
        self.city_db = self.city_var.get()
        self.state_db = self.state_var.get()
        self.pc_db = self.pc_var.get()
        self.jd_db = self.jd_var.get()
        self.des_db = self.des_var.get()
        self.ctt_db = self.ctt_var.get()
        self.email_db = self.email_var.get()
        self.pid = 0
        self.inst= """INSERT INTO stations (sttn_name, district, city, state, pincode, jurisdication ) 
                           VALUES 
                           (%(name_db)s, %(dist_db)s, %(city_db)s, %(state_db)s, %(pc_db)s, %(jd_db)s) """
        self.curs.execute(self.inst, {
            'name_db':self.name_db,
            'dist_db':self.dist_db,
            'city_db':self.city_db,
            'state_db':self.state_db,
            'pc_db':self.pc_db,
            'jd_db':self.jd_db })
        self.mydb.commit()
        self.curs.execute("SELECT id FROM stations WHERE sttn_name=%(name_db)s AND district=%(dist_db)s", {'name_db':self.name_db, 'dist_db': self.dist_db})
        self.res = self.curs.fetchone()
        x = 0
        (x) = self.res
        self.pid = x[0]
        #pid = int(res['id'])
        print(self.pid)   
    
        self.instctt = """INSERT INTO sttn_contact (pid, designation, contact, email) 
                           VALUES 
                           (%(pid)s, %(des_db)s, %(ctt_db)s, %(email_db)s) """
        self.curs.execute(self.instctt, {
            'pid':self.pid,
            'des_db':self.des_db,
            'ctt_db':self.ctt_db,
            'email_db':self.email_db
        })
        self.mydb.commit()
window=tk.Tk()
obj_home = reg_police(window)

window.mainloop()

