import random
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QMainWindow,  QMenu, QTableWidgetItem
from PyQt5.QtWidgets import QAction, QStyle
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QTableWidget, QComboBox
from classes.Polygon import Polygon

from controller.ListPolygon import ListPolygon
from view.ViewListPolygon import ViewListPolygon
from view.ViewRegisterPolygon import ViewRegisterPolygon
from view.ViewCredits import ViewCredits


class MainWindow(QMainWindow):

    # __search_button = Button()

    def __init__(self):
        super().__init__()
        self.__vector_polygon = ListPolygon()
        self.__window_register_polygon = ViewRegisterPolygon(
            self.__vector_polygon)
        self.__window_list_polygon = ViewListPolygon(self.__vector_polygon)
        self.__Credits = ViewCredits()

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Gestor de polígono")
        self.setFixedSize(1024, 768)
        # obtener barra de menú
        bar_menu = self.menuBar()
        # Adiciona opción al menú "&" sirve para dar acceso rápido
        menu_file = bar_menu.addMenu("&Polígono")
        menu_help = bar_menu.addMenu("&Ayuda")

        # Crear Item de un menú
        self.ite_register_polygon = QAction("&Registrar polígono", self)
        self.ite_list_polygons = QAction("&Lista de polígonos", self)
        self.ite_exit = QAction("&Salir", self)
        self.ite_show_credits = QAction("&Créditos", self)

        # Agregar Ícono al Item del menú
        self.ite_register_polygon.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon))
        self.ite_list_polygons.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogDetailedView))
        self.ite_exit.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogBack))
        self.ite_show_credits.setIcon(self.style().standardIcon(
            QStyle.SP_MessageBoxInformation))

        # agregar un short cut (acceso rápido)
        self.ite_register_polygon.setShortcut("CTRL+R")
        self.ite_list_polygons.setShortcut("CTRL+L")
        self.ite_exit.setShortcut("CTRL+E")
        self.ite_show_credits.setShortcut("CTRL+S")

        # agregar item al menú
        menu_file.addAction(self.ite_register_polygon)
        menu_file.addAction(self.ite_list_polygons)
        menu_file.addSeparator()
        menu_file.addAction(self.ite_exit)
        menu_help.addAction(self.ite_show_credits)

        canvas = QPixmap(700, 700)
        canvas.fill(Qt.white)
        self.lab_canvas = QLabel(self)
        self.lab_canvas.setGeometry(QRect(20, 45, 700, 700))
        self.lab_canvas.setPixmap(canvas)

        self.lab_code = QLabel(self)
        self.lab_code.setText("Código del polígono")
        self.lab_code.setGeometry(QRect(740, 45, 150, 25))

        self.lab_points = QLabel(self)
        self.lab_points.setText("Puntos del polígono")
        self.lab_points.setGeometry(QRect(740, 115, 150, 25))

        self.lab_perimeter = QLabel(self)
        self.lab_perimeter.setText("perímetro")
        self.lab_perimeter.setGeometry(QRect(740, 420, 100, 25))

        self.lab_area = QLabel(self)
        self.lab_area.setText("Area")
        self.lab_area.setGeometry(QRect(740, 490, 100, 25))

        self.com_code = QComboBox(self)
        self.com_code.setGeometry(QRect(740, 80, 70, 25))

        self.tab_point = QTableWidget(self)
        self.tab_point.setGeometry(QRect(740, 150, 170, 260))
        self.tab_point.setColumnCount(2)
        self.tab_point.setRowCount(0)
        self.tab_point.setColumnWidth(0, 75)
        self.tab_point.setColumnWidth(1, 75)

        ite_x = QTableWidgetItem("x")
        self.tab_point.setHorizontalHeaderItem(0, ite_x)
        ite_y = QTableWidgetItem("y")
        self.tab_point.setHorizontalHeaderItem(1, ite_y)

        self.tex_perimeter = QLineEdit(self)
        self.tex_perimeter.setGeometry(QRect(740, 455, 150, 25))

        self.tex_area = QLineEdit(self)
        self.tex_area.setGeometry(QRect(740, 525, 150, 25))

        self.but_update = QPushButton(self)
        self.but_update.setText("Actualizar")
        self.but_update.setGeometry(QRect(820, 80, 70, 30))

    def __launch_Events(self):
        # Conectar el método a el evento clic de un item del menú
        self.ite_register_polygon.triggered.connect(self.__register_polygons)
        self.ite_list_polygons.triggered.connect(self.__list_polygons)
        self.ite_show_credits.triggered.connect(self.__show_credits)
        self.but_update.clicked.connect(self.__update_list_code)
        self.com_code.currentTextChanged.connect(self.__search_polygon)

    def __register_polygons(self):
        # Hace visible la ventana
        self.__window_register_polygon.initWindow()
        self.__window_register_polygon.setVisible(True)

    def __list_polygons(self):
        # Hace visible la ventana
        self.__window_list_polygon.list_polygon()
        self.__window_list_polygon.setVisible(True)

    def __show_credits(self):
        # Hace visible la ventana
        self.__Credits.setVisible(True)

    def __search_polygon(self):
        self.tab_point.setRowCount(0)
        item = self.com_code.currentText()
        polygon = self.__vector_polygon.search_by_code(item)

        if polygon != None:
            self.tex_perimeter.setText(str(polygon.calculate_perimeter()))
            self.tex_area.setText(str(polygon.calculate_area()))
            self.__init_canvas()

            i = polygon.points.front()
            while i != polygon.points.back():

                ite_x = QTableWidgetItem(str(i.value.x))
                ite_y = QTableWidgetItem(str(i.value.y))

                self.tab_point.insertRow(self.tab_point.rowCount())
                self.tab_point.setItem(self.tab_point.rowCount()-1, 0, ite_x)
                self.tab_point.setItem(self.tab_point.rowCount()-1, 1, ite_y)

                i = i.next

            self.__draw_polygon(polygon.points)

    def __update_list_code(self):
        self.com_code.clear()
        self.__vector_polygon.list_code_polygon(self.com_code)

    def __draw_polygon(self, points):
        canvas = self.lab_canvas.pixmap()
        width = canvas.width()
        height = canvas.height()

        painter = QPainter(canvas)
        painter.translate(width/2, height/2)
        painter.scale(1, -1)

        random.randrange(255)

        pen_point = QPen(QColor(255, 0, 0), 5, Qt.SolidLine)
        pen_line = QPen(QColor(random.randrange(255), random.randrange(
            255), random.randrange(255)), 1, Qt.SolidLine)

        i = points.front()
        while i != points.back():
            point_a = i.value
            point_b = i.next.value

            painter.setPen(pen_point)
            painter.drawPoint(int(point_a.x), int(point_a.y))

            painter.setPen(pen_line)
            painter.drawLine(int(point_a.x), int(point_a.y),
                             int(point_b.x), int(point_b.y))

            i = i.next

        painter.end()
        self.lab_canvas.setPixmap(canvas)

    def __init_canvas(self):
        canvas = self.lab_canvas.pixmap()
        canvas.fill(Qt.white)
        width = canvas.width()
        height = canvas.height()

        painter = QPainter(canvas)
        painter.translate(width/2, height/2)
        painter.scale(1, -1)

        pen_eje = QPen(QColor(255, 128, 128), 1, Qt.SolidLine)
        painter.setPen(pen_eje)

        painter.drawLine(int(-width/2), 0, int(width/2), 0)
        painter.drawLine(0, int(height/2), 0, int(-height/2))

        painter.end()
        self.lab_canvas.setPixmap(canvas)

    def open_file(self):
        self.__vector_polygon.load_polygon()

    def save_file(self):
        self.__vector_polygon.save_polygon()

    def closeEvent(self, event):
        self.save_file()
        event.accept()

    def init_window(self):
        self.tab_point.setRowCount(0)
        self.tex_area
        self.tex_perimeter
        self.__init_canvas()
        # self.__update_list_code()
