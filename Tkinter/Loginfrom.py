from tkinter import *

def getvals():
    print("Your form has been submitted.")
    print("Your loged In information is here")
    print(f"Your name is {namevalue.get()}")
    print(f"Your password is {passwordvalue.get()}")
    print(f"Your email id {emailvalue.get()}")

root = Tk()
root.geometry("555x555")
root.title("BLogin Form")

namevalue = StringVar()
emailvalue = StringVar()
passwordvalue = StringVar()

name = Label(root, text="Enter your name").grid(row=0,column=1)
email = Label(root, text="Enter your Email ID").grid(row=1,column=1)
password = Label(root, text="Enter your password").grid(row=2,column=1)

nameEntry = Entry(root, textvariable=namevalue).grid(row=0,column=2)

emailEntry = Entry(root, textvariable=emailvalue).grid(row=1,column=2)
passEntry = Entry(root,show="*" ,textvariable=passwordvalue).grid(row=2,column=2)

Button(text="LogIn", command=getvals).grid(row=3, column=4)

root.mainloop()