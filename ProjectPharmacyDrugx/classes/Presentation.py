


class Presentation:
    __name_presentation =""
    __content = 0
    __extent = ""

    def __init__(self,name_presentation,content,extent):
        self.__name_presentation = name_presentation
        self.__content = content
        self.__extent = extent

    def get_name_presentation(self):
        return self.__name_presentation
    
    def get_content(self):
        return self.__content
    
    def get_extent(self):
        return self.__extent