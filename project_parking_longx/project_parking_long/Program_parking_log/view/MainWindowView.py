from array import array
import code
from tkinter import Canvas
from turtle import width
from PyQt5.QtCore import QRect, Qt, QSize
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtWidgets import QAction, QComboBox, QFileDialog, QLabel, QLineEdit, QMainWindow, QPushButton, QStyle, QTableWidget, QTableWidgetItem, QMessageBox, QToolBar, QColorDialog
from view.CreditView import CreditView
from view.ListPolygonsView import ListPolygonsView
from view.RegisterPolygonView import RegisterPolygonView
from controller.ListPolygon import ListPolygon
from view.UpdatePolygon import UpdatePolygon
from view.DeletePolygonsView import DeletePolygonsView


class MainWindowView(QMainWindow):

    def __init__(self):
        super().__init__()  # Constructor de la clase padre
        # Se separa memoria para el arreglo de polígonos
        # self.__vector_polygons = ListPolygon()
        # self.window_register_polygons = RegisterPolygonView(
        #    self.__vector_polygons)
        # self.window_list_polygons = ListPolygonsView(self.__vector_polygons)
        # self.window_credits = CreditView()
        # self.window_update_polygon = UpdatePolygon(self.__vector_polygons)
        # self.window_delete_polygon = DeletePolygonsView(self.__vector_polygons)

        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Parqueadero")
        self.setFixedSize(1024, 680)

        # obtener barra de menú
        bar_menu = self.menuBar()

        # Adiciona opción al menú "&" sirve para dar acceso rápido
        menu_file = bar_menu.addMenu("&Archivo")
        menu_parking = bar_menu.addMenu("parqueadero")
        menu_help = bar_menu.addMenu("&Ayuda")

        # Crear Item de un menú
        self.ite_register_polygon = QAction("&Registrar polígono", self)
        self.ite_list_polygons = QAction("&Lista de polígonos", self)
        self.ite_update = QAction("&Modificar", self)
        self.ite_delete = QAction("&Eliminar", self)
        self.ite_exit = QAction("&Salir", self)
        self.ite_show_credits = QAction("&Créditos", self)
        self.ite_open = QAction("&Abrir", self)
        self.ite_save = QAction("&Guardar", self)
        self.ite_save_as = QAction("&Guardar como", self)
        self.color_puntos = QColor(255, 0, 0)
        self.color_line = QColor(0, 0, 255)
        self.zoom = (1.0)
