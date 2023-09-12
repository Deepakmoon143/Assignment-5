class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
z = int(input("Enter the value of z: "))

obj = Point(x, y, z)

result = obj.sqSum()
print(f"The sum of squares is: {result}")  