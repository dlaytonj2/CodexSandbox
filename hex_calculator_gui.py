import tkinter as tk
from tkinter import ttk


def parse_hex(value: str) -> int:
    cleaned = value.strip()
    if not cleaned:
        raise ValueError("Hex value is required.")
    if cleaned.lower().startswith("0x"):
        cleaned = cleaned[2:]
    return int(cleaned, 16)


class HexCalculatorGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Hexadecimal Calculator")
        self.root.resizable(False, False)

        self.first_var = tk.StringVar()
        self.second_var = tk.StringVar()
        self.op_var = tk.StringVar(value="+")
        self.result_hex_var = tk.StringVar(value="HEX: 0x0")
        self.result_dec_var = tk.StringVar(value="DEC: 0")
        self.result_bin_var = tk.StringVar(value="BIN: 0b0")

        frame = ttk.Frame(root, padding=12)
        frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(frame, text="First hex value:").grid(row=0, column=0, sticky="w", pady=4)
        ttk.Entry(frame, textvariable=self.first_var, width=24).grid(row=0, column=1, pady=4)

        ttk.Label(frame, text="Operation:").grid(row=1, column=0, sticky="w", pady=4)
        ttk.Combobox(
            frame,
            textvariable=self.op_var,
            values=["+", "-", "*", "/", "AND", "OR", "XOR", "<<", ">>"],
            state="readonly",
            width=21,
        ).grid(row=1, column=1, pady=4)

        ttk.Label(frame, text="Second hex value:").grid(row=2, column=0, sticky="w", pady=4)
        ttk.Entry(frame, textvariable=self.second_var, width=24).grid(row=2, column=1, pady=4)

        ttk.Button(frame, text="Calculate", command=self.calculate).grid(
            row=3, column=0, columnspan=2, pady=(8, 10), sticky="ew"
        )

        ttk.Label(frame, textvariable=self.result_hex_var, font=("Helvetica", 12, "bold")).grid(
            row=4, column=0, columnspan=2, sticky="w", pady=2
        )
        ttk.Label(frame, textvariable=self.result_dec_var).grid(
            row=5, column=0, columnspan=2, sticky="w", pady=2
        )
        ttk.Label(frame, textvariable=self.result_bin_var).grid(
            row=6, column=0, columnspan=2, sticky="w", pady=2
        )

    def calculate(self) -> None:
        try:
            a = parse_hex(self.first_var.get())
            b = parse_hex(self.second_var.get())
        except ValueError as err:
            self._set_error(str(err))
            return

        op = self.op_var.get()
        try:
            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                if b == 0:
                    raise ValueError("Cannot divide by zero.")
                result = a // b
            elif op == "AND":
                result = a & b
            elif op == "OR":
                result = a | b
            elif op == "XOR":
                result = a ^ b
            elif op == "<<":
                result = a << b
            elif op == ">>":
                result = a >> b
            else:
                raise ValueError("Unsupported operation.")
        except ValueError as err:
            self._set_error(str(err))
            return

        sign = "-" if result < 0 else ""
        abs_result = abs(result)
        self.result_hex_var.set(f"HEX: {sign}0x{abs_result:X}")
        self.result_dec_var.set(f"DEC: {result}")
        self.result_bin_var.set(f"BIN: {sign}0b{abs_result:b}")

    def _set_error(self, message: str) -> None:
        self.result_hex_var.set(f"Error: {message}")
        self.result_dec_var.set("DEC: -")
        self.result_bin_var.set("BIN: -")


def main() -> None:
    root = tk.Tk()
    HexCalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
