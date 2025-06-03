class Rectangle:
    def __init__(self, width, height):
        self.width = width    
        self.height = height  

    def get_square(self):
      
        return self.width * self.height

    def get_perimeter(self):
       
        return 2 * (self.width + self.height)

    def get_ratio(self):
       
        square = self.get_square()
        perimeter = self.get_perimeter()
        return square / perimeter if perimeter != 0 else 0 

