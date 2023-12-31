import tkinter
from tkinter import *

window = Tk()
window.geometry("370x470")
window.title("Calculator")
window.configure(bg="light gray")

operator = ""
buttonclick = ""
oldValue = ""
newvalue = ""
result = ""


def button_clicked(btnValue):
    global buttonclick
    buttonclick = buttonclick + str(btnValue)
    input_text.set(buttonclick)
    result = (eval(buttonclick))
    input_text2.set(result)


input_text = StringVar()
input_text2= StringVar()


def equal_btnclick():
    result = (eval(buttonclick))
    input_text.set(result)



def clear_input():
    global buttonclick
    buttonclick = ""
    input_text.set(buttonclick)


# display--------------------------------------------------
Display_frame = Frame(window)
Display_frame.pack()
label = tkinter.Label(Display_frame, textvariable=input_text, width=28, bg="light gray", font=("Arial", 30, "bold"),
                      anchor=tkinter.E,
                      padx=24, pady=20, fg="#000000")
label1 = tkinter.Label(Display_frame, textvariable=input_text2, width=48, bg="light gray", font=("Arial", 40, "bold"),
                      anchor=tkinter.E,
                      padx=24, pady=20, fg="#000000")
label.pack(expand=True, fill='both')
label1.pack(expand=True, fill='both')

# button--------------------------------------------------
button_frame = Frame(window, bg="light gray", height=221, pady=0, padx=1)
button_frame.pack(expand=True, fill="both")

# firstRow-------------------------------------------------
add = Button(button_frame, text="+", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
             command=lambda: button_clicked("+")).grid(row=1, column=0, padx=1, pady=1)

sub = Button(button_frame, text="-", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
             command=lambda: button_clicked("-")).grid(row=1, column=1, padx=1, pady=1)

multi = Button(button_frame, text="x", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
               command=lambda: button_clicked("*")).grid(row=1, column=2, padx=1, pady=1)

div = Button(button_frame, text="/", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
             command=lambda: button_clicked("/")).grid(row=1, column=3, padx=1, pady=1)

# secondRow----------------------------------------------------------
seven = Button(button_frame, text="7", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
               command=lambda: button_clicked("7")).grid(row=2, column=0, padx=1, pady=1)

eight = Button(button_frame, text="8", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
               command=lambda: button_clicked("8")).grid(row=2, column=1, padx=1, pady=1)

nine = Button(button_frame, text="9", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
              command=lambda: button_clicked("9")).grid(row=2, column=2, padx=1, pady=1)

# ThirdRow-----------------------------------------------
four = Button(button_frame, text="4", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
              command=lambda: button_clicked("4")).grid(row=3, column=0, padx=1, pady=1)

five = Button(button_frame, text="5", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
              command=lambda: button_clicked("5")).grid(row=3, column=1, padx=1, pady=1)

six = Button(button_frame, text="6", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
             command=lambda: button_clicked("6")).grid(row=3, column=2, padx=1, pady=1)

# fourthRow-----------------------------------------------
one = Button(button_frame, text="1", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
             command=lambda: button_clicked("1")).grid(row=4, column=0, padx=1, pady=1)

two = Button(button_frame, text="2", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
             command=lambda: button_clicked("2")).grid(row=4, column=1, padx=1, pady=1)

three = Button(button_frame, text="3", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
               command=lambda: button_clicked("3")).grid(row=4, column=2, padx=1, pady=1)

# fifthRow-----------------------------------------------
zero = Button(button_frame, text="0", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
              command=lambda: button_clicked("0")).grid(row=5, column=0, padx=1, pady=1)
dot = Button(button_frame, text=".", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
             command=lambda: button_clicked(".")).grid(row=5, column=1, padx=1, pady=1)

clear = Button(button_frame, text="CA", fg="#25265E", width=12, height=3, bd=0, bg="#F5F5F5", cursor="hand2",
               command=lambda: clear_input()).grid(row=5, column=2, padx=1, pady=1)

# equalRow-----------------------------------------------
equal = Button(button_frame, text="=", fg="#25265E", width=12, height=14, bd=0, bg="#F5F5F5", cursor="hand2",
               command=lambda: equal_btnclick()).grid(row=2, rowspan=4, column=3, padx=1, pady=1)

mainloop()
