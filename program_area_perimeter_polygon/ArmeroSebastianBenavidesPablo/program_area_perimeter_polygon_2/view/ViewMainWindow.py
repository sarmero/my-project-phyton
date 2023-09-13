from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QColor, QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QColorDialog, QFileDialog, QMainWindow,  QMenu, QMessageBox, QTableWidgetItem
from PyQt5.QtWidgets import QAction, QStyle, QToolBar
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QTableWidget, QComboBox, QFileDialog

from controller.ListPolygon import ListPolygon
from view.ViewDeletePolygon import ViewDeletePolygon
from view.ViewListPolygon import ViewListPolygon
from view.ViewRegisterPolygon import ViewRegisterPolygon
from view.ViewCredits import ViewCredits
from view.ViewUpdatePolygon import ViewUpdatePolygon


class MainWindow(QMainWindow):

    # __search_button = Button()

    def __init__(self):
        super().__init__()
        self.__vector_polygon = ListPolygon()
        self.__window_register_polygon = ViewRegisterPolygon(
            self.__vector_polygon)
        self.__window_list_polygon = ViewListPolygon(self.__vector_polygon)
        self.__Credits = ViewCredits()
        self.__window_update_polygon = ViewUpdatePolygon(self.__vector_polygon)
        self.__window_DeletePolygon = ViewDeletePolygon(self.__vector_polygon)
        self.__route_file = ""
        self.__scale = 1
       

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
        self.ite_update_polygon = QAction("&Modificar polígono", self)
        self.ite_delete_polygon = QAction("&Eliminar polígono", self)
        self.ite_save_polygon = QAction("&Guardar", self)
        self.ite_save_as_polygon = QAction("&Guardar como", self)
        self.ite_open_polygon = QAction("&Abrir archivo", self)
        self.ite_exit = QAction("&Salir", self)
        self.ite_show_credits = QAction("&Créditos", self)

        # Agregar Ícono al Item del menú
        self.ite_register_polygon.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon))
        self.ite_list_polygons.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogDetailedView))
        self.ite_update_polygon.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon))
        self.ite_open_polygon.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon))
        self.ite_delete_polygon.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon))
        self.ite_save_polygon.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon))
        self.ite_save_as_polygon.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon))
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
        menu_file.addAction(self.ite_update_polygon)
        menu_file.addAction(self.ite_delete_polygon)
        menu_file.addSeparator()
        menu_file.addAction(self.ite_open_polygon)
        menu_file.addAction(self.ite_save_polygon)
        menu_file.addAction(self.ite_save_as_polygon)
        menu_file.addSeparator()
        menu_file.addAction(self.ite_exit)
        menu_help.addAction(self.ite_show_credits)

        toolbar = QToolBar(self)
        toolbar.setIconSize(QSize(20,20))
        toolbar.addAction(self.ite_register_polygon)
        toolbar.addAction(self.ite_list_polygons)
        toolbar.addAction(self.ite_update_polygon)
        toolbar.addAction(self.ite_delete_polygon)
        toolbar.addSeparator()
        toolbar.addAction(self.ite_open_polygon)
        toolbar.addAction(self.ite_save_polygon)
        toolbar.addAction(self.ite_save_as_polygon)
        toolbar.addSeparator()
        toolbar.addAction(self.ite_exit)
        self.addToolBar(toolbar)

        canvas = QPixmap(690, 690)
        canvas.fill(Qt.white)
        self.lab_canvas = QLabel(self)
        self.lab_canvas.setGeometry(QRect(20, 55, 690, 690))
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

        self.lab_point = QLabel(self)
        self.lab_point.setText("Color punto")
        self.lab_point.setGeometry(QRect(740, 560, 100, 25))

        self.but_color_point = QPushButton(self)
        self.but_color_point.setText("")
        self.but_color_point.setGeometry(QRect(800, 560, 40, 30))

        self.lab_line = QLabel(self)
        self.lab_line.setText("Color linea")
        self.lab_line.setGeometry(QRect(740, 600, 100, 25))

        self.but_color_line = QPushButton(self)
        self.but_color_line.setText("")
        self.but_color_line.setGeometry(QRect(800, 600, 40, 30))

        self.lab_zoom = QLabel(self)
        self.lab_zoom.setText("Zoom")
        self.lab_zoom.setGeometry(QRect(740, 640, 100, 25))

        self.but_scale_increase = QPushButton(self)
        self.but_scale_increase.setText("+")
        self.but_scale_increase.setGeometry(QRect(800, 640, 40, 25))

        self.but_scale_decrease = QPushButton(self)
        self.but_scale_decrease.setText("-")
        self.but_scale_decrease.setGeometry(QRect(850, 640, 40, 25))

        


    def __launch_Events(self):
        # Conectar el método a el evento clic de un item del menú
        self.ite_register_polygon.triggered.connect(self.__register_polygons)
        self.ite_list_polygons.triggered.connect(self.__list_polygons)
        self.ite_update_polygon.triggered.connect(self.__update_polygon)
        self.ite_delete_polygon.triggered.connect(self.__delete_polygon)
        self.ite_save_polygon.triggered.connect(self.__save_file)
        self.ite_save_as_polygon.triggered.connect(self.__save_as_file)
        self.ite_open_polygon.triggered.connect(self.__open_file)
        self.ite_show_credits.triggered.connect(self.__show_credits)
        self.but_update.clicked.connect(self.__update)
        self.com_code.currentTextChanged.connect(self.__search_polygon)
        self.but_scale_increase.clicked.connect(self.__zoom_polygon_increase)
        self.but_scale_decrease.clicked.connect(self.__zoom_polygon_decrease)
        self.but_color_line.clicked.connect(self.selected_color_line)
        self.but_color_point.clicked.connect(self.selected_color_point)

    def __zoom_polygon_increase(self):
        self.__scale += 0.5
        self.__search_polygon()

    def __zoom_polygon_decrease(self):
        self.__scale -= 0.5
        self.__search_polygon()

    def __open_file(self):
        file_name = QFileDialog.getOpenFileName(self,str("Abrir polígono"),"savePolygon/untitled.plg",str("polygon(*.plg)"))
        if file_name != ('', ''):
            print(file_name[0])
            self.__route_file = file_name[0]
            self.open_file()

    def __save_file(self):
        if self.__vector_polygon.get_size() > 0:
            if  self.__route_file != "":
                self.save_file()
            else:
                self.__save_as_file()
        else:
            QMessageBox.information(
                self, "Gestor polígonos", "No se encuentra ningún polígono listado", QMessageBox.Ok)
      

    def __save_as_file(self):
        file_name = QFileDialog.getSaveFileName(self, str("Guardar Polígono"),"/savePolygon/untitled.plg",str("polygon(*.plg)"))
        if file_name != ('', ''):
            print(file_name[0])
            self.__route_file = file_name[0]
            self.save_file()

    def selected_color_line(self):
        self.color_line = QColorDialog.getColor()
        self.but_color_line.setStyleSheet("background-color: rgb("+str(self.color_line.red(
        ))+","+str(self.color_line.green())+","+str(self.color_line.blue())+");")
        self.__search_polygon()

    def selected_color_point(self):
        self.color_point = QColorDialog.getColor()
        self.but_color_point.setStyleSheet("background-color: rgb("+str(self.color_point.red(
        ))+","+str(self.color_point.green())+","+str(self.color_point.blue())+");")
        self.__search_polygon()

    def __delete_polygon(self):
        self.__window_DeletePolygon.initWindow()
        self.__window_DeletePolygon.setVisible(True)

    def __update_polygon(self):
        self.__window_update_polygon.initWindow()
        self.__window_update_polygon.setVisible(True)

    def __register_polygons(self):
        # Hace visible la ventana
        self.__window_register_polygon.initWindow()
        self.__window_register_polygon.setVisible(True)

    def __list_polygons(self):
        # Hace visible la ventana
        self.__window_list_polygon.setVisible(True)

    def __show_credits(self):
        # Hace visible la ventana
        self.__Credits.setVisible(True)

    def __search_polygon(self):
        self.tab_point.setRowCount(0)
        item = self.com_code.currentText()
        polygon = self.__vector_polygon.show_polygon(item)

        if polygon != None:
            self.tex_perimeter.setText(str(polygon.calculate_perimeter()))
            self.tex_area.setText(str(polygon.calculate_area()))
            self.__init_canvas()

            for i in range(polygon.points_count()):
                x = polygon.point_x[i]
                y = polygon.point_y[i]

                ite_x = QTableWidgetItem(str(x))
                ite_y = QTableWidgetItem(str(y))

                self.tab_point.insertRow(self.tab_point.rowCount())
                self.tab_point.setItem(self.tab_point.rowCount()-1, 0, ite_x)
                self.tab_point.setItem(self.tab_point.rowCount()-1, 1, ite_y)

            self.__draw_polygon(polygon.points_count(),
                                polygon.point_x, polygon.point_y)

    def __update(self):
        self.com_code.clear()

        for i in range(self.__vector_polygon.get_size()):
            self.com_code.addItem(
                str(self.__vector_polygon.array_polygon[i].code))

    def __draw_polygon(self, quantity_point, point_x, point_y):
        canvas = self.lab_canvas.pixmap()
        width = canvas.width()
        height = canvas.height()
    

        painter = QPainter(canvas)
        painter.translate(width/2, height/2)
        painter.scale(self.__scale, -1*self.__scale)

        red = int(self.color_line.red())
        green = int(self.color_line.green())
        blue = int(self.color_line.blue())

        red1 = self.color_point.red()
        green1 = self.color_point.green()
        blue1 = self.color_point.blue()

        

        pen_point = QPen(QColor(red1, green1, blue1), 5, Qt.SolidLine)
        pen_line = QPen(QColor(red, green, blue), 1, Qt.SolidLine)

        for i in range(quantity_point):
            painter.setPen(pen_point)
            painter.drawPoint(int(point_x[i]), int(point_y[i]))

            painter.setPen(pen_line)
            painter.drawLine(int(point_x[i]), int(
                point_y[i]), int(point_x[i+1]), int(point_y[i+1]))

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
        self.__vector_polygon.load_polygon(self.__route_file)

    def save_file(self):
        self.__vector_polygon.save_polygon(self.__route_file)

    def closeEvent(self, event):
        res = QMessageBox.question(
            self, "Gestor polígonos", "¿Esta seguro que desea salir?", QMessageBox.Yes, QMessageBox.No)
        if res == 16384:
            #self.__save_file()
            event.accept()
        else:
            event.ignore()

    def init_window(self):
        self.tab_point.setRowCount(0)
        self.tex_area
        self.tex_perimeter
        self.color_line = QColor()
        self.color_point = QColor()
        self.__init_canvas()
        self.__update()
