

class Medicine:
    __code = ""
    __name = ""
    __presentation = None

    def __init__(self,code,name,presentation):
        self.__code = code
        self.__name = name
        self.__presentation = presentation

    def get_code(self):
        return self.__code
    
    def get_name(self):
        return self.__name
    
    def get_presentation(self):
        return self.__presentation