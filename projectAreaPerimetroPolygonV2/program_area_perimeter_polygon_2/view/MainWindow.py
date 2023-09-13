from PySide6.QtWidgets import QMainWindow


from controller.ListPolygon import ListPolygon
from view.RegisterPolygon import RegisterPolygon
from view.Credits import Credits


class MainWindow(QMainWindow):
    __vector_polygon = ListPolygon()
    __window_register_polygon = RegisterPolygon()
    __window_list_polygon = ListPolygon()
    __Credits = Credits()
    # __search_button = Button()

    def __init__(self):
        super().__init__()
        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Gestor de polígono")
        self.setFixedSize(1024, 768)
        pass

    def __launch_Events(self):
        pass

    def __register_polygon(self):
        pass

    def __list_polygon(self):
        pass

    def __show_credits(self):
        pass

    def __search_polygon(self):
        pass
