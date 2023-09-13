class ClaimSuggestions:
    __code = ""
    __type = ""
    __id_user = ""
    __date = ""
    __date_response = ""
    __hour = ""
    __description = ""
    __response = ""
    __state = False
    
    def __init__(self, code, date, hour, id_user, state, type, description):
        self.__type = type
        self.__code = code
        self.__id_user = id_user
        self.__date = date
        self.__hour = hour
        self.__description = description
        self.__state = state
        
    def type(self):
        return self.__type  
    
    def code(self):
        return self.__code
    
    def id_user(self):
        return self.__id_user

    def date(self):
        return self.__date

    def hour(self):
        return self.__hour
    
    def description(self):
        return self.__description

    def state(self):
        return self.__state
    
    def set_state(self, state):
        self.__state = state
    
    def set_response(self, response):
        self.__response = response

    def response(self):
        return self.__response
    
    def set_date_response(self, date_response):
        self.__date_response = date_response

    def date_response(self):
        return self.__date_response
    
    
    
