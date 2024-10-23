import tkinter as tk
from tkinter import messagebox
import re

# Значение по умолчанию для операции
DEFAULT_OPERATION = "Сложение"

# Список доступных операций
OPERATIONS = [
    "Сложение",
    "Вычитание",
    "Умножение",
    "Деление",
]

# Словарь для сопоставления выбора функции
OPERATION_FUNCTIONS = {
    "Сложение": lambda x, y: x + y,
    "Вычитание": lambda x, y: x - y,
    "Умножение": lambda x, y: x * y,
    "Деление": lambda x, y: x / y if y != 0 else float("inf"),
}

# Список для хранения истории операций
operation_history = []


def calculate():
    try:
        num1_str = entry_num1.get().replace(",", ".")
        num2_str = entry_num2.get().replace(",", ".")

        if not re.match(r"^-?\d+(\.\d+)?$", num1_str) or not re.match(
            r"^-?\d+(\.\d+)?$", num2_str
        ):
            raise ValueError("Некорректный ввод")

        if not num1_str:
            raise ValueError("Поле ввода первого числа пустое")
        if not num2_str:
            raise ValueError("Поле ввода второго числа пустое")

        num1 = float(num1_str)
        num2 = float(num2_str)
        operation = operation_var.get()

        if operation in OPERATION_FUNCTIONS:
            result = OPERATION_FUNCTIONS[operation](num1, num2)
            if result == float("inf"):
                raise ZeroDivisionError("Деление на ноль недопустимо.")
            label_result.config(text=f"Результат: {result}")
            operation_history.append(f"{num1} {operation} {num2} = {result}")
            update_history()
        else:
            messagebox.showerror("Ошибка", "Выберите операцию")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))
    except ZeroDivisionError as e:
        messagebox.showerror("Ошибка", str(e))


def swap_numbers():
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    entry_num1.delete(0, tk.END)
    entry_num1.insert(0, num2)
    entry_num2.delete(0, tk.END)
    entry_num2.insert(0, num1)


def update_history():
    history_text.set("\n".join(operation_history[-10:]))


root = tk.Tk()
root.minsize(400, 600)
root.title("Калькулятор")
root.configure(bg="#f0f0f0")
root.option_add("*Font", "Helvetica 14")

label_num1 = tk.Label(root, text="Введите первое число:", bg="#f0f0f0", fg="#333")
label_num1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_num1 = tk.Entry(root, bd=2, relief="solid", font="Helvetica 14")
entry_num1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

label_num2 = tk.Label(root, text="Введите второе число:", bg="#f0f0f0", fg="#333")
label_num2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_num2 = tk.Entry(root, bd=2, relief="solid", font="Helvetica 14")
entry_num2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

operation_var = tk.StringVar(root)
operation_var.set(DEFAULT_OPERATION)

label_operation = tk.Label(root, text="Выберите операцию:", bg="#f0f0f0", fg="#333")
label_operation.grid(row=2, column=0, padx=10, pady=10, sticky="w")
option_menu = tk.OptionMenu(root, operation_var, *OPERATIONS)
option_menu.config(font="Helvetica 14", bd=2, relief="solid")
option_menu.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

button_calculate = tk.Button(
    root,
    text="Вычислить",
    command=calculate,
    bg="#007acc",
    fg="white",
    bd=0,
    padx=10,
    pady=10,
    activebackground="#005f99",
    highlightthickness=0,
)
button_calculate.configure(borderwidth=1, relief="flat")
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=20, sticky="nsew")
button_calculate.config(
    font="Helvetica 14",
    highlightbackground="#007acc",
    highlightcolor="#007acc",
    activeforeground="white",
)

button_swap = tk.Button(
    root,
    text="Поменять числа местами",
    command=swap_numbers,
    bg="#4caf50",
    fg="white",
    bd=0,
    padx=10,
    pady=10,
    activebackground="#388e3c",
    highlightthickness=0,
)
button_swap.configure(borderwidth=1, relief="flat")
button_swap.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
button_swap.config(
    font="Helvetica 14",
    highlightbackground="#4caf50",
    highlightcolor="#4caf50",
    activeforeground="white",
)

label_result = tk.Label(root, text="Результат: ", bg="#f0f0f0", fg="#333")
label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")

history_text = tk.StringVar()
label_history = tk.Label(root, text="История операций:", bg="#f0f0f0", fg="#333")
label_history.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="w")
history_label = tk.Label(
    root,
    textvariable=history_text,
    justify="left",
    bg="#ffffff",
    fg="#333",
    bd=2,
    relief="solid",
    font="Helvetica 12",
    padx=10,
    pady=10,
)
history_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
for i in range(8):
    root.rowconfigure(i, weight=1)

root.mainloop()
