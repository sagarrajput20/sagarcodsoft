import tkinter as tk

class SagarCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sagar Calculator")
        self.window.geometry('361x458')
        self.window.configure(background="#1e2128")

        self.text_input = tk.StringVar()
        self.expression = ""

        self.create_ui()
        self.create_buttons()

        self.window.mainloop()

    def create_ui(self):
        entry = tk.Entry(self.window, width=17, bg='#292c33', fg='white')
        entry.config(font=('Ink Free', 23, 'bold'), textvariable=self.text_input)
        entry.place(x=0, y=132, height=70)

        label = tk.Label(self.window, text='Enter the Expression:', fg='white', bg='#34373d', font=('Arial', 14))
        label.place(x=0, y=0, height=130, width=360)

    def create_buttons(self):
        buttons_data = [
            ('1', 12, 340), ('2', 85, 340), ('3', 158, 340),
            ('4', 12, 280), ('5', 85, 280), ('6', 158, 280),
            ('7', 12, 220), ('8', 85, 220), ('9', 158, 220),
            ('0', 12, 400), ('+', 158, 400), ('-', 228, 280),
            ('*', 295, 280), ('/', 228, 340), ('%', 295, 340),
            ('.', 85, 400)
        ]

        for data in buttons_data:
            text, x, y = data
            self.create_button(text, x, y)

        equal_button = tk.Button(self.window, text='=', cursor="hand2", command=self.equal)
        equal_button.config(font=('Ink Free', 20, 'bold'), fg='#f1a872', bg='#e66100', activebackground='#f28430', activeforeground='#f0e3da')
        equal_button.place(x=228, y=400, height=48, width=125)

        clear_button = tk.Button(self.window, font='Amiri', text='Clear', cursor="hand2", command=self.clear)
        clear_button.config(font=('Ink Free', 20, 'bold'), fg='#ffffff', bg='#34373d', activebackground='#444850', activeforeground='#C0C0C0')
        clear_button.place(x=228, y=220, height=48, width=125)

    def create_button(self, text, x, y):
        button = tk.Button(self.window, text=text, cursor="hand2", padx=19, pady=5, command=lambda t=text: self.click(t))
        button.config(font=('Ink Free', 20, 'bold'), fg='#f8d7bf', bg='#4b4d53', activebackground='#5a5c63', activeforeground='#C0C0C0')
        button.place(x=x, y=y, height=48, width=60)

    def click(self, num):
        self.expression += num
        self.text_input.set(self.expression)

    def clear(self):
        self.expression = ""
        self.text_input.set("")

    def equal(self):
        try:
            result = str(eval(self.expression))
            self.text_input.set(result)
            self.expression = ""
        except:
            self.text_input.set("error")
            self.expression = ""

if __name__ == '__main__':
    SagarCalculator()
