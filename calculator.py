import math
import tkinter as tk
from tkinter import ttk


SAFE_NAMES = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sqrt": math.sqrt,
    "log": math.log10,
    "ln": math.log,
    "exp": math.exp,
    "abs": abs,
    "pi": math.pi,
    "e": math.e,
}


def safe_eval(expression: str) -> float:
    expression = expression.replace("^", "**")
    return eval(expression, {"__builtins__": {}}, SAFE_NAMES)


class ScientificCalculator(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Scientific Calculator")
        self.resizable(False, False)

        self.expression_var = tk.StringVar()
        self.result_var = tk.StringVar(value="0")

        self._build_ui()

    def _build_ui(self) -> None:
        container = ttk.Frame(self, padding=10)
        container.grid(row=0, column=0, sticky="nsew")

        expression_entry = ttk.Entry(
            container,
            textvariable=self.expression_var,
            font=("Helvetica", 14),
            justify="right",
            width=30,
        )
        expression_entry.grid(row=0, column=0, columnspan=6, pady=(0, 6), sticky="ew")
        expression_entry.focus_set()
        expression_entry.bind("<Return>", lambda _e: self.calculate())

        result_label = ttk.Label(
            container,
            textvariable=self.result_var,
            font=("Helvetica", 16, "bold"),
            anchor="e",
            width=30,
        )
        result_label.grid(row=1, column=0, columnspan=6, pady=(0, 10), sticky="ew")

        buttons = [
            ["C", "DEL", "(", ")", "^", "/"],
            ["sin(", "cos(", "tan(", "sqrt(", "log(", "*"],
            ["7", "8", "9", "asin(", "acos(", "-"],
            ["4", "5", "6", "atan(", "ln(", "+"],
            ["1", "2", "3", "pi", "e", "."],
            ["0", "00", "abs(", "exp(", "=", ""],
        ]

        for r, row in enumerate(buttons, start=2):
            for c, label in enumerate(row):
                if not label:
                    continue
                ttk.Button(
                    container,
                    text=label,
                    command=lambda value=label: self.on_button_click(value),
                    width=8,
                ).grid(row=r, column=c, padx=2, pady=2, sticky="nsew")

        for col in range(6):
            container.columnconfigure(col, weight=1)

    def on_button_click(self, value: str) -> None:
        if value == "C":
            self.expression_var.set("")
            self.result_var.set("0")
            return

        if value == "DEL":
            current = self.expression_var.get()
            self.expression_var.set(current[:-1])
            return

        if value == "=":
            self.calculate()
            return

        self.expression_var.set(self.expression_var.get() + value)

    def calculate(self) -> None:
        expression = self.expression_var.get().strip()
        if not expression:
            self.result_var.set("0")
            return

        try:
            result = safe_eval(expression)
            self.result_var.set(str(result))
        except Exception:
            self.result_var.set("Error")


def main() -> None:
    app = ScientificCalculator()
    app.mainloop()


if __name__ == "__main__":
    main()
