
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QDate, QRect, QRegExp, Qt
from PyQt5.QtWidgets import QDateEdit, QDialog, QLabel, QLineEdit, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem
from tkinter import * 
import datetime
from classes.ControlInOut import ControlInOut

from structures.List import List

class ReportParkingLogView(QDialog):

    def __init__(self, vector_parking):
        super().__init__()
        self.__vector_parking = vector_parking
        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Reporte de Parqueadero")
        # tamaño fijo
        self.setFixedSize(750, 420)
        # activar una ventana modal(no funciona la principal hasta que termine la secundaria)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # estilo
        self.setStyleSheet("QMainWindow {background-color: #023047; border: 2px solid orange;}"+
                           "QMenuBar {background-color: #FFB703;}"+
                           "QToolBar {background-color: #FFB703;}"+
                           "QDialog {background-color: #023047;  border: 2px solid orange;}"+
                           "QPushButton {background-color: #FFB703; color: #023047;}"+
                           "QLabel {color: #FFB703;}"
        )

        self.tab_vehicle = QTableWidget(self)
        self.tab_vehicle.setGeometry(QRect(20, 80, 710, 280))
        self.tab_vehicle.setAlternatingRowColors(True)
        self.tab_vehicle.setStyleSheet("alternate-background-color: #219EBC; background: #FFB703; border-radius: 12px; border: 2px solid #219EBC;")

        # colocar el ancho de cada columna
        self.tab_vehicle.setColumnCount(8)
        self.tab_vehicle.setRowCount(0)

        self.tab_vehicle.setColumnWidth(0, 70)
        self.tab_vehicle.setColumnWidth(1, 70)
        self.tab_vehicle.setColumnWidth(2, 110)
        self.tab_vehicle.setColumnWidth(3, 110)
        self.tab_vehicle.setColumnWidth(4, 100)
        self.tab_vehicle.setColumnWidth(5, 100)
        self.tab_vehicle.setColumnWidth(6, 70)
        self.tab_vehicle.setColumnWidth(7, 75)


        # nombre encabezado de la tabla
        ite_code = QTableWidgetItem("Código")
        self.tab_vehicle.setHorizontalHeaderItem(0, ite_code)
        ite_registration = QTableWidgetItem("Matricula")
        self.tab_vehicle.setHorizontalHeaderItem(1, ite_registration)
        ite_date = QTableWidgetItem("Fecha de entrada")
        self.tab_vehicle.setHorizontalHeaderItem(2, ite_date)
        ite_time = QTableWidgetItem("Hora de entrada")
        self.tab_vehicle.setHorizontalHeaderItem(3, ite_time)
        ite_exit = QTableWidgetItem("Fecha de salida")
        self.tab_vehicle.setHorizontalHeaderItem(4, ite_exit)
        ite_output = QTableWidgetItem("Hora de salida")
        self.tab_vehicle.setHorizontalHeaderItem(5, ite_output)
        ite_period = QTableWidgetItem("Tiempo")
        self.tab_vehicle.setHorizontalHeaderItem(6, ite_period)
        ite_cost = QTableWidgetItem("Costo")
        self.tab_vehicle.setHorizontalHeaderItem(7, ite_cost)
        self.tab_vehicle.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)


        self.but_add_ok = QPushButton(self)
        self.but_search = QPushButton(self)
        self.but_look = QPushButton(self)


        self.but_add_ok.setText("Aceptar")
        self.but_add_ok.setGeometry(QRect(525, 375, 100, 30))
        self.but_add_ok.setStyleSheet("QPushButton {background-color: #219EBC; color: white; border-radius: 12px; font-size: 14px; border: 2px solid white;}"+
                                      " QPushButton:hover{background-color: #023047; color: #219EBC; border: 2px solid #219EBC;}")


        self.tab_name = QLabel(self)
        self.tab_name.setText("Total Recaudado:")
        self.tab_name.setGeometry(QRect(60, 375, 110, 30))
        self.tab_name.setStyleSheet("font-size: 14px; color: #FFB703;")


        self.text_total = QLineEdit(self)
        self.text_total.setGeometry(QRect(200, 375, 100, 30))
        self.text_total.setStyleSheet("background-color: #023047; color: #FFB703; font-size: 14px; border-radius: 12px; border: 2px solid orange;")
        self.text_total.setReadOnly(True)
        self.text_total.setAlignment(Qt.AlignHCenter)

        self.tab_registration = QLabel(self)
        self.tab_registration.setText("Matricula: ")
        self.tab_registration.setGeometry(QRect(30, 30, 100, 30))
        self.tab_registration.setStyleSheet("font-size: 14px; color: #FFB703;")

        registration = QRegExp("[a-zA-Z0-9]{3}-[a-zA-Z0-9]{3}")
        validator_registration = QtGui.QRegExpValidator(registration)

        self.text_registration = QLineEdit(self)
        self.text_registration.setGeometry(QRect(100, 30, 90, 30))
        self.text_registration.setStyleSheet("background-color: #023047;color: #FFB703; font-size: 14px; border-radius: 12px; border: 2px solid orange;")
        self.text_registration.setValidator(validator_registration)

        self.but_search.setText("Buscar")
        self.but_search.setGeometry(QRect(200, 30, 100, 30))
        self.but_search.setStyleSheet("QPushButton {background-color: #FFB703; color: #023047; border-radius: 12px; font-size: 14px; border: 2px solid white;}"+
                                      " QPushButton:hover{background-color: #023047; color: #FFB703; border: 2px solid #FFB703;}")

        self.tab_input = QLabel(self)
        self.tab_input.setText("Fecha de Entrada: ")
        self.tab_input.setGeometry(QRect(340, 30, 110, 30))
        self.tab_input.setStyleSheet("font-size: 14px; color: #FFB703;")

        self.but_look.setText("Buscar")
        self.but_look.setGeometry(QRect(600, 30, 100, 30))
        self.but_look.setStyleSheet("QPushButton {background-color: #FFB703; color: #023047; border-radius: 12px; font-size: 14px; border: 2px solid white;}"+
                                      " QPushButton:hover{background-color: #023047; color: #FFB703; border: 2px solid #FFB703;}")

        self.date_in = QDateEdit(QDate.currentDate(), self, calendarPopup=True)
        self.date_in.setDisplayFormat("dd/MM/yyyy")
        self.date_in.setGeometry(QRect(450, 30, 130, 30))
        self.date_in.setMinimumDate(QDate.currentDate().addDays(-365))
        self.date_in.setMaximumDate(QDate.currentDate().addDays(365))
        self.date_in.setStyleSheet("background-color: #023047; color: #FFB703; font-size: 12px; border-radius: 10px; border: 2px solid orange;")
        self.date_in.setAlignment(Qt.AlignHCenter)

    def __launch_events(self):
        self.but_add_ok.clicked.connect(self.__ok)
        self.but_search.clicked.connect(self.__show_by_number)
        self.but_look.clicked.connect(self.__show_by_date)
        

    def init_window(self):
        self.tab_vehicle.setRowCount(0)
        self.text_total.setText("")

    def __ok(self):
        self.setVisible(False)

    def __show_by_number(self):
        self.tab_vehicle.setRowCount(0)
        registration_number = self.text_registration.text()

        if registration_number != "":
            vehicle: ControlInOut = self.__vector_parking.search_by_registration_number(registration_number)
            
            if vehicle is not None:
                code = vehicle.code
                registration_number = vehicle.registration_number
                date_in = vehicle.date_in
                time_in = vehicle.time_in
                date_out = vehicle.date_out
                time_out = vehicle.time_out
                minutes = vehicle.minutes
                cost = vehicle.cost

                ite_code = QTableWidgetItem(str(code))
                ite_registration_number = QTableWidgetItem(str(registration_number))
                ite_date_in = QTableWidgetItem(str(date_in))
                ite_time_in = QTableWidgetItem(str(time_in))
                ite_date_out = QTableWidgetItem(str(date_out))
                ite_time_out = QTableWidgetItem(str(time_out))
                ite_minutes = QTableWidgetItem(str(minutes))
                ite_cost = QTableWidgetItem(str(cost))

                self.tab_vehicle.insertRow(self.tab_vehicle.rowCount())
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 0, ite_code)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 1, ite_registration_number)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 2, ite_date_in)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 3, ite_time_in)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 4, ite_date_out)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 5, ite_time_out)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 6, ite_minutes)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 7, ite_cost)


                self.text_total.setText(str(vehicle.cost))
            else:
                QMessageBox.information(self,"Gestor vehículo"," vehículo no encontrado",QMessageBox.Ok,)
        else:
            QMessageBox.information(self,"Gestor vehículo","Error por campo vació",QMessageBox.Ok,)

    def __show_by_date(self):
        self.tab_vehicle.setRowCount(0)
        date_in = self.date_in.date().toString("dd-MM-yyyy")
        cost_total = 0

        list:List = self.__vector_parking.search_by_date_in(date_in)
        size_list = list.size()

        if size_list > 0:
            i = list.front()
            while i is not None:
                code = i.value.code
                registration_number = i.value.registration_number
                date_in = i.value.date_in
                time_in = i.value.time_in
                date_out = i.value.date_out
                time_out = i.value.time_out
                minutes = i.value.minutes
                cost = i.value.cost
                cost_total += cost

                ite_code = QTableWidgetItem(str(code))
                ite_registration_number = QTableWidgetItem(str(registration_number))
                ite_date = QTableWidgetItem(str(date_in))
                ite_time = QTableWidgetItem(str(time_in))
                ite_date_out = QTableWidgetItem(str(date_out))
                ite_time_out = QTableWidgetItem(str(time_out))
                ite_minutes = QTableWidgetItem(str(minutes))
                ite_cost = QTableWidgetItem(str(cost))

                self.tab_vehicle.insertRow(self.tab_vehicle.rowCount())
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 0, ite_code)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 1, ite_registration_number)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 2, ite_date)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 3, ite_time)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 4, ite_date_out)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 5, ite_time_out)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 6, ite_minutes)
                self.tab_vehicle.setItem(self.tab_vehicle.rowCount() - 1, 7, ite_cost)

                i = i.next

            self.text_total.setText(str(cost_total))
        else:
            QMessageBox.information(self,"Gestor vehículo","Error no se encontraron registro con la fecha solicitada",QMessageBox.Ok,)