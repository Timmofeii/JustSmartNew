from tkinter import  *

root = Tk()
button = Button(root,text  = 'click  on me ')
button.pack()
entry = Entry(root)
root.mainloop()


import tkinter as tk
root = tk.Tk()
root.title("soccer game")
root.geometry("200x100")
label = tk.Label(root,bg="green",text = "hi",fg = "blue",font = ("Arial",33))
label.pack(side="right", padx= 10,pady=10)
def my_friend():
    label.config(fg = "pink")
button = tk.Button(root, text="click on me", command=my_friend)
button.pack()
entry = tk.Entry(root)
entry.pack()
def change_label():
    label.config(text = entry.get())
change_button = tk.Button(root,text = "change label",command = change_label)
change_button.pack()
root.mainloop()