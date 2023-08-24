class Character:
    def __init__(self, name, class_type, health, damage):
        self.__name = name
        self.__class_type = class_type
        self.__health = health
        self.__damage = damage

    def get_name(self):
        return self.__name

    def get_class_type(self):
        return self.__class_type

    def get_health(self):
        return self.__health

    def get_damage(self):
        return self.__health

    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print('Неправильный ввод данных. Введите свое имя')
    
    def set_class_type(self, new_class_type):
        print('')

class Skills:


    def set_health(self, new_health):
        if isinstance(new_health, int) and new_health <= 100:
            self.__health = new_health
        else:
            print('Неправильный ввод данных. Числовые значения равно или меньше 100')
    
    def set_damage(self, new_damage):
        if isinstance(new_damage, int) and new_damage <= 30:
            self.__health = new_health
        else:
            print('Неправильный ввод данных. Числовые значения равно или меньше 30')

class Enemy:
    hp = randint(10, 200)
    damage = randint(1, 15)

class World:
    def __init__ (self, bosses, characters, items):
        self.__bosses = bosses
        self.__characters = characters
        self.__items = items

mini_world = World([Character('Гуль', 100, 5), Character('Бес', 100, 5), Character('Брукса', 100, 5), Character('Василиск', 100, 5), 
                    Character('Кикимора', 100, 5), Character('Великан', 100, 5), Character('Тролль', 100, 5), Character('Накер', 100, 5), 
                    Character('Призрак', 100, 5), Character('Суккуб', 100, 5), Character('Циклоп', 100, 5), Character('Эхидна', 100, 5)],
                    Item())