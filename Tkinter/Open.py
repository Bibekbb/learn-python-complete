from tkinter import *
def getvals():
    print("Value Stored")
root = Tk()
root.geometry("555x555")
root.title("BIBEK BB WINDOW")

user = Label(root, text="Username")
password = Label(root, text="Password")

user.grid()
password.grid(row=1)

userinput = StringVar()
passinput = StringVar()

userentry = Entry(root, textvariable=userinput)
passentry = Entry(root, textvariable=passinput)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit" ,command=getvals).grid(row=2)
root.mainloop()