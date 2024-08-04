import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Básica")

        self.input_text = tk.StringVar()

        # Entry para mostrar los valores
        self.entry = tk.Entry(root, textvariable=self.input_text, font=("Arial", 18), justify="right", state="disabled")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Lista de botones y sus respectivas posiciones en la matriz
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0),
        ]

        # Crear botones y agregarlos a la ventana
        for label, row, col in buttons:
            btn = tk.Button(root, text=label, font=("Arial", 18), command=lambda lbl=label: self.on_button_click(lbl))
            btn.grid(row=row, column=col, sticky="nsew")

        # Hacer que las columnas y filas se expandan al ajustar la ventana
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.input_text.get())
                self.input_text.set(str(result))
            except:
                self.input_text.set("Error")
        elif value == "C":
            self.input_text.set("")
        else:
            self.input_text.set(self.input_text.get() + value)

# Crear la ventana principal
root = tk.Tk()
root.resizable(False, False)

# Crear la calculadora
calc = Calculadora(root)

# Ejecutar la ventana
root.mainloop()
