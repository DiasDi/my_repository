class Person:
    def __init__(self, fullname:str = None, address:str = None, phone:int = None) -> None:
        self.__fullname = fullname
        self.__address = address
        self.__phone = phone
    
    def get_name(self):
        return self.__fullname

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
    
    def set_name(self):
        if isinstance(new_fullname, str):
            self.__fullname = new_fullname
        else:
            print("Incorrect. Please enter the fullname by string")

    def set_address(self):
        if isinstance(new_address, str):
            self.__address = new_address
        else:
            print("Incorrect. Please enter the address by string")

    def set_phone(self):
        if isinstance(new_phone, sint):
            self.__phone = new_phone
        else:
            print("Incorrect. Please enter the address by int")

    def get_data(self):
        print(f'Person {self.__fullname} which lives in {self.__address}, have a phone {self.__phone}')

class Customer(Person):
    def __init__(self, client_number:str = None, sms_code:bool = False, fullname:str = None, address:str = None, phone:int = None) -> None:
        super().__init__(fullname, address, phone)
        self.__client_number = client_number
        self.__sms_code = sms_code

    def get_client_number(self):
        return self.__client_number

    def get_sms_code(self):
        return self.__sms_code

    def set_client_number(self):
        if isinstance(new_number, sint):
            self.__client_number = new_number
        else:
            print("Incorrect. Please enter the address by int")
    
    def set_sms_code(self):
        if isinstance(new_sms, bool):
            self.__sms_code = True
        else:
            self.__sms_code = False

    def get_customer_data(self):
        print(f'{self.__client_number} {self.__sms_code}')

client_a = Customer(87714133433, False, 'Dinmukhammeduly Dias', 'Almaty, Altyn Orda', 87001181843)
client_a.get_customer_data()
client_a.get_data()