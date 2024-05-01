from tkinter import *
import os
from PIL import ImageTk, Image

master = Tk()
master.title("Banking App")

img = Image.open('C:\\Users\\sthar\\OneDrive\\Desktop\\banking gui app\\img.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

Label(master, text="Banking Application", font=("Calibri",14)).grid(row=0,sticky=N,pady=10)
Label(master, text="Developed by Rhythm Shrestha", font=("Calibri",12)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N, pady=15)

master.mainloop()