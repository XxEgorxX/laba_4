import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius  

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_circumference(self):
        return 2 * math.pi * self.__radius

circle = Circle(5)

print(f"Площадь круга: {circle.get_area():.2f}")          
print(f"Длина окружности: {circle.get_circumference():.2f}")  