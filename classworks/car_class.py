# Создайте класс Автомобиль (Car) со следующими характеристиками: вес автомобиля (weigth), марка 
# автомобиля (model), цвет автомобиля (color, обозначить одним символом) и его скорость(speed). Создайте 
# метод, который будет выводить характеристики автомобиля на экран

class Car:
    def __init__(self, weigth, model, color, speed):
        self.__weigth = weigth
        self.__model = model
        self.__color = color
        self.__speed = speed
    
    def get_speed(self):
        return self.__speed

    def get_weigth(self):
        return self.__weigth

    def get_model(self):
        return self.__model
    
    def get_color(self):
        return self.__color
#по отдельности
    def set_model(self, new_model):
        if isinstance(new_model, str):
            self.__model = new_model
        else:
            print('Incorrect. Must be string')

    def set_speed(self, new_speed):
        if isinstance(new_speed, int):
            self.__speed = new_speed
        else:
            print('Incorrect. Must be string')
    
    def set_weigth(self, new_weigth):
        if isinstance(new_weigth, int):
            self.__weigth = new_weigth
        else:
            print('Incorrect. Must be string')
    
    def set_color(self, new_color):
        if len(new_color) == 1:
            self.__color = new_color
        else:
            print('Incorrect. Enter only one symbol')
#Одним полем
    def get_car_info(self):
        print(f'{self.__model} {self.__color} {self.__weigth} kg {self.__speed} km/h')

legacy = Car(2000, 'Nissan', 'silver', 300)

legacy.set_model('Nissan')
legacy.set_model(200)
legacy.set_color('Silver')
legacy.set_color('S')
legacy.get_car_info()