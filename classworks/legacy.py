class Vehicle:
    def __init__(self,color, wheels) -> None:
        self.color=color
        self.__wheels=wheels

    def get_color(self):
        return self.__color
    
    def get_wheels(self):
        return self.__wheels

    def set_wheels(self,new_wheels):
        self.__wheels=new_wheels

    def set_color(self,new_color):
        self.__color=new_color

    def get_all_atributes(self):
        print(f'{self.__wheels}, {self.__color}')

class Car(Vehicle):

    def __init__(self, model,speed,color, wheels) -> None:
        super().init(color, wheels)
        self.__model=model
        self.__speed=speed

    def get_model(self):
        return self.__model

    def get_speed(self):
        return self.__speed

    def ride(self):
        print('Машина едет')

Nissan=Car('X-Trail',90,'g',4)
Nissan.ride()
Nissan.get_all_atributes()