import tkinter as tk
import PIL
from PIL import ImageTk, Image
import webbrowser
import mysql.connector

#creating db connection 
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Dreamers29",
database="crime_report")
curs = mydb.cursor()
check2 = "SHOW TABLES LIKE 'sttn_contact'"  
curs.execute(check2)
result1 = curs.fetchone()
if result1:
    print("table for contact exists")
else:
    print("table doesn't exist")
    curs.execute("CREATE TABLE sttn_contact (id int AUTO_INCREMENT PRIMARY KEY, pid int NOT NULL, designation VARCHAR(255), contact VARCHAR(66), email VARCHAR(66))")

window = tk.Tk()
name_var = tk.StringVar()
dist_var = tk.StringVar()
city_var = tk.StringVar()
state_var = tk.StringVar()
pc_var = tk.StringVar()
jd_var = tk.StringVar()
ot_var = tk.StringVar()
ct_var = tk.StringVar()
des_var = tk.StringVar()
ctt_var = tk.StringVar()
email_var = tk.StringVar()

window.title("Welcome to TutorialsPoint")
window.geometry('400x400')
window.configure(background = "grey")
name = tk.Label(window ,text = "Name of Police Station")
name.grid(row = 0,column = 0)
district = tk.Label(window ,text = "District")
district.grid(row = 1,column = 0)
city = tk.Label(window ,text = "City")
city.grid(row = 2,column = 0)
state = tk.Label(window ,text = "State")
state.grid(row = 3,column = 0)
pc = tk.Label(window ,text = "Pincode")
pc.grid(row = 4,column = 0)
jd = tk.Label(window ,text = "Jurisdication")
jd.grid(row = 5,column = 0)

contact = tk.Label(window, text="Phone no.")
contact.grid(row= 8, column = 0)
des = tk.Label(window, text="Designation: ")
des.grid(row=9, column=0)
email = tk.Label(window, text="Email id")
email.grid(row=10, column=0)



name_in = tk.Entry(window, textvariable=name_var)
name_in.grid(row = 0,column = 1)
district_in = tk.Entry(window, textvariable=dist_var)
district_in.grid(row = 1,column = 1)
city_in = tk.Entry(window, textvariable=city_var)
city_in.grid(row = 2,column = 1)
state_in = tk.Entry(window, textvariable=state_var)
state_in.grid(row = 3,column = 1)
pc_in = tk.Entry(window, textvariable=pc_var)
pc_in.grid(row = 4,column = 1)
jd_in = tk.Entry(window, textvariable=jd_var)
jd_in.grid(row = 5,column = 1)

des_in = tk.Entry(window, textvariable=des_var)
des_in.grid(row = 8,column = 1)
ctt_in = tk.Entry(window, textvariable=ctt_var)
ctt_in.grid(row = 9,column = 1)
email_in = tk.Entry(window, textvariable=email_var)
email_in.grid(row = 10,column = 1)

#function
def onSubmit():
    name_db=name_var.get() 
    dist_db =dist_var.get() 
    city_db = city_var.get()
    state_db = state_var.get()
    pc_db = pc_var.get()
    jd_db = jd_var.get()
    des_db = des_var.get()
    ctt_db = ctt_var.get()
    email_db = email_var.get()
    pid = 0
    inst= """INSERT INTO stations (sttn_name, district, city, state, pincode, jurisdication ) 
                           VALUES 
                           (%(name_db)s, %(dist_db)s, %(city_db)s, %(state_db)s, %(pc_db)s, %(jd_db)s) """
    curs.execute(inst, {
        'name_db':name_db,
        'dist_db':dist_db,
        'city_db':city_db,
        'state_db':state_db,
        'pc_db':pc_db,
        'jd_db':jd_db
    })
    mydb.commit()
    curs.execute("SELECT id FROM stations WHERE sttn_name=%(name_db)s AND district=%(dist_db)s", {'name_db':name_db, 'dist_db': dist_db})
    res = curs.fetchone()
    x = 0
    (x) = res
    pid = x[0]
    #pid = int(res['id'])
    print(pid)   
    curs.execute("SELECT * FROM stations")
    res1 = curs.fetchall()
    for y in res1:
        print(y)
    instctt = """INSERT INTO sttn_contact (pid, designation, contact, email) 
                           VALUES 
                           (%(pid)s, %(des_db)s, %(ctt_db)s, %(email_db)s) """
    curs.execute(instctt, {
            'pid':pid,
            'des_db':des_db,
            'ctt_db':ctt_db,
            'email_db':email_db
        })
    mydb.commit()

    


btn = tk.Button(window ,text="Submit", command=lambda:onSubmit())
btn.grid(row=11,column=0)
window.mainloop()

