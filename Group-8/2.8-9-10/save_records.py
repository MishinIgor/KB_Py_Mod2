from tkinter import *
from tkinter import ttk
def save_records(points):
    def save_inp():
        try:
            with open('records.txt','x',encoding='utf-8') as f:
                print(inp.get(), file = f,end=' - ')
                print(f'набрал {points} поугаев(я)',file= f)
        except FileExistsError:
            with open('records.txt','a',encoding='utf-8') as f:
                print(inp.get(), file = f,end=' - ')
                print(f'набрал {points} поугаев(я)',file= f)
        win.destroy()
    win = Tk()
    win.title('Никнейм?')
    win.geometry('250x50')
    mainframe = ttk.Frame(win)
    mainframe.grid(row = 0, column = 0)
    inp = StringVar()
    ttk.Entry(mainframe, textvariable = inp)\
        .grid(row = 0, column = 0)
    ttk.Button(mainframe, text = 'Save', command = save_inp)\
        .grid(row=1,column = 0)
    win.mainloop()