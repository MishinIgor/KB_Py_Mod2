from tkinter import ttk
from tkinter import *
def save_my_rezult(points):
    def save_inp():
        try:
            with open('records.txt','x',encoding='utf-8') as f:
                print(inp.get(),file=f,end='')
                print(f' - набрал попугаев:{points}',file=f)
        except FileExistsError:
            with open('records.txt','a',encoding='utf-8') as f:
                print(inp.get(),file=f,end='')
                print(f' - набрал попугаев:{points}',file=f)
        win.destroy()
    win = Tk()
    win.title('NickName:')
    win.geometry(f'130x70+900+400')
    mainframe = ttk.Frame(win)
    mainframe.grid(row=0,column=0)
    inp = StringVar()
    ttk.Label(mainframe,text='Nickname:') \
        .grid(row=0,column=0)
    ttk.Entry(mainframe,textvariable=inp) \
        .grid(row=1,column=0)
    ttk.Button(mainframe, text='Save', command=save_inp)\
        .grid(row=2,column=0)
    win.mainloop()