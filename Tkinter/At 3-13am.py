from tkinter import *
def getvals():
    print("Your form has been saved")
    print(f"You name is {namevalue.get()}")
    print(f"Your password is {passwordvalue.get()}")
    print(f"Your locationis {locationvalue.get()}")

root = Tk()
root.geometry("555x555")
root.title("Bibek BB window")


namevalue = StringVar()
passwordvalue = StringVar()
locationvalue = StringVar()

title = Label(root, text="Submission form", padx=10).grid(row=0)
name = Label(root, text="Enter you Name:")
password = Label(root, text="Enter you password:")
location = Label(root, text="Enter your location:")

name.grid(row=1,column=1)
password.grid(row=2,column=1)
location.grid(row=3,column=1)

nameentry = Entry(root, textvariable=namevalue)
passwordentry = Entry(root,show="*", textvariable=passwordvalue)
locationentry = Entry(root, textvariable=locationvalue)

nameentry.grid(row=1, column=2)
passwordentry.grid(row=2, column=2)
locationentry.grid(row=3,column=2)

terms = Checkbutton(text="I Agree Terms And Conditions" ).grid(row=4,column=2)

Button(text="Submit", command=getvals).grid(row=5,column=2)

root.mainloop()