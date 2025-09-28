from tkinter import *

def getvals():
    print("Your form has been registred")

root = Tk()
root.geometry("644x344")
# heading
Label(root, text="welcome to Bibek BB Gui",
      font="comicsansms 13 bold", pady=15).grid(row=0, column=3)
# Text for form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmethod = Label(root, text="Payment Mode")

# Pack our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmethod.grid(row=5, column=2)

# Tkinters varibale for stroing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmethodvalue = StringVar()
foodservicevalue = IntVar()

# Enteries our form

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmathodentry = Entry(root, textvariable=paymentmethodvalue)

# Packing the Entries

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmathodentry.grid(row=5, column=3)

#Checkbox
foodservice = Checkbutton(text="Book Now?",variable=foodservicevalue )
foodservice.grid(row=6, column=3)

#Button and packing it's and assigning a command
Button(text="Submit to Bibek BB",command=getvals).grid(row=7, column=3)
root.mainloop()
