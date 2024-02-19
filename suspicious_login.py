import sqlite3
import tkinter  as tk
from tkinter import *
import time
import numpy as np

import tkinter.messagebox

import os
from PIL import Image , ImageTk
from PIL import *
from PIL import Image # For face recognition we will the the LBPH Face Recognizer
 

root = tk.Tk()
root.geometry('800x350')
root.title("Login Form")
root.resizable(False,False)

Name=StringVar()
upass=StringVar()


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")
import sqlite3
my_conn = sqlite3.connect('face.db')

#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.geometry("%dx%d+0+0" % (w, h))


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('new3.jpg')
image2 =image2.resize((1400,700), Image.LANCZOS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image
background_label.place(x=0, y=0)
#-----------------------------------



def login_now():
   
##### tkinter window ######
    print("reg")
 
   
 
    from subprocess import call
    call(["python", "GUI_Master.py"])  
   
   
label_0 = Label(root, text="Login Here",width=20,font=("bold", 20))
label_0.place(x=260,y=53)



label_1 = Label(root, text="User Name",width=20,font=("bold", 11))
label_1.place(x=250,y=130)

entry_1 = Entry(root,textvar=Name,bg="lightgray",font=("bold", 11))
entry_1.place(x=450,y=130)

label_2 = Label(root, text="Password",width=20,font=("bold", 11))
label_2.place(x=250,y=180)

entry_2 = Entry(root,textvar=upass,bg="lightgray",font=("bold", 11))
entry_2.place(x=450,y=180)

#img=ImageTk.PhotoImage(Image.open ("E:\\login_button.jpg"))
#image3 =Image.open('p.jpg')
#img =image3.resize((60,50), Image.ANTIALIAS)

Button(root, text='Login Now',width=20,bg='red',fg='white',command=login_now).place(x=350,y=250)



root.mainloop()



