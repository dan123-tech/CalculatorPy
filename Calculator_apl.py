import tkinter as tk
from tkinter import messagebox
import math



class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.entry = tk.Entry(master, width=30)
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        self.bind_keyboard_events()
        menubar = tk.Menu(master)
        master.config(menu=menubar)

        mod_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Mod", menu=mod_menu)
        mod_menu.add_command(label="Calculator Stiintific", command=self.calc_st)
        mod_menu.add_command(label="Convertor", command=self.convertor)

        setari_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Setari", menu=setari_menu)
        setari_menu.add_command(label="Exit", command=self.exit_app)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+', '='
        ]

        row = 2
        col = 0

        for button in buttons:
            if button == '=':
                tk.Button(master, text=button, width=7, command=self.calculate).grid(row=row, column=col, columnspan=2)
            else:
                if button == '+':
                    action = lambda b=button: self.entry.insert(tk.END, ' ' + b + ' ')
                else:
                    action = lambda b=button: self.entry.insert(tk.END, b)
                tk.Button(master, text=button, width=7, command=action).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def calc_st(self):
        root_scientific = tk.Toplevel(self.master)
        calculator_scientific = ScientificCalculator(root_scientific)

    def convertor(self):
        root_scientific = tk.Toplevel(self.master)
        calculator_scientific = ConverterCalculator(root_scientific)

    def bind_keyboard_events(self):
        for char in '0123456789*/-+.':
            self.master.bind(char, lambda event, char=char: self.handle_key_press(char))
        self.master.bind('<Return>', lambda event: self.calculate())

    def handle_key_press(self, char):
        self.entry.insert(tk.END, char)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")

    def exit_app(self):
        self.master.quit()


class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator Științific")
        menubar = tk.Menu(master)
        master.config(menu=menubar)

        self.entry = tk.Entry(master, width=30)
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4), ('cos', 1, 5),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('tan', 2, 4), ('log', 2, 5),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('sqrt', 3, 4), ('^', 3, 5),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('(', 4, 4), (')', 4, 5),
            ('C', 5, 0), ('pi', 5, 1), ('e', 5, 2), ('DEL', 5, 3), ('Grf', 5, 4)
        ]

        for button_text, row, col in buttons:
            action = lambda b=button_text: self.on_button_click(b)
            tk.Button(master, text=button_text, width=5, command=action).grid(row=row + 1, column=col)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == 'DEL':
            current_text = self.entry.get()[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current_text)
        elif text == 'C':
            self.entry.delete(0, tk.END)
        elif text == 'sqrt':
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, math.sqrt(float(current_text)))
        elif text == 'pi':
            self.entry.insert(tk.END, math.pi)
        elif text == 'e':
            self.entry.insert(tk.END, math.e)
        elif text in ['sin', 'cos', 'tan', 'log']:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(eval('math.' + text + '(' + current_text + ')')))
       # elif text == 'Grf':
            #self.open_graph_calc()

        else:
            self.entry.insert(tk.END, text)

    def open_graph_calc(self):
        root_graph = tk.Toplevel(self.master)
        calculator_graph = GraphCalc(root_graph)


class ConverterCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator Convertor")
        self.entry = tk.Entry(master, width=30)
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        buttons = [
            ('C', 1, 0), ('F', 1, 1), ('K', 1, 2), ('cm', 1, 3), ('m', 1, 4), ('km', 1, 5),
            ('kg', 2, 0), ('g', 2, 1), ('lb', 2, 2), ('m/s', 2, 3), ('km/h', 2, 4), ('mi/h', 2, 5)
        ]

        for button_text, row, col in buttons:
            action = lambda b=button_text: self.on_button_click(b)
            tk.Button(master, text=button_text, width=5, command=action).grid(row=row + 2, column=col)

    def on_button_click(self, text):
        current_text = self.entry.get()
        if text == 'C':
            self.entry.delete(0, tk.END)
        elif text == 'F':
            result = (float(current_text) * 9/5) + 32
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif text == 'K':
            result = float(current_text) + 273.15
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif text == 'cm':
            result = float(current_text) / 100
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif text == 'm':
            result = float(current_text)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif text == 'km':
            result = float(current_text) * 1000
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif text == 'kg':
            result = float(current_text)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif text == 'g':
            result = float(current_text) * 1000
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif text == 'lb':
            result = float(current_text) * 2.20462
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif text == 'm/s':
            result = float(current_text)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif text == 'km/h':
            result = float(current_text) * 3.6
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        elif text == 'mi/h':
            result = float(current_text) * 2.23694
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))




root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
