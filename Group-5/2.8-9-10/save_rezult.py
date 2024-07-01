from tkinter import *
from tkinter import ttk
import datetime
def my_rezult(points):
    def save_inp():
        today = datetime.datetime.today()
        today = today.strftime("%Y-%m-%d-%H.%M.%S")
        with open('records.txt','a',encoding='utf-8') as f:
            print(f'{inp.get()}-набрал {points} попугаев; data: {today[:10]}, time: {today[11:]};',file=f)
        win.destroy()
    win = Tk()
    win.title('save')
    win.geometry('235x50+900+400')
    mainframe = ttk.Frame(win)
    mainframe.grid(row=0,column=0)
    inp = StringVar()
    ttk.Label(mainframe,text="     You'r nickname:")\
        .grid(row=0,column=0)
    ttk.Entry(mainframe, textvariable = inp)\
        .grid(row=1,column=1)
    ttk.Button(mainframe,text='Save', command=save_inp)\
        .grid(row=1,column=0)
    win.mainloop()
