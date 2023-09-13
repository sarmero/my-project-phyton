import datetime
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRect, QRegExp, QSize, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QAction, QFileDialog,  QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QStyle, QTableWidget, QTableWidgetItem, QToolBar
from classes.ControlInOut import ControlInOut
from controller.ListControlIntOut import ListControlInOut
from structures.List import List
from view.CreditsView import CreditsView
from view.ReportParkingLogView import ReportParkingLogView



class MainWindowView(QMainWindow):

    def __init__(self):
        super().__init__()  # constructor de clase de padre
        # se separa memoria para arreglo de polígono
        self.__vector_parking = ListControlInOut()
        self.__window_report_parking = ReportParkingLogView(self.__vector_parking)
        self.__window_credits = CreditsView()
        self._vehicle: ControlInOut = None
        self.file_name:str = ""

        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Parking Long")
        self.setMinimumSize(1160, 680)

        # obtener barra de menú
        bar_menu = self.menuBar()

        # Adiciona opción al menú "&" sirve para dar acceso rápido
        menu_file = bar_menu.addMenu("&Archivo")
        tool_bar = bar_menu.addMenu("&Parqueadero")
        menu_help = bar_menu.addMenu("&Ayuda")

        # Crear Item de un menú
        self.ite_open_file = QAction("&Abrir", self)
        self.ite_save_file = QAction("&Guardar", self)
        self.ite_save = QAction("&Guardar como", self)
        self.ite_report_parking = QAction("&Reporte de Parqueadero", self)
        self.ite_exit = QAction("&Salir", self)
        self.ite_show_credits = QAction("&Créditos", self)
        
        # Agregar Ícono al Item del menú
        self.ite_open_file.setIcon(self.style().standardIcon(
            QStyle.SP_FileDialogNewFolder))
        self.ite_save.setIcon(self.style().standardIcon(
            QStyle.SP_FileDialogEnd))
        self.ite_save_file.setIcon(self.style().standardIcon(
            QStyle.SP_FileDialogStart))
        self.ite_report_parking.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogDetailedView))
        self.ite_exit.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogBack)) 
        self.ite_show_credits.setIcon(self.style().standardIcon(
            QStyle.SP_MessageBoxInformation))

        # agregar un short cut (acceso rápido)
        self.ite_open_file.setShortcut("CTRL+A")
        self.ite_save.setShortcut("CTRL+G")
        self.ite_save_file.setShortcut("CTRL+C")
        self.ite_report_parking.setShortcut("CTRL+R")
        self.ite_exit.setShortcut("CTRL+E")
        self.ite_show_credits.setShortcut("CTRL+S")

        # agregar item al menú
        menu_file.addAction(self.ite_open_file)
        menu_file.addAction(self.ite_save_file)
        menu_file.addAction(self.ite_save)
        tool_bar.addSeparator()
        tool_bar.addAction(self.ite_report_parking)
        tool_bar.addAction(self.ite_exit)
        tool_bar.addSeparator()
        menu_help.addAction(self.ite_show_credits)

        # estilo
        self.setStyleSheet("QMainWindow {background-color: #023047; border: 2px solid orange;}"+
                           "QMenuBar {background-color: #FFB703;}"+
                           "QToolBar {background-color: #FFB703;}"+
                           "QDialog {background-color: #023047;  border: 2px solid orange;}"+
                           "QPushButton {background-color: #FFB703; color: #023047;}"+
                           "QLabel {color: #FFB703;}"
        )

        
        # label
        self.lab_name = QLabel(self)
        self.lab_name.setText(" Vehículos en el Parqueadero ")
        self.lab_name.setGeometry(QRect(163, 66, 311, 28))
        self.lab_name.setStyleSheet("font-size: 24px; color: #FFB703;")

        #validador matricula 
        registration = QRegExp("[a-zA-Z0-9]{3}-[a-zA-Z0-9]{3}")
        validator_registration = QtGui.QRegExpValidator(registration)

        # label
        self.lab_search = QLabel(self)
        self.lab_search.setText("Matricula: ")
        self.lab_search.setGeometry(QRect(129, 111, 61, 30))
        self.lab_search.setStyleSheet("font-size: 14px; color: #FFB703;")

        # texto
        self.text_search = QLineEdit(self)
        self.text_search.setGeometry(QRect(198, 111, 90, 30))
        self.text_search.setStyleSheet("background-color: #023047; color: #FFB703; font-size: 14px; border-radius: 12px; border: 2px solid orange;")
        self.text_search.setValidator(validator_registration)

        # botón
        self.but_search = QPushButton(self)
        self.but_search.setText("Buscar")
        self.but_search.setGeometry(QRect(297, 111, 100, 30))
        self.but_search.setStyleSheet("QPushButton {background-color: #FFB703; color: #023047; border-radius: 12px; font-size: 14px; border: 2px solid white;}"+
                                      " QPushButton:hover{background-color: #023047; color: #FFB703; border: 2px solid #FFB703;}")

        # botón
        self.but_update = QPushButton(self)
        self.but_update.setText("Actualizar")
        self.but_update.setGeometry(QRect(403, 111, 100, 30))
        self.but_update.setStyleSheet("QPushButton {background-color: #219EBC; color: white; border-radius: 12px; font-size: 14px; border: 2px solid white;}"+
                                      " QPushButton:hover{background-color: #023047; color: #219EBC; border: 2px solid #219EBC;}")

        # tablas
        self.tab_vehicle = QTableWidget(self)
        self.tab_vehicle.setGeometry(QRect(60, 145, 500, 479))
        self.tab_vehicle.setAlternatingRowColors(True)
        self.tab_vehicle.setStyleSheet("alternate-background-color: #219EBC; background: #FFB703; border-radius: 12px; border: 2px solid #219EBC;")

        # colocar el ancho de cada columna
        self.tab_vehicle.setColumnCount(4)
        self.tab_vehicle.setRowCount(0)

        self.tab_vehicle.setColumnWidth(0, 100)
        self.tab_vehicle.setColumnWidth(1, 110)
        self.tab_vehicle.setColumnWidth(2, 135)
        self.tab_vehicle.setColumnWidth(3, 140)

        # nombre encabezado de la tabla
        ite_code = QTableWidgetItem("Código")
        ite_code.setSizeHint(QSize(100,30))
        ite_code.setBackground(QColor("#219EBC"))
        ite_code.setForeground(QColor("#023047"))
        self.tab_vehicle.setHorizontalHeaderItem(0, ite_code)
        ite_register = QTableWidgetItem("Matricula")
        ite_register.setBackground(QColor("#219EBC"))
        ite_register.setForeground(QColor("#023047"))
        self.tab_vehicle.setHorizontalHeaderItem(1, ite_register)
        ite_entry_date = QTableWidgetItem("Fecha de entrada")
        ite_entry_date.setBackground(QColor("#219EBC"))
        ite_entry_date.setForeground(QColor("#023047"))
        self.tab_vehicle.setHorizontalHeaderItem(2, ite_entry_date)
        ite_departure_date = QTableWidgetItem("Hora de entrada")
        ite_departure_date.setBackground(QColor("#219EBC"))
        ite_departure_date.setForeground(QColor("#023047"))
        self.tab_vehicle.setHorizontalHeaderItem(3, ite_departure_date)
        self.tab_vehicle.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # label
        self.lab_date = QLabel(self)
        self.lab_date.setText("Fecha: ")
        self.lab_date.setGeometry(QRect(767, 90, 45, 30))
        self.lab_date.setStyleSheet("font-size: 14px; color: #FFB703;")

        # texto
        self.text_date = QLineEdit(self)
        self.text_date.setGeometry(QRect(822, 90, 111, 30))
        self.text_date.setStyleSheet("background-color: #023047; color: #FFB703; font-size: 14px; border-radius: 12px; border: 2px solid orange; ")
        self.text_date.setText(datetime.datetime.now().strftime("%d - %m - %Y"))
        self.text_date.setReadOnly(True)
        self.text_date.setAlignment(Qt.AlignHCenter)

        # tablas
        self.tab_register = QTableWidget(self)
        self.tab_register.setGeometry(QRect(600, 145, 500, 200))
        self.tab_register.setStyleSheet("background-color: #FFB703; border-radius: 18px; border: 2px solid #219EBC;")


        self.tab_name = QLabel(self)
        self.tab_name.setText("Información de entrada Vehículos")
        self.tab_name.setGeometry(QRect(705, 161, 290, 26))
        self.tab_name.setStyleSheet("font-size: 18px; color: #023047;")

        # validador solo números
        code = QRegExp("[0-9]*")
        validator = QtGui.QRegExpValidator(code)

        self.tab_code = QLabel(self)
        self.tab_code.setText("Código: ")
        self.tab_code.setGeometry(QRect(652, 210, 51, 30))
        self.tab_code.setStyleSheet("font-size: 14px; color: #023047;")

        #texto
        self.text_code = QLineEdit(self)
        self.text_code.setGeometry(QRect(741, 210, 116, 30))
        self.text_code.setStyleSheet("background-color: #FFB703; color: #023047; font-size: 14px; border-radius: 12px; border: 2px solid #023047;")
        self.text_code.setValidator(validator)
        
        self.tab_registration = QLabel(self)
        self.tab_registration.setText("Matricula: ")
        self.tab_registration.setGeometry(QRect(652, 250, 69, 30))
        self.tab_registration.setStyleSheet("font-size: 14px; color: #023047;")
        
        #texto
        self.text_registration = QLineEdit(self)
        self.text_registration.setGeometry(QRect(741, 250, 116, 30))
        self.text_registration.setStyleSheet("background-color: #FFB703; color: #023047; font-size: 14px; border-radius: 12px; border: 2px solid #023047;")
        self.text_registration.setValidator(validator_registration)

        # botón
        self.but_add_ok = QPushButton(self)
        self.but_add_ok.setText("Registrar Entrada")
        self.but_add_ok.setGeometry(QRect(886, 207, 145, 75))
        self.but_add_ok.setStyleSheet("QPushButton {background-color: #023047; color: #FFB703; border-radius: 12px; font-size: 18px; border: 2px solid #219EBC;}"+
                                      " QPushButton:hover{background-color: #FFB703; color: #023047; border: 2px solid #023047;}")

        # tablas
        self.chart_open = QTableWidget(self)
        self.chart_open.setGeometry(QRect(600, 391, 500, 233))
        self.chart_open.setStyleSheet("background-color: #FFB703; border-radius: 18px; border: 2px solid #219EBC;")

        self.chart_name = QLabel(self)
        self.chart_name.setText(" Información de salida Vehículos")
        self.chart_name.setGeometry(QRect(705, 407, 283, 26))
        self.chart_name.setStyleSheet("font-size: 18px; color: #023047;")

        self.chart_code = QLabel(self)
        self.chart_code.setText("Código: ")
        self.chart_code.setGeometry(QRect(652, 452, 52, 30))
        self.chart_code.setStyleSheet("font-size: 14px; color: #023047;")

        #texto
        self.tex_code = QLineEdit(self)
        self.tex_code.setGeometry(QRect(773, 452, 95, 30))
        self.tex_code.setStyleSheet("background-color: #FFB703; color: #023047; font-size: 14px; border-radius: 12px; border: 2px solid  #023047;")
        self.tex_code.setValidator(validator)
        
        
        self.chart_registration = QLabel(self)
        self.chart_registration.setText("Matricula: ")
        self.chart_registration.setGeometry(QRect(652, 486, 250, 30))
        self.chart_registration.setStyleSheet("font-size: 14px; color: #023047;")
        
        #texto
        self.tex_registration = QLineEdit(self)
        self.tex_registration.setGeometry(QRect(773, 486, 95, 30))
        self.tex_registration.setStyleSheet("background-color: #FFB703; color: #023047; font-size: 14px; border-radius: 12px; border: 2px solid #023047;")
        self.tex_registration.setReadOnly(True)
        self.tex_registration.setAlignment(Qt.AlignHCenter)

        self.chart_time = QLabel(self)
        self.chart_time.setText("Tiempo (minuto): ")
        self.chart_time.setGeometry(QRect(652, 525, 121, 30))
        self.chart_time.setStyleSheet("font-size: 14px; color: #023047;")

        #texto
        self.tex_time = QLineEdit(self)
        self.tex_time.setGeometry(QRect(773, 525, 95, 30))
        self.tex_time.setStyleSheet("background-color: #FFB703; color: #023047; font-size: 14px; border-radius: 12px; border: 2px solid #023047;")
        self.tex_time.setReadOnly(True)
        self.tex_time.setAlignment(Qt.AlignHCenter)

        self.chart_cost = QLabel(self)
        self.chart_cost.setText("Costo: ")
        self.chart_cost.setGeometry(QRect(652, 559, 121, 30))
        self.chart_cost.setStyleSheet("font-size: 14px; color: #023047;")

        #texto
        self.tex_cost = QLineEdit(self)
        self.tex_cost.setGeometry(QRect(773, 559, 95, 30))
        self.tex_cost.setStyleSheet("background-color: #FFB703; color: #023047; font-size: 14px; border-radius: 12px; border: 2px solid #023047;")
        self.tex_cost.setReadOnly(True)
        self.tex_cost.setAlignment(Qt.AlignHCenter)

        self.but_search_off = QPushButton(self)
        self.but_search_off.setText("Buscar")
        self.but_search_off.setGeometry(QRect(886, 449, 80, 30))
        self.but_search_off.setStyleSheet("QPushButton {background-color: #219EBC; color: #023047; border-radius: 12px; font-size: 14px; border: 2px solid #023047;}"+
                                      " QPushButton:hover{background-color: #FFB703; color: #219EBC; border: 2px solid #219EBC;}")

        # botón
        self.but_off = QPushButton(self)
        self.but_off.setText("Registrar Salida")
        self.but_off.setGeometry(QRect(886, 511, 145, 75))
        self.but_off.setStyleSheet("QPushButton {background-color: #023047; color: #FFB703; border-radius: 12px; font-size: 18px; border: 2px solid #219EBC;}"+
                                      " QPushButton:hover{background-color: #FFB703; color: #023047; border: 2px solid #023047;}")


        # toolbar
        tool_bar = QToolBar(self)
        tool_bar.setIconSize(QSize(40, 20))
        self.addToolBar(tool_bar)
        tool_bar.addAction(self.ite_open_file)
        tool_bar.addAction(self.ite_save_file)
        tool_bar.addAction(self.ite_save)
        tool_bar.addSeparator()
        tool_bar.addAction(self.ite_report_parking)
        tool_bar.addSeparator()
        tool_bar.addAction(self.ite_exit)
        tool_bar.addAction(self.ite_show_credits)

    def __launch_events(self):
        # Conectar el método a el evento clic de un item del menú
        self.ite_report_parking.triggered.connect(self.__report_parking)
        self.ite_show_credits.triggered.connect(self.__show_credits)
        self.ite_open_file.triggered.connect(self.__open_file)
        self.ite_save_file.triggered.connect(self.__save_file)
        self.ite_save.triggered.connect(self.__save_as_file)
        self.but_update.clicked.connect(self.__show_update)
        self.but_search.clicked.connect(self.__show_by_registration_number)
        self.but_search_off.clicked.connect(self.__show_report_by_code)
        self.but_add_ok.clicked.connect(self.__ok)
        self.but_off.clicked.connect(self.__register_off)

    def init_window(self):
        self.but_off.setEnabled(False)
        self.tex_registration.setText("")
        self.tex_time.setText("")
        self.tex_cost.setText("")
        

    def __show_report_by_code(self):
        code = self.tex_code.text()
        if code != "":
            vehicle: ControlInOut = self.__vector_parking.search_by_code(int(code))
            self.init_window()

            if vehicle is not None:

                date = datetime.datetime.now()
                date_out = date.strftime('%d-%m-%Y')
                time_out = date.strftime('%H:%M')

                vehicle.date_out = date_out
                vehicle.time_out = time_out
                vehicle.calculate_minutes()
                vehicle.calculate_cost()

                self.tex_registration.setText(str(vehicle.registration_number))
                self.tex_time.setText(str(vehicle.minutes))
                self.tex_cost.setText(str(vehicle.cost))
                self.but_off.setEnabled(True)
                self._vehicle = vehicle
            else:
                QMessageBox.information(self,"Gestor vehículo"," Vehículo no encontrado",QMessageBox.Ok,)
        else:
            self._vehicle = None
            QMessageBox.information(self,"Gestor vehículo","Error por campo vació",QMessageBox.Ok,)

            

    def __register_off(self):
        self.__vector_parking.register_input(self._vehicle)
        self._vehicle = None
        self.tex_code.setText("")
        QMessageBox.information(self,"Gestor vehículo"," Vehículo registrado correctamente",QMessageBox.Ok,)
        self.init_window()

    def __ok(self):
        code = self.text_code.text()
        registration_number = self.text_registration.text()

        if code != "" and registration_number != "":
            valid:bool = self.__vector_parking.search_code_validate(int(code))
            valid_number:bool = self.__vector_parking.search_number_validate(registration_number)

            if valid is False:
                if valid_number is False:
                    date = datetime.datetime.now()
                    date_in = date.strftime('%d-%m-%Y')
                    time_in = date.strftime('%H:%M')

                    vehicle = ControlInOut(int(code), registration_number, date_in, time_in)
                    self.__vector_parking.add_control_in_out(vehicle)
                    self.text_code.setText("")
                    self.text_registration.setText("")

                    QMessageBox.information(self,"Gestor vehículo"," Vehículo agregado correctamente",QMessageBox.Ok,)
                else:
                    QMessageBox.information(self,"Gestor vehículo","Error, la matricula ya existe \n ya se encuentra el Vehículo en el Parqueadero",QMessageBox.Ok,)
            else:
                QMessageBox.information(self,"Gestor vehículo","Error, El código ya existe",QMessageBox.Ok,)
        else:
            QMessageBox.information(self,"Gestor vehículo","Error, todos los campos son obligatorios",QMessageBox.Ok,)

    def __show_update(self):
        self.tab_vehicle.setRowCount(0)
        list:List = self.__vector_parking.list_in_service()
        size_list = list.size()

        if size_list > 0:
            i = list.front()
            while i is not None:
                code = i.value.code
                registration_number = i.value.registration_number
                date_in = i.value.date_in
                time_in = i.value.time_in

                ite_code = QTableWidgetItem(str(code))
                ite_registration_number = QTableWidgetItem(str(registration_number))
                ite_date = QTableWidgetItem(str(date_in))
                ite_time = QTableWidgetItem(str(time_in))

                self.tab_vehicle.insertRow(self.tab_vehicle.rowCount())
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 0, ite_code)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 1, ite_registration_number)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 2, ite_date)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 3, ite_time)

                i = i.next
                

    def __show_by_registration_number(self):
        self.tab_vehicle.setRowCount(0)
        registration_number = self.text_search.text()
        
        if registration_number != "":
            vehicle: ControlInOut = self.__vector_parking .search_by_registration_number_service(registration_number)
            
            if vehicle is not None:
                code = vehicle.code
                registration_number = vehicle.registration_number
                date_in = vehicle.date_in
                time_in = vehicle.time_in

                ite_code = QTableWidgetItem(str(code))
                ite_registration_number = QTableWidgetItem(str(registration_number))
                ite_date = QTableWidgetItem(str(date_in))
                ite_time = QTableWidgetItem(str(time_in))

                self.tab_vehicle.insertRow(self.tab_vehicle.rowCount())
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 0, ite_code)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 1, ite_registration_number)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 2, ite_date)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 3, ite_time)

            else:
                QMessageBox.information(self,"Gestor Vehículo"," Vehículo no encontrado",QMessageBox.Ok,)

        else:
            QMessageBox.information(self,"Gestor Vehículo","Error, por favor escriba una matricula valida",QMessageBox.Ok,)


    def __report_parking(self):
        # Hace visible la ventana
        self.__window_report_parking.init_window()
        self.__window_report_parking.setVisible(True)

    def __show_credits(self):
        # Hace visible la ventana
        self.__window_credits.setVisible(True)

    def __save_file(self):
        if self.file_name != "":
            self.__vector_parking.save_control(self.file_name)
            QMessageBox.information(self,"Gestor vehículo","Cambios guardados correctamente", QMessageBox.Ok,)
        else:
            self.__save_as_file()
        

    def __save_as_file(self):
        file_name = QFileDialog.getSaveFileName(
        self, "Guardar el polígono", "", "Archivo polígono(*.plg)")
        if file_name != ("", ""):
                self.file_name = file_name[0]
                self.__vector_parking.save_control(self.file_name)
                QMessageBox.information(self,"Gestor vehículo","Lista vehículo guardada correctamente", QMessageBox.Ok,)

    def __open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Abrir lista vehículo", "", "Lista vehículo (*.plg)")
        if file_name != ("", ""):
                print(file_name[0])
                self.file_name = file_name[0]
                self.__vector_parking.load_control(self.file_name)
                QMessageBox.information(self,"Gestor vehículo","Lista vehículo cargada correctamente", QMessageBox.Ok,)
        
        

    def closeEvent(self, Event):
        reply = QMessageBox.question(
            self, " Salir ", " Seguro Desea Salir ", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            Event.accept()
        else:
            Event.ignore()
