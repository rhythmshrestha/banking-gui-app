#imports
from tkinter import *
import os
from PIL import ImageTk, Image

#main screen
master = Tk()
master.title("Banking App")

#functions
def finish_registration():
    name = temp_name.get()
    phonenum = temp_phonenum.get()
    address = temp_address.get()
    password = temp_password.get()

def register_logic():
    #variables
    global temp_name
    global temp_phonenum
    global temp_address
    global temp_password
    temp_name = StringVar()
    temp_phonenum = StringVar()
    temp_address = StringVar()
    temp_password = StringVar()

    #register screen
    register_screen = Toplevel(master)
    register_screen.title("Register")
    
    #register labels
    Label(register_screen, text="Enter your details below to register", font=("calibri", 12)).grid(row=0, columnspan=2, pady=10)
    Label(register_screen, text="Name", font=("calibri", 12)).grid(row=1, column=0, sticky=W)
    Label(register_screen, text="Phone Number", font=("calibri", 12)).grid(row=2, column=0, sticky=W)
    Label(register_screen, text="Address", font=("calibri", 12)).grid(row=3, column=0, sticky=W)
    Label(register_screen, text="Password", font=("calibri", 12)).grid(row=4, column=0, sticky=W)

    #register entries
    Entry(register_screen, textvariable= temp_name).grid(row=1, column=1)
    Entry(register_screen, textvariable= temp_phonenum).grid(row=2, column=1)
    Entry(register_screen, textvariable= temp_address).grid(row=3, column=1)
    Entry(register_screen, textvariable= temp_password, show="*").grid(row=4, column=1)

    #register button
    Button(register_screen, text="Register", command=finish_registration, font=("calibri", 12)).grid(row=5, columnspan=2, pady=10)

def login_logic():
    print("This is a login page")

#image import
img = Image.open('C:\\Users\\sthar\\OneDrive\\Desktop\\banking gui app\\img.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#labels
Label(master, text="Banking Application", font=("Calibri",14)).grid(row=0,sticky=N,pady=10)
Label(master, text="Developed by Rhythm Shrestha", font=("Calibri",12)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

#buttons
Button(master, text="Register", font=("Calibri", 12), width=20, command=register_logic).grid(row=3,sticky=N)
Button(master, text="Login", font=("Calibri", 12), width=20, command=login_logic).grid(row=4,sticky=N, pady=10)

master.mainloop()