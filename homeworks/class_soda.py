class Soda:
    def __init__(self, addition:str = '') -> None:
        if isinstance(addition, str):
            self.addition = addition
        else:
            self.addition = None

    def show_my_drink(self):
        if self.addition:
            print(f'Lemonade with {self.addition} additions')
        else:
            print('Simple soda without any additions')

without_addition_drink = Soda()
lime_lemodane = Soda('lime')

without_addition_drink.show_my_drink()
lime_lemodane.show_my_drink()