# Создайте класс «Дом» (House) со следующими его характеристиками:
# • количество этажей (floors);
# • год постройки (year);
# • название (предназначение) дома (name);
# На основании класса «Дом» создайте два объекта и, используя метод класса, пропишите для каждого их 
# уникальные характеристики.
# Выведите информацию о каждом объекте, используя метод класса.
# Создайте метод, который будет показывать (возвращать) возраст дома (количество лет прошедших с момента 
# постройки дома по сегодняшний год)

class House:
    def __init__(self, floors, year_creation, type_name, name):
        self.__floors = floors
        self.__year_creation = year_creation
        self.__type_name = type_name
        self.__name = name
    
    def get_floors(self):
        return self.__floors
    
    def get_year(self):
        return self.__year_creation

    def get_type(self):
        return self.__type_name
    
    def get_name(self):
        return self.__name

    def get_age(self):
        print(2023 - self.__year_creation)        

    def set_floors(self, new_floors):
        if isinstance(new_floors, int):
            self.__floors = new_floors
        else:
            print('Incorrect. Must be int')

    def set_year(self, new_year):
        if isinstance(new_year, int):
            self.__year_creation = new_year
        else:
            print('Incorrect. Must be int')

    def set_type(self, new_type):
        if isinstance(new_type, str):
            self.__type_name = new_type
        else:
            print('Incorrect. Must be string')

    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print('Incorrect. Must be string')
        