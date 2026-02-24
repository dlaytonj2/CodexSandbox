import tkinter as tk
from tkinter import ttk

from calculator import add, subtract, multiply, divide


class CalculatorGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Calculator v2 (GUI)")
        self.root.resizable(False, False)

        self.first_var = tk.StringVar()
        self.second_var = tk.StringVar()
        self.op_var = tk.StringVar(value="+")
        self.result_var = tk.StringVar(value="Enter values and click Calculate")

        frame = ttk.Frame(root, padding=12)
        frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(frame, text="First number:").grid(row=0, column=0, sticky="w", pady=4)
        ttk.Entry(frame, textvariable=self.first_var, width=20).grid(row=0, column=1, pady=4)

        ttk.Label(frame, text="Operation:").grid(row=1, column=0, sticky="w", pady=4)
        ttk.Combobox(
            frame,
            textvariable=self.op_var,
            values=["+", "-", "*", "/"],
            state="readonly",
            width=17,
        ).grid(row=1, column=1, pady=4)

        ttk.Label(frame, text="Second number:").grid(row=2, column=0, sticky="w", pady=4)
        ttk.Entry(frame, textvariable=self.second_var, width=20).grid(row=2, column=1, pady=4)

        ttk.Button(frame, text="Calculate", command=self.calculate).grid(
            row=3, column=0, columnspan=2, pady=(8, 6), sticky="ew"
        )
        ttk.Label(frame, textvariable=self.result_var).grid(row=4, column=0, columnspan=2, sticky="w")

    def calculate(self) -> None:
        try:
            a = float(self.first_var.get().strip())
            b = float(self.second_var.get().strip())
        except ValueError:
            self.result_var.set("Error: Enter valid numbers.")
            return

        operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
        }

        op = self.op_var.get()
        if op not in operations:
            self.result_var.set("Error: Select a valid operation.")
            return

        try:
            result = operations[op](a, b)
        except ValueError as err:
            self.result_var.set(f"Error: {err}")
            return

        self.result_var.set(f"Result: {result}")


def main() -> None:
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
