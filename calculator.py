class calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "division by 0"
        return a / b
calc = calculator()
print(calc.add(5, 3))
