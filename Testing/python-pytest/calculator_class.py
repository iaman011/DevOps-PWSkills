class addition:
    def add (self,a,b):
        return a +b

class subtraction:
    def sub (self,a,b):
        return a-b

class multiply:
    def mul (self,a,b):
        return a*b

class Divide:
    def div(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
