from controller.ListEPS import ListEPS
from structures.List import List

class ListUser(ListEPS):

    def __init__(self):
        self.file_name = 'user.usr'

    def update_user(self, user):
        i: List = self.get_list().front()
        while i != None:
            if user.get_id() == i.value.get_id():
                i.value = user
            i = i.next

    def search_by_id(self, id):
        i: List = self.get_list().front()
        while i != None:
            if id == i.value.get_id():
                return i.value
            i = i.next
        return None
    
    def validate_id(self, id):
        i = self.get_list().front()
        while i != None:
            if id == i.value.get_id():
                return True
            i = i.next

        return False
