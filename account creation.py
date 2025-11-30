from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')
frame = Frame(master = root, height = 200, width = 360, bg = '#d0efff')

lbl1 = Label(frame, text = "Full Name", bg = '#3895D3', fg = 'white', width = 12 )
lbl2 = Label(frame, text = "Email", bg = '#3895D3', fg = 'white', width = 12 )
lbl3 = Label(frame, text = "Password", bg = '#3895D3', fg = 'white', width = 12 )

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show = '*')

def display():
    name = name_entry.get()
    greet = "Hey "+name
    message = "\nCongratulations on your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg = "#BEBEBE", fg = 'black')

btn = Button(text = "Submit", command = display, bg = 'red')

frame.place(x = 20, y = 0)
lbl1.place(x = 20, y = 20)
name_entry.place(x = 150, y = 20)
lbl2.place(x = 20, y = 70)
email_entry.place(x = 150, y = 70)
lbl3.place(x = 20, y = 120)
pass_entry.place(x = 150, y = 120)
btn.place(x = 160, y = 220)
textbox.place(y = 250)

root.mainloop()