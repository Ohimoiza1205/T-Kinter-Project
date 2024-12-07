import tkinter as tk
from math import sin, cos, tan, log, log10, sqrt, radians, factorial

class AdvancedCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Advanced Calculator")
        self.geometry("500x700")
        self.result_var = tk.StringVar()
        self.memory = 0
        self.create_widgets()

    def create_widgets(self):
        # Display area
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="sunken", justify="right")
        entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

        # Button definitions (with scientific functions)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('sin', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('cos', 4, 4),
            ('(', 5, 0), (')', 5, 1), ('log', 5, 2), ('tan', 5, 3), ('M+', 5, 4),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=("Arial", 18), bd=5, relief="raised", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        # Memory button
        mem_button = tk.Button(self, text="MRC", font=("Arial", 18), bd=5, relief="raised", command=self.recall_memory)
        mem_button.grid(row=6, column=0, columnspan=2, sticky="nsew")
        
        # Clear button
        clear_button = tk.Button(self, text="C", font=("Arial", 18), bd=5, relief="raised", command=self.clear)
        clear_button.grid(row=6, column=2, columnspan=2, sticky="nsew")

        # Make the grid cells expand evenly
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        current_text = self.result_var.get()

        if char == "=":
            try:
                # Evaluate the expression
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif char == 'sqrt':
            try:
                # Calculate square root
                result = sqrt(float(current_text))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif char == '^':
            self.result_var.set(current_text + '**')  # Handle exponentiation
        elif char in ['sin', 'cos', 'tan']:
            try:
                # Trigonometric functions (in radians)
                angle = radians(float(current_text))
                if char == 'sin':
                    result = sin(angle)
                elif char == 'cos':
                    result = cos(angle)
                elif char == 'tan':
                    result = tan(angle)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif char == 'log':
            try:
                result = log10(float(current_text))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif char == 'M+':
            # Memory store current value
            try:
                self.memory += float(current_text)
                self.result_var.set(f"Memory: {self.memory}")
            except Exception as e:
                self.result_var.set("Error")
        else:
            # Append the pressed button to the text entry
            self.result_var.set(current_text + char)

    def clear(self):
        self.result_var.set("")

    def recall_memory(self):
        self.result_var.set(str(self.memory))

if __name__ == "__main__":
    app = AdvancedCalculator()
    app.mainloop()
