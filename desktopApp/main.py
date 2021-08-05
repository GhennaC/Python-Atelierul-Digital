import tkinter
from tkinter import *

window = tkinter.Tk()
window.title('Prima noastra aplicatie')
window.geometry('200x100')
"""label = tkinter.Label(window, text = 'TEXT').pack()
button = tkinter.Button(window, text = 'Click')
button.pack()

checkbox1 = IntVar()
checkbox2 = IntVar()
tkinter.Checkbutton(window, text='Text1', variable=checkbox1, onvalue=1, offvalue=0).grid(row=6, sticky=W)
tkinter.Checkbutton(window, text='Text2', variable=checkbox2, onvalue=0, offvalue=1).grid(row=7, sticky=W)"""

"""tkinter.Label(window, text="Username").grid(row=0)
tkinter.Entry(window).grid(row=0, column=1)
tkinter.Label(window, text="Password").grid(row=1)
tkinter.Entry(window, show='*').grid(row=1, column=1)"""

#tkinter.Checkbutton(window, text="Tine-ma minte").grid(columnspan=2)

def left_click(event):
    tkinter.Label(window, text='Left click!').pack()


def middle_click(event):
    tkinter.Label(window, text="Middle click!").pack()


def right_click(event):
    tkinter.Label(window, text="Right click!").pack()


def double_click(event):
    tkinter.Label(window, text="Double click!").pack()


frame1 = Frame(window, height=100, width=200)
window.bind("<Button-1>", left_click)
window.bind("<Button-2>", middle_click)
window.bind("<Button-3>", right_click)
frame1.bind("<Double 1>", double_click)
frame1.pack()

window.mainloop()
