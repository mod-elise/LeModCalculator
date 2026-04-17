import tkinter as tk
import tkinter.font as tkfont
import math


# ----------- CALCULATOR LOGIC ----------- #
def multiply(x, y):
    result = x * y
    return result

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return (0, True)
    else:
        return (x / y, False)

def percent(x):
    return x / 100

def square(x):
    return x * x

def square_root(x):
    if x < 0:
        return (0, True)
    return (math.sqrt(x), False )


def factorial(x):
    if x < 0:
        return (0, True)
    total = 1
    for i in range(1, int(x) + 1):
        total *= i
    return (total, False)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def validator (numbers, operators):
    validOperators = ['*', '/', '+', '-', '%', 'x²', '√', '!', 'sin', 'cos', 'tan']
    err = False
    operandValidation = {
        '*': 2,
        '+': 2,
        '/': 2,
        '-': 2,
        '%': 1,
        'x²': 1,
        '√': 1,
        '!': 1,
        'sin': 1,
        'cos': 1,
        'tan': 1
    }

    if len(operators) != 1 or operators[0] not in validOperators:
        err = True
    try:
        operator = operators[0]
    except:
        operator = '*'

    if operandValidation[operator] != len(numbers):
        err = True
    return numbers, operator, err

def evaluator (calculation):
    numbers = []
    operators = []
    processed = calculation.split(' ')
    processed = [x for x in processed if x.strip()]
    for item in processed:
        try:
            numerical = float(item)
            numbers.append(numerical)
        except:
            operators.append(item)

    return numbers, operators

def calculate(inputString):
    numbers, operators = evaluator(inputString)
    operands, operator, err = validator(numbers, operators)
   
    if err:
        return "-- Error --"
    else:
        match operator:
            case '*':
                return multiply(operands[0],operands[1])
            case '+':
                return add(operands[0], operands[1])
            case '-':
                return subtract(operands[0], operands[1])
            case '/':
                result, err = divide(operands[0], operands[1])
                if err:
                    return "-- Error --"
                else:
                    return result
            
            case '%':
                return percent(operands[0])
            case '!':
                result, err =  factorial(operands[0])
                if err:
                    return "-- Error --"
                else:
                    return result
            case 'x²':
                return square(operands[0])
            case '√':
                result, err =  square_root(operands[0])
                if err:
                    return "-- Error --"
                else:
                    return result
            case 'sin':
                return sin(operands[0])
            case 'cos':
                return cos(operands[0])
            case 'tan':
                return tan(operands[0])
     
#------------------- USER INTERFACE -----------------#

def press (value):
    match value:
        case 'C':        
            entry.delete(0, tk.END)
        case '=':
            calculation = entry.get()
            entry.delete(0, tk.END)
            entry.insert(tk.END, calculate(calculation))
        case 'π':
            entry.insert(tk.END, " 3.1416 ")
        case 'τ':
            entry.insert(tk.END, " 6.2832 ")
        case '𝒆':
            entry.insert(tk.END, " 2.7183 ")
        case 'ϕ':
            entry.insert(tk.END, " 1.618 ")
        case _:
            entry.insert(tk.END, value)

buttons = [
    (' x² ',1,0),    (' √ ',1,1),    (' ! ',1,2),     ('C',1,3),
    (' sin ',2,0),  (' cos ',2,1),  (' tan ',2,2),    (' % ',2,3),      
    ('7',3,0),      ('8',3,1),      ('9',3,2),        (' / ',3,3),
    ('4',4,0),      ('5',4,1),      ('6',4,2),        (' * ',4,3),
    ('1',5,0),      ('2',5,1),      ('3',5,2),        (' - ',5,3),
    ('0',6,0),      ('.',6,1),      ('=',6,2),        (' + ',6,3),
    ('π',7,0),      ('𝒆',7,1),      ('τ',7,2),        ('ϕ',7,3),
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
