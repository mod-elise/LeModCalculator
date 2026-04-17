import tkinter as tk
import tkinter.font as tkfont
import math

# ----------- CALCULATOR LOGIC ----------- #

def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return (0, False)
    else:
        return (x / y, True)

def percent(x):
    return x / 100

def square(x):
    return x * x

def square_root(x):
    if x < 0:
        return (0, False)
    return (math.sqrt(x), True)

def factorial(x):
    if x < 0:
        return (0, False)
    total = 1
    for i in range(1, int(x) + 1):
        total *= i
    return (total, True)


#------------------- USER INTERFACE -----------------#

def press (value):
    if value == '=':
        calculate(entry.get())
    else:
        entry.insert(tk.END, value)

buttons = [
    ('7',1,0),      ('8',1,1),      ('9',1,2),        (' / ',1,3),
    ('4',2,0),      ('5',2,1),      ('6',2,2),        (' * ',2,3),
    ('1',3,0),      ('2',3,1),      ('3',3,2),        (' - ',3,3),
    ('0',4,0),      ('.',4,1),      ('=',4,2),        (' + ',4,3),
]

root = tk.Tk()
root.title("LeMod Calculator")
btnFont = tkfont.Font(family='Arial', size=12)

for (text, row, col) in buttons:
    tk.Button(
        root,
        text=text,
        width=10,
        height=4,
        font=btnFont,
        command=lambda t=text: press(t)
    ).grid(row=row, column=col)

entry = tk.Entry(root, width=34, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

root.mainloop()
