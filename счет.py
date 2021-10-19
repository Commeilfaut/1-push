
from tkinter import *

temp = 0
after_id = ""

def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    label1.configure(text=str(temp))
    temp += 1

def start_sw():
    btn1.grid_forget()
    btn2.grid(row=1, columnspan=2, sticky='ew')
    tick()

def close_window():
    root.destroy()


root =Tk()

root.title('Секундомер')

label1 = Label(root, width=5, font=('Ubuntu', 100), text='0')
label1.grid(row=0,columnspan=2)

btn1 = Button(root, text='Start', font=('ubuntu', 30), command=start_sw)
btn2 = Button(root, text='Exit', font=('ubuntu', 30), command=close_window)

btn1.grid(row=1, columnspan=2, sticky='ew')

root.mainloop()
