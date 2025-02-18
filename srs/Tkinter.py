import tkinter as tk


def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except:
        entry_var.set("Ошибка")


root = tk.Tk()
root.title("Калькулятор")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, font=("Arial", 20), width=5, height=2,
                  command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, font=("Arial", 20), width=5, height=2,
                  command=lambda b=button: entry_var.set(entry_var.get() + b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
