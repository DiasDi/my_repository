class Human:
    def init(self,name=None,surname=None) -> None:
        self.__name=name
        self.__surname=surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        if isinstance(new_name,str):
            self.__name=new_name
        else:
            print('Имя должно быть корректного формата!')
        
tom=Human('Tom','Anderson')

print(tom.name)

tom.name='Tom2'

print(tom.name)