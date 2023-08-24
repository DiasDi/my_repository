class Snow:
    def __init__(self, quantity):
        self.quantity = int(quantity)
 
    def __add__(self, n):
        return self.quantity + n
    def __sub__(self, n):
        return self.quantity - n
    def __mul__(self, n):
        return self.quantity * n
    def __truediv__(self, n):
        return self.quantity / n
    
    def makeSnow(self, quantity_of_snowflakes):
        string_value = ""
        row = int(self.quantityr_of_snowflakes)//quantity_of_snowflakes
        for i in range(row):
            string_value += ("*" * quantity_of_snowflakes)
            string_value += "\n"
        rest_of_snowflakes = (int(self.quantity) - row * quantity_of_snowflakes)
        string_value += "*" * rest_of_snowflakes
        return string_value
