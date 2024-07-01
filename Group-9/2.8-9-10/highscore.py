from tkinter import *
from tkinter import ttk
import datetime
def save_records(points):
    def save_inp():
        tim = datetime.datetime.today()
        tim = tim.strftime("data: %Y-%m-%d || time: %H.%M.%S")
        with open('records.txt','a',encoding='utf-8') as f:
            print(f'{inp.get()} - набрал {points} || {tim}', file = f)
        win.destroy()
    win = Tk()
    win.title('Name')
    win.geometry('210x50+900+400')
    mainframe = ttk.Frame(win)
    mainframe.grid(row=0,column=0)
    inp = StringVar()
    ttk.Label(mainframe,text="You'r name: ")\
        .grid(row=0,column=0)
    ttk.Entry(mainframe,textvariable=inp)\
        .grid(row=1,column=1)
    ttk.Button(mainframe,text='Save',command=save_inp)\
        .grid(row=1,column=0)
    win.mainloop()