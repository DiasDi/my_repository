# У вас есть класс Car с атрибутами: модель и цвет.Добавьте новый класс Грузовик и сделайте его классом наследником класса Car.
# В классе Грузовик создайте переменные: количество колес и максимальный вес. Создайте метод newWheels,
# который будет устанавливать значение в переменную "количество колёс" и выводить все данные из класса в
# консоль.
# Также создайте конструктор в главном классе для присвоения всех переменных. В классе наследнике
# создайте конструктор, устанавливающий все значения в конструктор главного класса и дополнительно
# переменные в класс Грузовик.

class Car:
    def __init__(self, model, color):
        self.__model = model
        self.__color = color
    
    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color
    
    def set_model(self, new_model):
        if isinstance(new_model, str):
            self.__model = new_model
        else:
            print('Incorrect. Must be string')
    
    def set_color(self, new_color):
        if isinstance(new_color, str):
            self.__color = new_color
        else:
            print('Incorrect. Must be string')

class Truck(Car):
    def __init__ (self, wheels, weight, model, color):
        super().__init__(model, color)
        self.__wheels = wheels
        self.__weight = weight

    def get_weight(self):
        return self.__weight
    
    def get_wheels(self):
        return self.__wheels

    def set_weight(self, new_wheels):
        if isinstance(new_wheels, int):
            self.__wheels = new_wheels
        else:
            print('Incorrect. Must be int')
    
    def set_wheels(self, new_weigth):
        if isinstance(new_weigth, int):
            self.__weight = new_weigth
        else:
            print('Incorrect. Must be int')

    def get_data(self):
        return f'{self.__weight} kg with {self.__wheels} wheels'

Nissan=Truck(4, 1000, 'X-Trail','g')
print(Nissan.get_model(), Nissan.get_color(), Nissan.get_data())