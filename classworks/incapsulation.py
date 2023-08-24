class Human:
    def __init__(self, name, surname) -> None:
        self.__name = name 
        self.__surname = surname
    
    def get_name(self):
        return self.__name
    
    def get_surname(self):
        return self.__surname

    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print('Incorrect. Must be string') 
    
    def set_surname(self, new_surname):
        if isinstance(new_surname, str):
            self.__surname = new_surname
        else:
            print('Incorrect. Must be string')

tom = Human('Tom', 'Human')

#print(tom.__name)
#print(tom.__surname)

print(tom.get_name())
print(tom.get_surname())

tom.set_name(0)
tom.set_surname('Dias')
print(tom.get_surname())

