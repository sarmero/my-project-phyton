


class User:
    __id = ""
    __name = ""
    __address = ""
    __phone = ""
    __mail = ""

    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__address = ""
        self.__phone = ""
        self.__mail = ""

    def get_id(self):
        return self.__id
    
    def set_id(self,id):
        self.__id = id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_address(self):
        return self.__address
    
    def set_address(self, address):
        self.__address = address

    def get_phone(self):
        return self.__phone
    
    def set_phone(self, phone):
        self.__phone = phone

    def get_mail(self):
        return self.__mail
    
    def set_mail(self, mail):
        self.__mail = mail