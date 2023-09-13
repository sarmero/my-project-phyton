class User:
    __type_id =""
    __id = ""
    __name = ""
    __mail = ""
    __cell = ""
    __address = ""
    __gender = ""
    __date_birth = ""
    
    def __init__(self, type_id, id, name, mail, cell, address, gender,date_birth):
        self.__type_id = type_id
        self.__id = id
        self.__name = name
        self.__mail = mail
        self.__cell = cell
        self.__address = address
        self.__gender = gender
        self.__date_birth = date_birth

    def type_id(self):
        return self.__type_id

    def id(self):
        return self.__id

    def name(self):
        return self.__name
    
    def mail(self):
        return self.__mail
    
    def cell(self):
        return self.__cell

    def address(self):
        return self.__address
    
    def gender(self):
        return self.__gender
    
    def date_birth(self):
        return self.__date_birth
