from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QColor, QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QAction, QColorDialog, QComboBox, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QStyle, QTableWidget, QTableWidgetItem, QToolBar
from controller.ListEquipment import ListEquipment
from controller.ListMaintenance import ListMaintenance
from view.CreditView import CreditView
from view.ListEquipmentView import ListEquipmentView
from view.RegisterEquipmentView import RegisterEquipmentView
from view.RegisterMaintenanceView import RegisterMaintenanceView
from view.RegisterReparationsView import RegisterReparationsView


class MainWindowView(QMainWindow):
    def __init__(self):
        super().__init__()  # Constructor de la clase padre
        # se separa para arreglo de polígonos(una sola vez)
        self.__vector_equipment = ListEquipment()
        self.__vector_maintenance = ListMaintenance()

        self.window_register_equipment = RegisterEquipmentView(
            self.__vector_equipment)

        self.window_list_equipment = ListEquipmentView(self.__vector_equipment)

        self.window_register_maintenance = RegisterMaintenanceView(
            self.__vector_equipment, self.__vector_maintenance)

        self.window_reparations = RegisterReparationsView(
            self.__vector_equipment, self.__vector_maintenance)

        self.window_credits = CreditView()

        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Gestor de mantenimiento de computadores")
        self.setFixedSize(887, 470)

        # obtener barra de menú
        bar_menu = self.menuBar()

        # Adiciona opción al menú "&" sirve para dar acceso rápido
        menu_file = bar_menu.addMenu("Archivo")
        menu_equipment = bar_menu.addMenu("Equipos")
        menu_maintenance = bar_menu.addMenu("Mantenimiento")
        menu_help = bar_menu.addMenu("Ayuda")

        # Crear Item de un menú
        self.ite_register_equipment = QAction("Registrar equipos", self)
        self.ite_list_equipment = QAction("Lista de equipos", self)
        self.ite_register_maintenance = QAction(
            "Registrar &mantenimiento", self)
        self.ite_reparations = QAction("Reparaciones", self)
        self.ite_open = QAction("Abrir", self)
        self.ite_save = QAction("Guardar", self)
        self.ite_save_as = QAction("Guardar como", self)

        self.ite_exit = QAction("Salir", self)
        self.ite_show_credits = QAction("Créditos", self)

        # Agregar Ícono al Item del menú
        self.ite_open.setIcon(self.style().standardIcon(QStyle.SP_DirOpenIcon))
        self.ite_save.setIcon(self.style().standardIcon(
            QStyle.SP_DialogSaveButton))
        self.ite_save_as.setIcon(self.style().standardIcon(
            QStyle.SP_DirHomeIcon))
        self.ite_register_equipment.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon))
        self.ite_list_equipment.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogDetailedView))
        self.ite_register_maintenance.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon))
        self.ite_exit.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogBack))
        self.ite_show_credits.setIcon(self.style().standardIcon(
            QStyle.SP_MessageBoxInformation))

        # agregar un short cut (acceso rápido)
        self.ite_register_equipment.setShortcut("CTRL+R")
        self.ite_list_equipment.setShortcut("CTRL+L")
        self.ite_exit.setShortcut("CTRL+E")
        self.ite_show_credits.setShortcut("CTRL+S")
        self.ite_register_maintenance.setShortcut("CTRL+M")
        self.ite_save.setShortcut("CTRL+S")
        self.ite_save_as.setShortcut("CTRL+M")

        # agregar item al menú
        menu_equipment.addAction(self.ite_register_equipment)
        menu_equipment.addAction(self.ite_list_equipment)
        menu_maintenance.addAction(self.ite_register_maintenance)
        menu_maintenance.addAction(self.ite_reparations)
        menu_file.addAction(self.ite_open)
        menu_file.addAction(self.ite_save)
        menu_file.addAction(self.ite_save_as)
        menu_file.addAction(self.ite_exit)
        menu_help.addAction(self.ite_show_credits)

        # tool_bar
        tool_bar = QToolBar()
        tool_bar.setIconSize(QSize(130, 15))

        self.addToolBar(tool_bar)
        tool_bar.addAction(self.ite_list_equipment)

        tool_bar.addAction(self.ite_register_equipment)

        tool_bar.addAction(self.ite_show_credits)
        tool_bar.addSeparator()

        tool_bar.addAction(self.ite_save)

        tool_bar.addAction(self.ite_exit)

        tool_bar.addAction(self.ite_register_maintenance)

        # -----------------------------------------------------------
        # Crea una tabla y la asocia a la ventana
        self.tab_info_maintenance = QTableWidget(self)
        # Ubicar tabla en la ventana (x,y,ancho,largo)
        self.tab_info_maintenance.setGeometry(QRect(40, 140, 800, 290))
        # Agregar filas y columnas a la tabla
        self.tab_info_maintenance.setColumnCount(6)
        self.tab_info_maintenance.setRowCount(0)
        # Agregar ancho a las columnas (indice, ancho)
        self.tab_info_maintenance.setColumnWidth(0, 100)  # columna 1 (marca)
        self.tab_info_maintenance.setColumnWidth(1, 100)  # columna 2 (modelo)
        self.tab_info_maintenance.setColumnWidth(2, 100)  # columna 3 (código)
        self.tab_info_maintenance.setColumnWidth(
            3, 120)  # columna 4 (fecha ingreso)
        self.tab_info_maintenance.setColumnWidth(
            4, 260)  # columna 5 (descripción)
        self.tab_info_maintenance.setColumnWidth(5, 90)  # columna 6 (teléfono)

        ite_mark = QTableWidgetItem("Marca")
        self.tab_info_maintenance.setHorizontalHeaderItem(0, ite_mark)
        ite_model = QTableWidgetItem("Modelo")
        self.tab_info_maintenance.setHorizontalHeaderItem(1, ite_model)
        ite_code = QTableWidgetItem("Código")
        self.tab_info_maintenance.setHorizontalHeaderItem(2, ite_code)
        ite_date_input = QTableWidgetItem("Fecha de ingreso")
        self.tab_info_maintenance.setHorizontalHeaderItem(3, ite_date_input)
        ite_description = QTableWidgetItem("Descripción")
        self.tab_info_maintenance.setHorizontalHeaderItem(4, ite_description)
        ite_reparation = QTableWidgetItem("Reparación")
        self.tab_info_maintenance.setHorizontalHeaderItem(5, ite_reparation)

        self.but_update = QPushButton(self)
        self.but_update.setText("Actualizar")
        # Ubicar en la ventana(x,y,ancho,largo)
        self.but_update.setGeometry(QRect(40, 80, 100, 30))

        
        

        
    

    def __launch_events(self):
        # Conectar el método a el evento clic de un item del menú
        self.ite_register_equipment.triggered.connect(
            self.__register_equipment)
        self.ite_list_equipment.triggered.connect(self.__list_equipment)
        self.ite_register_maintenance.triggered.connect(
            self.__register_maintenance)
        self.ite_reparations.triggered.connect(self.__reparations)
        self.ite_show_credits.triggered.connect(self.__show_credits)
        self.but_update.clicked.connect(self.__load_maintenance)

    def init_window(self):
        self.tab_info_maintenance.setRowCount(0)

    def __load_maintenance(self):
        self.tab_info_maintenance.setRowCount(0)
        self.maintenance = self.__vector_maintenance.get_maintenance()
        i = self.maintenance.front()
        while i != None:
            equipment = self.__vector_equipment.search_by_code(
                i.value.code_equipment)
            ite_mark = QTableWidgetItem(str(equipment.mark))
            ite_mark.setForeground(QColor("blue"))
            ite_model = QTableWidgetItem(str(equipment.model))
            ite_code = QTableWidgetItem(str(i.value.code))
            ite_date_input = QTableWidgetItem(str(i.value.date_input))
            ite_description = QTableWidgetItem(str(i.value.description_fail))
            ite_link = QTableWidgetItem("Reparación")
            # Insertar fila al final de la tabla
            # rowcount() devuelve la cantidad de filas de la tabla
            self.tab_info_maintenance.insertRow(
                self.tab_info_maintenance.rowCount())
            self.tab_info_maintenance.setItem(
                self.tab_info_maintenance.rowCount()-1, 0, ite_mark)
            self.tab_info_maintenance.setItem(
                self.tab_info_maintenance.rowCount()-1, 1, ite_model)
            self.tab_info_maintenance.setItem(
                self.tab_info_maintenance.rowCount()-1, 2, ite_code)
            self.tab_info_maintenance.setItem(
                self.tab_info_maintenance.rowCount()-1, 3, ite_date_input)
            self.tab_info_maintenance.setItem(
                self.tab_info_maintenance.rowCount()-1, 4, ite_description)
            self.tab_info_maintenance.setItem(
                self.tab_info_maintenance.rowCount()-1, 5, ite_link)

            i = i.next

    def __reparations(self):
        self.window_reparations
        self.window_reparations.setVisible(True)

    def __register_equipment(self):
        # Hace visible la ventana
        self.window_register_equipment.init_window()
        self.window_register_equipment.setVisible(True)

    def __list_equipment(self):
        # Hace visible la ventana
        self.window_list_equipment.init_window()
        self.window_list_equipment.setVisible(True)

    def __register_maintenance(self):
        # Hace visible la ventana
        self.window_register_maintenance.init_window()
        self.window_register_maintenance.setVisible(True)

    def __show_credits(self):
        # Hace visible la ventana
        self.window_credits.setVisible(True)
