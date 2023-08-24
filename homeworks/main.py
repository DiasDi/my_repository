import math
import random

from homework import cm_to_m
from homework import kg_to_tonn
from homework import byte_to_kilobyte

class Soda:
    def __init__(self, addition):
        if isinstance(addition, str):
            self.addition = addition
        else:
            self.addition = None

    def show_my_drink(self):
        if self.addition:
            print(f'Lemonade with {self.addition} additions')
        else:
            print('Simple soda without any additions')

cm_to_m(random.randint(100, 10000))
kg_to_tonn(random.randint(1000, 10000))
byte_to_kilobyte(random.randint(1024, 10240))


without_addition_drink = Soda('')
lime_lemodane = Soda('lime')

without_addition_drink.show_my_drink()
lime_lemodane.show_my_drink()