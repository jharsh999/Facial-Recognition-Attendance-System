import os
import tkinter as tk
from datetime import datetime
from emb import emb
from recog import recog

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

window = tk.Tk()

# setting attribute
window.state('zoomed')
window.title("Facial Attendance System")

name_var=tk.StringVar()
Roll_var=tk.StringVar()


test = tk.Label(window, text="Facial Attendance System Using python And OpenCV",font=("Arial Bold", 25),bg="pink")
test.pack(side=tk.TOP,pady=30)

test = tk.Label(window, text="Enter Name :-",width=20,font=("Arial Bold", 15), bg="brown", fg="white")
test.pack(side=tk.TOP,pady=20)
name = tk.Entry(window,textvariable = name_var, font=('calibre',15,'normal'))
name.pack(side=tk.TOP,pady=5)

test = tk.Label(window,text="Enter Roll Number :-",width=20,font=("Arial Bold", 15), bg="brown", fg="white")
test.pack(side=tk.TOP,pady=20)
Roll = tk.Entry(window,textvariable = Roll_var, font=('calibre',15,'normal'))
Roll.pack(side=tk.TOP)

def run1():
    e1 = emb
    e1.Add(name_var.get(),Roll_var.get())
    # os.system('python emb.py')
Add = tk.Button(window, text ="Add Student",width=20,bg="Light blue",font=("Arial Bold", 15), command =run1)
Add.pack(side=tk.TOP,pady=20)


def run2():
    os.system(current_date+'.csv')
Add = tk.Button(window, text ="Manually Attendance",width=20,bg="Light blue",font=("Arial Bold", 15), command =run2)
Add.pack(padx=130, side=tk.LEFT)

def run3():
    r1 = recog
    r1.Attendance("")
    #os.system('python recog.py')
Add = tk.Button(window, text ="Automatic Attendance",width=20,bg="Light blue",font=("Arial Bold", 15), command =run3)
Add.pack(padx=130, side=tk.LEFT)

def run4():
    os.system('StudentList.csv')
Add = tk.Button(window, text ="List of Students",width=20,bg="Light blue",font=("Arial Bold", 15), command =run4)
Add.pack(padx=130, side=tk.LEFT)


window.configure(background='#ecbcb4')
window.mainloop()