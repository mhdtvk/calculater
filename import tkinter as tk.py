import tkinter as tk

from main_class import *

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.num1_label = tk.Label(master, text="Enter number 1:")
        self.num1_label.grid(row=0, column=0, padx=5, pady=5)

        self.num1_entry = tk.Entry(master)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        self.num2_label = tk.Label(master, text="Enter number 2:")
        self.num2_label.grid(row=1, column=0, padx=5, pady=5)

        self.num2_entry = tk.Entry(master)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('+', lambda: self.calculate('+')),
            ('-', lambda: self.calculate('-')),
            ('*', lambda: self.calculate('*')),
            ('/', lambda: self.calculate('/')),
            ('Clear', self.clear_entries)
        ]

        row_num = 3
        for button_text, command in buttons:
            button = tk.Button(self.master, text=button_text, command=command)
            button.grid(row=row_num, column=buttons.index((button_text, command)), padx=5, pady=5)
            row_num += 1

    def calculate(self, operator):
        num1 = float(self.num1_entry.get())
        num2 = float(self.num2_entry.get())

        calc = Calculation()
        calc.num1 = num1
        calc.num2 = num2

        if operator == '+':
            result = calc.sume()
        elif operator == '-':
            result = calc.tafrigh()
        elif operator == '*':
            result = calc.zarb()
        elif operator == '/':
            result = calc.taghsim()

        self.result_label.config(text=f"Result: {result}")

    def clear_entries(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_label.config(text="")

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
