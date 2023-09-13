from PyQt5.QtWidgets import QDialog
from controller.ListPharmacy import ListPetition


class RegisterMedicineView(QDialog):
    __vector_pharmacy = ListPetition()

    def __init__(self, vector_pharmacy):
        super().__init__()
        self.__vector_pharmacy = vector_pharmacy

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        pass

    def __launch_Events(self):
        pass

    def save(self):
        pass
    
    def cancel(self):
        pass

    def init_window(self):
        pass