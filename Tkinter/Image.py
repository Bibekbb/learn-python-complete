from tkinter import *
from PIL import Image

root = Tk()

#Show window
root.geometry("455x244")

#Show Image
# photo = PhotoImage(file="Tkinter/1.png")

#for Jpg Image
image = Image.open("Tkinter/sani.jpg")
photo = Image.PhotoImage(Image)
 
label = Label(image=photo)
label.pack()

root.mainloop()




