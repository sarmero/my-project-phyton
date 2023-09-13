from data.StorageEps import StorageEps
from structures.List import List


class ListClaimSuggestions:
    __list_ClaimSuggestions = List()
    __file_ClaimSuggestions = StorageEps()

    def __init__(self):
        pass    

    def add_claim_suggestions(self, petition):
        self.__list_ClaimSuggestions.push_front(petition)

    def list_claim_suggestions(self):
        return self.__list_ClaimSuggestions

    def search_by_state(self, state):
        list_state = List()
        i = self.__list_ClaimSuggestions.front()
        while i is not None:
            print(state," : ",i.value.state())
            if state == i.value.state() or state == "Todo":
                list_state.push_front(i.value)
            i = i.next

        return list_state

    def search_by_code(self, code):
        suggestion = None
        i = self.__list_ClaimSuggestions.front()
        while i is not None:
            if code == i.value.code():
                suggestion = i.value
            i = i.next

        return suggestion

    def search_by_id(self, id):
        suggestion = None
        i = self.__list_ClaimSuggestions.front()
        while i is not None:
            if id == i.value.id_user():
                suggestion = i.value
            i = i.next

        return suggestion
    
    def register_response(self, code, response, date_response, state):
        i = self.__list_ClaimSuggestions.front()
        while i is not None:
            if code == i.value.code():
                i.value.set_response(response)
                i.value.set_date_response(date_response)
                i.value.set_state(state)
            i = i.next

    def search_code(self,code):
        exists = False
        i = self.__list_ClaimSuggestions.front()
        while i is not None:
            if code == i.value.code():
                exists = True
            i = i.next

        return exists

    def save_file_claim_suggestions(self):
        self.__file_ClaimSuggestions.set_file_name('ClaimSuggestions.eps')
        self.__file_ClaimSuggestions.save(self.__list_ClaimSuggestions)

    def load_file_claim_suggestions(self):
        self.__file_ClaimSuggestions.set_file_name('ClaimSuggestions.eps')
        self.__list_ClaimSuggestions = self.__file_ClaimSuggestions.open_file()