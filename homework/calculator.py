from kivy.core.window import Window
from kivymd.app import MDApp

class calculator(MDApp):
    def build(self):
        Window.size = (300, 400)
        self.current_input = "0"
        self.last_operator = None
        self.last_operand = None

        return

    def display(self):
        self.root.ids.display.text = self.current_input

    def number(self, value):
        if self.current_input == "0":
            self.current_input = value
        else:
            self.current_input += value
        self.display()

    def calculate(self):
        if self.last_operator is None or self.last_operand is None:
            return
        if self.last_operator == "+":
            self.current_input = str(float(self.last_operand) + float(self.current_input))
        elif self.last_operator == "-":
            self.current_input = str(float(self.last_operand) - float(self.current_input))
        elif self.last_operator == "×":
            self.current_input = str(float(self.last_operand) * float(self.current_input))
        elif self.last_operator == "÷":
            if self.current_input == "0":
                self.current_input = "Error"
            else:
                self.current_input = str(float(self.last_operand) / float(self.current_input))
        self.last_operator = None
        self.last_operand = None
        self.display()


    def operator(self,operator):
        if self.last_operand is not None:
            self.calculate()
        self.last_operator = operator
        self.last_operand = self.current_input
        self.current_input = "0"

    def clear(self):
        self.current_input = "0"
        self.display()

    def negate(self):
        if self.current_input.startswith("-"):
            self.current_input = self.current_input[1:]
        else:
            self.current_input = "-" + self.current_input
        self.display()

    def percent(self):
        self.current_input = str(float(self.current_input) / 100)
        self.display()

    def decimal(self):
        if "." not in self.current_input:
            self.current_input += "."
        self.display()

t = calculator()
t.run()
