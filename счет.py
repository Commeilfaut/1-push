
import tkinter as tk

import time

def exit_programm():
    print('exit')

def generator():
    a = 0
    while True:
         a = a + 1
         print(a)
         time.sleep(1)



win = tk.Tk()
win.geometry(f"240x270+100+200")
win.title('моя кнопка')


btn1 = tk.Button(win, text='Exit',
                 command=exit_programm)
btn1.pack()

win.mainloop()
