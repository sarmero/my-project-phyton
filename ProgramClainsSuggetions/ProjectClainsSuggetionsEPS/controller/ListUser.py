from data.StorageEps import StorageEps
from structures.List import List


class ListUser():
    __list_user = List()
    __file_user = StorageEps()

    def __init__(self):
        pass

    def add_user(self, user):
        self.__list_user.push_front(user)

    def list_user(self):
        return self.__list_user

    def search_by_id(self, id):
        user = None
        i = self.__list_user.front()
        while i != None:
            if id == i.value.id():
                user = i.value
            i = i.next

        return user
    
    def search_id(self,code):
        exists = False
        i = self.__list_user.front()
        while i is not None:
            if code == i.value.id():
                exists = True
            i = i.next

        return exists
    
    def save_file_claim_suggestions(self):
        self.__file_user.set_file_name('user.eps')
        self.__file_user.save(self.__list_user)
        

    def load_file_claim_suggestions(self):
        self.__file_user.set_file_name('user.eps')
        self.__list_user = self.__file_user.open_file()
        
