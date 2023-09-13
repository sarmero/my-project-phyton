import random
from controller.ListEPS import ListEPS
from structures.List import List


class ListSuggestion(ListEPS):

    def __init__(self):
        self.file_name = "Suggestions.sgt"

    def search_by_guy(self, guy):
        list = List()
        i = self.get_list().front()
        while i != None:
            if guy == i.value.get_guy():
                list.push_front(i.value)
            i = i.next

        return list

    def search_by_code(self, code):
        i = self.get_list().front()
        while i != None:
            if code == i.value.get_code():
                return i.value
            i = i.next

        return None

    def search_by_id(self, id):
        list = List()
        i = self.get_list().front()
        while i != None:
            if id == i.value.get_id_user():
                list.push_front(i.value)
            i = i.next

        return list
    
    def search_list_code_by_id(self, id):
        list = List()
        i = self.get_list().front()
        while i != None:
            if id == i.value.get_id_user():
                list.push_front(i.value.get_code())
            i = i.next

        return list
    
    def search_list_code(self):
        list = List()
        i = self.get_list().front()
        while i != None:
            if i.value.get_state() == False:
                list.push_front(i.value.get_code())
            i = i.next

        return list

    def validate_code(self,code):
        i = self.get_list().front()
        while i != None:
            if code == i.value.get_code():
                return True
            i = i.next

        return False
    
    def answer(self, suggestion):
        i = self.get_list().front()
        while i != None:
            if suggestion.get_code() == i.value.get_code():
                i.value = suggestion
                break
            i = i.next

        return None
    
    def generate_code(self):
        code = self.__nRandom("")
        if self.validate_code(code) == True:
            code = self.generate_code()
        
        return code

    def __nRandom(self, code):
        n = random.randrange(47, 91)
        if (n > 47 and n < 58) or (n > 64 and n < 91):
            code += str(chr(n))
            if  len(code) == 4:
                return code
            else:
                return  self.__nRandom(code)
        else:
            return self.__nRandom(code)
           
