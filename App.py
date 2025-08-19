import tkinter as tk

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total  # allow further calculations
    except:
        equation.set(" error ")
        expression = ""

# Function to clear input
def clear():
    global expression
    expression = ""
    equation.set("")

# main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

expression = ""
equation = tk.StringVar()

# input field
entry = tk.Entry(window, textvariable=equation, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# button layout
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
]

for (text, row, col) in buttons:
    if text == "=":
        b = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=equalpress)
    else:
        b = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: press(t))
    b.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_button = tk.Button(window, text="C", width=23, height=2, font=("Arial", 14), command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

window.mainloop()
