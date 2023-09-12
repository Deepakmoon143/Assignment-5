class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):

        return self.x / self.y

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

obj = Calculator(x, y)

add_result = obj.add()
sub_result = obj.subtract()
mult_result = obj.multiply()
div_result = obj.divide()

print(f"Addition: {add_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {mult_result}")
print(f"Division: {div_result}")
