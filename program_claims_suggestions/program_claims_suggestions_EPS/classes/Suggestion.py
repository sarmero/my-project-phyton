

class Suggestion:
    __code = ""
    __date = ""
    __hour = ""
    __id_user = ""
    __state = False
    __guy = ""
    __answer = ""
    __description = ""

    def __init__(self):
        self.__code = ""
        self.__date = ""
        self.__hour = ""
        self.__id_user = ""
        self.__state = False
        self.__guy = ""
        self.__answer = ""
        self.__description = ""

    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description

    def get_code(self):
        return self.__code

    def set_code(self,code):
        self.__code = code

    def get_date(self):
        return self.__date

    def set_date(self,date):
        self.__date = date

    def get_hour(self):
        return self.__hour

    def set_hour(self,hour):
        self.__hour = hour

    def get_id_user(self):
        return self.__id_user

    def set_id_user(self, user):
        self.__id_user = user

    def get_state(self):
        return self.__state

    def set_state(self,state):
        self.__state = state

    def get_guy(self):
        return self.__guy

    def set_guy(self, guy):
        self.__guy = guy

    def get_answer(self):
        return self.__answer

    def set_answer(self, answer):
        self.__answer = answer


