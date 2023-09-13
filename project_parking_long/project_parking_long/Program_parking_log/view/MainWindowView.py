from array import array
from tkinter import Canvas
from turtle import width
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRect, Qt, QSize
from PyQt5.QtWidgets import QAction, QComboBox, QFileDialog, QLabel, QLineEdit, QMainWindow, QPushButton, QStyle, QTableWidget, QTableWidgetItem, QMessageBox, QToolBar, QColorDialog
from controller.ListControlInputOutput import ListControlInputOutput
from view.RegisterInputVehicleView import RegisterInputVehicleView
from view.RegisterOutputView import RegisterOutputView
from view.ReportParkingView import ReportParkingView


class MainWindowView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.__vector_parking_log = ListControlInputOutput()
        self.__window_register_input = RegisterInputVehicleView(
            self.__vector_parking_log)
        self.__window_register_output = RegisterOutputView(
            self.__vector_parking_log)
        self.__window_report_parking = ReportParkingView(
            self.__vector_parking_log)
        self.file = ""
        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Parqueadero Vehículos")
        self.setFixedSize(900, 600)

        # obtener barra de menú
        bar_menu = self.menuBar()

        # Adiciona opción al menú "&" sirve para dar acceso rápido
        menu_archive = bar_menu.addMenu("&Archivo")
        menu_file = bar_menu.addMenu("&Parqueadero")
        menu_help = bar_menu.addMenu("&Ayuda")

        # Crear Item de un menú
        self.ite_open = QAction("&Abrir", self)
        self.ite_save = QAction("&Guardar", self)
        self.ite_register_input = QAction(
            "&Registrar entrada de vehículos", self)
        self.ite_report_output = QAction("&Registro salida vehículo", self)
        self.ite_report_parking = QAction("&Reporte vehículos")
        self.ite_show_credits = QAction("&Créditos", self)

        self.ite_open.setIcon(self.style().standardIcon(
            QStyle.SP_DialogOpenButton))
        self.ite_save.setIcon(
            self.style().standardIcon(QStyle.SP_DialogSaveButton))
        self.ite_show_credits.setIcon(self.style().standardIcon(
            QStyle.SP_MessageBoxInformation))
        self.ite_register_input.setIcon(self.style().standardIcon(
            QStyle.SP_TitleBarMaxButton))
        self.ite_report_output.setIcon(self.style().standardIcon(
            QStyle.SP_FileDialogDetailedView))
        self.ite_report_parking.setIcon(self.style().standardIcon(
            QStyle.SP_FileDialogBack))

        # agregar un short cut (acceso rápido)
        self.ite_open.setShortcut("CTRL+A")
        self.ite_save.setShortcut("CTRL+G")

        self.ite_register_input.setShortcut("CTRL+R")
        self.ite_report_output.setShortcut("CTRL+L")
        self.ite_report_parking.setShortcut("CTRL+Z")
        self.ite_show_credits.setShortcut("CTRL+S")

        # agregar item al menú
        menu_file.addAction(self.ite_register_input)
        menu_file.addAction(self.ite_report_output)
        menu_file.addAction(self.ite_report_parking)
        menu_archive.addAction(self.ite_open)
        menu_archive.addAction(self.ite_save)
        menu_help.addAction(self.ite_show_credits)

        tool_bar = QToolBar()
        tool_bar.setIconSize(QSize(32, 32))
        self.addToolBar(tool_bar)
        tool_bar.addAction(self.ite_register_input)
        tool_bar.addAction(self.ite_report_output)
        tool_bar.addAction(self.ite_report_parking)
        tool_bar.addSeparator()
        tool_bar.addAction(self.ite_show_credits)
        tool_bar.addSeparator()
        tool_bar.addAction(self.ite_open)
        tool_bar.addAction(self.ite_save)

        self.lab_f_salida = QLabel(self)
        self.lab_f_salida.setText("Vehículos en el Parqueadero")
        self.lab_f_salida.setGeometry(QRect(190, 70, 518, 44))
        self.lab_f_salida.setStyleSheet("font-size: 40px;")


        self.but_update = QPushButton(self)
        self.but_update.setText("Actualizar")
        self.but_update.setGeometry(QRect(415, 125, 85, 25))

        # Crea una tabla y la asocia a la ventana
        self.tab_parking = QTableWidget(self)
        self.tab_parking.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        # Ubicar tabla en la ventana (x,y,ancho,largo)
        self.tab_parking.setGeometry(QRect(100, 160, 700, 400))
        # Agregar filas y columnas a la tabla
        self.tab_parking.setColumnCount(5)
        self.tab_parking.setRowCount(0)
        # Agregar ancho a las columnas (indice, ancho)
        self.tab_parking.setColumnWidth(0, 100)  # columna 1 (ID)
        self.tab_parking.setColumnWidth(1, 200)  # columna 2 (Usuario)
        self.tab_parking.setColumnWidth(2, 110)  # columna 3 (Matricula)
        self.tab_parking.setColumnWidth(3, 130)  # columna 4 (Fecha entrada)
        self.tab_parking.setColumnWidth(4, 130)  # columna 5 (Hora entrada)
        # columna 8 (Registrar salida)
        self.tab_parking.setColumnWidth(5, 150)

        # Nombre en cabecera de la tabla
        ite_id = QTableWidgetItem("ID")
        self.tab_parking.setHorizontalHeaderItem(0, ite_id)
        ite_usuario = QTableWidgetItem("Usuario")
        self.tab_parking.setHorizontalHeaderItem(1, ite_usuario)
        ite_matricula = QTableWidgetItem("Matricula")
        self.tab_parking.setHorizontalHeaderItem(2, ite_matricula)
        ite_f_entrada = QTableWidgetItem("Fecha entrada")
        self.tab_parking.setHorizontalHeaderItem(3, ite_f_entrada)
        ite_h_entrada = QTableWidgetItem("Hora entrada")
        self.tab_parking.setHorizontalHeaderItem(4, ite_h_entrada)
       

    def __launch_events(self):
        self.ite_register_input.triggered.connect(self.__register_input)
        self.ite_report_output.triggered.connect(self.__report_output)
        self.ite_report_parking.triggered.connect(self.__report_parking)
        self.ite_show_credits.triggered.connect(self.__show_credits)
        self.but_update.clicked.connect(self.__report_service)
        self.ite_open.triggered.connect(self.__open)
        self.ite_save.triggered.connect(self.__save)

    def init_window(self):
        pass

    def __register_input(self):
        # Limpia componentes de la ventana
        self.__window_register_input.init_window()
        self.__window_register_input.setVisible(True)
        # Hace visible la ventana

    def __report_output(self):
        self.__window_register_output.init_window()
        self.__window_register_output.setVisible(True)
        # Hace visible la ventana
        pass

    def __report_parking(self):
        self.__window_report_parking.ini_window()
        self.__window_report_parking.setVisible(True)
        # Hace visible la ventana
        pass

    def __show_credits(self):
        # Hace visible la ventana
        self.window_credits.setVisible(True)

    def __report_service(self):
        self.tab_parking.setRowCount(0)
        list = self.__vector_parking_log.list_report_service()
        if list.size() > 0:

            i = list.front()
            while i != None:
                id = i.value.get_id()
                user = i.value.get_user()
                tuition = i.value.get_tuition()
                date_input = i.value.get_date_input()
                time_input = i.value.get_time_input()

                ite_id = QTableWidgetItem(str(id))
                ite_user = QTableWidgetItem(str(user))
                ite_tuition = QTableWidgetItem(str(tuition))
                ite_date = QTableWidgetItem(str(date_input))
                ite_time = QTableWidgetItem(str(time_input))


                self.tab_parking.insertRow(self.tab_parking.rowCount())
                self.tab_parking.setItem(
                    self.tab_parking.rowCount() - 1, 0, ite_id)
                self.tab_parking.setItem(
                    self.tab_parking.rowCount() - 1, 1, ite_user)
                self.tab_parking.setItem(
                    self.tab_parking.rowCount() - 1, 2, ite_tuition)
                self.tab_parking.setItem(
                    self.tab_parking.rowCount() - 1, 3, ite_date)
                self.tab_parking.setItem(
                    self.tab_parking.rowCount() - 1, 4, ite_time)

                i = i.next

    def __open(self):
        file = QFileDialog.getOpenFileName(
            self, "Abrir el  vehículos", "", "Archivo vehículos (*.vhl)")
        if file != ("", ""):
                self.file = file[0]
                self.__vector_parking_log.load_file(self.file)
                QMessageBox.information(self,"Gestor vehículo","vehículos cargados correctamente", QMessageBox.Ok,)
        
    def __save(self):
        if self.file != "":
            self.__vector_parking_log.save_file(self.file)
            QMessageBox.information(self,"Gestor vehículo","Cambios guardados correctamente", QMessageBox.Ok,)
        else:
            self.__save_as_file()
        

    def __save_as_file(self):
        file = QFileDialog.getSaveFileName(
        self, "Guardar como ", "", "Archivo vehículos(*.vhl)")
        if file != ("", ""):
                self.file = file[0]
                self.__vector_parking_log.save_file(self.file)
                QMessageBox.information(self,"Gestor vehículo","vehículos guardados correctamente", QMessageBox.Ok,)

    def closeEvent(self, Event):
        reply = QMessageBox.question(
            self, " Salir ", " ¿ Seguro que desea Salir ?", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            Event.accept()
        else:
            Event.ignore()