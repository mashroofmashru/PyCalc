import tkinter
from tkinter import *

window = Tk()
window.geometry("375x667")
window.title("Calculator")


def display(value):
    label = tkinter.Label(text=value, bg="#d3d3d3", font=("Arial", 40, "bold"), anchor=tkinter.E, padx=24, fg="#25265E")
    label.pack(expand=True, fill='both')



mainloop()
