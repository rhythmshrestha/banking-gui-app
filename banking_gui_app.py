#imports
from tkinter import *
import os
from PIL import ImageTk, Image

#main screen
master = Tk()
master.title("Banking App")

#functions
def finish_registration():
    username = temp_username.get()
    phonenum = temp_phonenum.get()
    address = temp_address.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if username == "" or phonenum == "" or address == "" or password == "":
        notif.config(fg="red", text="All fields are required")
        return
    
    for username_check in all_accounts:
        if username == username_check:
            notif.config(fg="red", text="Account already exists")
            return
        else:
            new_file = open(username, "w")
            new_file.write(username+'\n')
            new_file.write(phonenum+'\n')
            new_file.write(address+'\n')
            new_file.write(password+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green", text="Account created successfully")

def register_logic():
    #variables
    global notif
    global temp_username
    global temp_phonenum
    global temp_address
    global temp_password
    temp_username = StringVar()
    temp_phonenum = StringVar()
    temp_address = StringVar()
    temp_password = StringVar()

    #register screen
    register_screen = Toplevel(master)
    register_screen.title("Register")
    
    #register labels
    Label(register_screen, text="Enter your details below to register", font=("calibri", 12)).grid(row=0, columnspan=2, pady=10)
    Label(register_screen, text="Username", font=("calibri", 12)).grid(row=1, column=0, sticky=W)
    Label(register_screen, text="Phone Number", font=("calibri", 12)).grid(row=2, column=0, sticky=W)
    Label(register_screen, text="Address", font=("calibri", 12)).grid(row=3, column=0, sticky=W)
    Label(register_screen, text="Password", font=("calibri", 12)).grid(row=4, column=0, sticky=W)
    notif = Label(register_screen, font=("calibri", 12))
    notif.grid(row=6, columnspan=2, pady=10)

    #register entries
    Entry(register_screen, textvariable= temp_username).grid(row=1, column=1)
    Entry(register_screen, textvariable= temp_phonenum).grid(row=2, column=1)
    Entry(register_screen, textvariable= temp_address).grid(row=3, column=1)
    Entry(register_screen, textvariable= temp_password, show="*").grid(row=4, column=1)

    #register button
    Button(register_screen, text="Register",relief="groove", width=15, command=finish_registration, font=("calibri", 12)).grid(row=5, columnspan=2, pady=5, padx=15)

def login_session():
    global login_username
    global dashboard_notif
    all_accounts = os.listdir()
    login_username = temp_login_username.get()
    login_password = temp_login_password.get()

    if login_username == "" or login_password == "":
        login_notif.config(fg="red", text="Fill all the fields")
        return

    for username in all_accounts:
        if username == login_username:
            file = open(username, "r")
            file_data = file.read()
            file_data = file_data.split("\n")
            password = file_data[3]
            #account dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Your Account")
                #labels
                Label(account_dashboard, text="Account Dashboard", font=("calibri", 12)).grid(row=0, sticky=N, pady=10)
                Label(account_dashboard, text="Welcome "+ username, font=("calibri", 12)).grid(row=1, sticky=N, pady=5)
                #buttons
                Button(account_dashboard,relief="groove", text="Deposit", width= 30, command=deposit, font=("calibri", 12)).grid(row=2, sticky=N, padx=15, pady=5)
                Button(account_dashboard,relief="groove", text="Withdraw", width= 30, command=withdraw, font=("calibri", 12)).grid(row=3, sticky=N, padx=15, pady=5)
                Button(account_dashboard,relief="groove", text="Check Balance", width= 30, command=check_balance, font=("calibri", 12)).grid(row=4, sticky=N, padx=15, pady=5)
                dashboard_notif = Label(account_dashboard)
                dashboard_notif.grid(row=5, sticky=N, pady=10)
                return
            else:
                login_notif.config(fg="red", text="Your password is incorrect")
        else:
            login_notif.config(fg="red", text="Enter correct username")

def deposit():
    print("deposit")

def withdraw():
    print("withdraw")

def check_balance():
    file = open(login_username, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    balance = user_details[4]
    dashboard_notif.config(fg="green", text="Your current balance is NPR "+ balance)

def login_logic():
    global login_notif
    global login_screen
    global temp_login_username
    global temp_login_password
    temp_login_username = StringVar()
    temp_login_password= StringVar()

    #login screen
    login_screen = Toplevel(master)
    login_screen.title("Login")

    #labels for login
    Label(login_screen, text="Enter your details", font=("calibri", 12)).grid(row=0, columnspan=2, pady=10)
    Label(login_screen, text="Username", font=("calibri", 12)).grid(row=1, column=0, sticky=W)
    Label(login_screen, text="Password", font=("calibri", 12)).grid(row=2, column=0, sticky=W)
    login_notif = Label(login_screen, font=("calibri", 12))
    login_notif.grid(row=4, columnspan=2, pady=10)

    #login entries
    Entry(login_screen, textvariable= temp_login_username).grid(row=1, column=1)
    Entry(login_screen, textvariable= temp_login_password, show="*").grid(row=2, column=1)

    #login button
    Button(login_screen, text="Login",relief="groove", command=login_session, width= 15, font=("calibri", 12)).grid(row=3, columnspan=2, padx=15, pady=5)

#image import
img = Image.open('C:\\Users\\sthar\\OneDrive\\Desktop\\banking gui app\\img.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#labels
Label(master, text="Banking Application", font=("Calibri",14)).grid(row=0,sticky=N,pady=10)
Label(master, text="Developed by Rhythm Shrestha", font=("Calibri",12)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

#buttons
Button(master, text="Register",relief="groove", font=("Calibri", 12), width=20, command=register_logic).grid(row=3,sticky=N)
Button(master, text="Login",relief="groove", font=("Calibri", 12), width=20, command=login_logic).grid(row=4,sticky=N, pady=10)

master.mainloop()