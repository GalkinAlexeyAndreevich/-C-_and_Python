from tkinter import *

root = Tk()
root["bg"] = "#000"
root.geometry("485x515")
root.title("Калькулятор")
root.resizable(False, False)


def calculator(operation):
    global formula # Глобальная переменная для сохранения значения всей строки

    if operation == "C":
        formula = ""
    elif operation == "DEL":
        formula = formula[0:-1]
    elif operation == "=":
        try:
            if eval(formula) % 1 == 0:
                formula = str(round(eval(formula)))
            else:
                formula = str(eval(formula))
        except ZeroDivisionError:
            formula = "На ноль делить нельзя"
    else:
        if formula == "0":
            formula = ""
        formula += operation
    lbl.configure(text=formula) # изменение значения lbl после вычисления


formula = "0"
lbl = Label(root, text=formula, font=("Times New Roman", 30), bg="black", fg="white")
lbl.place(x=11, y=25)
btns = [
    "C", "DEL", "*", "=",
    "1", "2", "3", "/",
    "4", "5", "6", "+",
    "7", "8", "9", "-",
    "(", "0", ")", "."
    ]
x = 10
y = 100
for bt in btns:
    lbl_but = lambda x=bt: calculator(x)
    Button(text=bt, bg="orange", font=("Times New Roman", 15),
            command=lbl_but).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400: # Переход кнопок на новую строку
        x = 10
        y += 81



root.mainloop()