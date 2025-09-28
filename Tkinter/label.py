from tkinter import *

root = Tk()

root.geometry("444x555")
root.title("Bibek")
# Imporatnt Label Option
# text - adds the Text
# bd - background
# font=("comicsansms",19,"bold" 
# fg - foreground
# font - sets the font
# padx - x padding
# pady - y padding
# relif - border styling - sunken, Raised, groove, ridge

title_label = Label(text='''Hi, i am Bibek bb from laliptpur nepal, i am learning  a pyhton programming language''', bg = "red" ,fg="blue", padx=44, pady=45 , font = "comicsansms 19 bold" ,borderwidth=3, relief=SUNKEN)
# Important pack Option
# anchor = nw
# side = top, botton, left, right
# fill
# padx
# pady
title_label.pack(side=BOTTOM, anchor="sw", fill="x")
title_label.pack()

root.mainloop()