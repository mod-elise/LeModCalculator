import tkinter as tk
import tkinter.font as tkfont
import math
import math

def Multiply(x, y):
    result = x * y
    return result


def add(x, y):
    result = x + y
    return result
   


def subtract(x, y):
    result = x - y
    return result

def validator (numbers, operators):
    validOperators = ['*', '/', '+', '-', '%', 'x²', '√' ,'sin', 'cos', 'tan']
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
    for item in processed:
        # isnumeric is a problem because of decimals
        if item.isnumeric():           
            numbers.append(item)
        else:
            operators.append(item)
    return numbers, operators

def calculate(inputString):
    numbers, operators = evaluator(inputString)
    numbers, operator, err = validator(numbers, operators)
    operands = [float(x) for x in numbers]
   
    if err:
        return "-- Error --"
    else:
        match operator:
            case '*':
                return Multiply(operands[0],operands[1])
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
                return factorial(operands[0])
            case 'x²':
                return square(operands[0])
            case '√':
                return squareRoot(operands[0])
            case 'sin':
                return sin(operands[0])
            case 'cos':
                return cos(operands[0])
            case 'tan':
                return tan(operands[0])
     
#------------------- USER INTERFACE -----------------#

def press (value):
    if value == 'C':
        entry.delete(0, tk.END)
    elif value == '=':
        calculation = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, calculate(calculation))
    else:
        entry.insert(tk.END, value)

buttons = [
    (' x² ',1,0),    (' √ ',1,1),    (' ! ',1,2),     ('C',1,3),
    (' sin ',2,0),  (' cos ',2,1),  (' tan ',2,2),    (' % ',2,3),      
    ('7',3,0),      ('8',3,1),      ('9',3,2),        (' / ',3,3),
    ('4',4,0),      ('5',4,1),      ('6',4,2),        (' * ',4,3),
    ('1',5,0),      ('2',5,1),      ('3',5,2),        (' - ',5,3),
    ('0',6,0),      ('.',6,1),      ('=',6,2),        (' + ',6,3),
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
