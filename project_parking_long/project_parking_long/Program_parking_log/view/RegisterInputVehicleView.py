
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QDate, QRect, QRegExp, QTime, Qt
from PyQt5.QtWidgets import QDateEdit, QDateTimeEdit, QDialog, QLabel, QLineEdit, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem, QTimeEdit

from classes.ControlInputOutput import ControlInputOutput


class RegisterInputVehicleView(QDialog):
    def __init__(self, vector_parking_log):

        super().__init__()  # Constructor de la clase padre

        self.__launch_widgets()
        self.__vector_parking_log = vector_parking_log
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Registrar Entrada vehículos")
        self.setFixedSize(670, 390)
        # Activar una ventana modal(no funciona la principal hasta que termine la secundaria)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        # Quita el botón de ayuda de la ventana
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        code = QRegExp("^[a-zA-Z0-9]*$")

        self.lab_code = QLabel(self)
        self.lab_code.setText("Código: ")
        self.lab_code.setGeometry(QRect(100, 20, 150, 25))
        self.text_code = QLineEdit(self)
        self.text_code.setGeometry(QRect(240, 20, 200, 25))
        self.text_code.setValidator(QtGui.QRegExpValidator(code))

        id = QRegExp("[0-9]*")

        self.lab_id = QLabel(self)
        self.lab_id.setText("ID: ")
        self.lab_id.setGeometry(QRect(100, 60, 150, 25))
        self.text_id = QLineEdit(self)
        self.text_id.setGeometry(QRect(240, 60, 200, 25))
        self.text_id.setValidator(QtGui.QRegExpValidator(id))

        self.lab_user = QLabel(self)
        self.lab_user.setText("Usuario: ")
        self.lab_user.setGeometry(QRect(100, 100, 150, 25))
        self.text_user = QLineEdit(self)
        self.text_user.setGeometry(QRect(240, 100, 200, 25))

        self.lab_tuition = QLabel(self)
        self.lab_tuition.setText("Matricula vehículos: ")
        self.lab_tuition.setGeometry(QRect(100, 140, 150, 25))

        matricula = QRegExp("^[A-Z0-9]{3}-[A-Z0-9]{3}$")
        self.text_matricula = QLineEdit(self)
        self.text_matricula.setGeometry(QRect(240, 140, 200, 25))
        self.text_matricula.setValidator(QtGui.QRegExpValidator(matricula))

        self.lab_f_income = QLabel(self)
        self.lab_f_income.setText("Fecha de entrada: ")
        self.lab_f_income.setGeometry(QRect(100, 190, 150, 25))
        self.date_input = QDateEdit(
            QDate.currentDate(), self, calendarPopup=True)
        self.date_input.setDisplayFormat("yyyy/MM/dd")
        self.date_input.setGeometry(QRect(240, 190, 200, 25))
        self.date_input.setMinimumDate(QDate.currentDate().addDays(-365))
        self.date_input.setMaximumDate(QDate.currentDate().addDays(365))

        self.lab_h_income = QLabel(self)
        self.lab_h_income.setText("Hora de entrada: ")
        self.lab_h_income.setGeometry(QRect(100, 220, 150, 25))
        self.time_input = QTimeEdit(QTime.currentTime(), self)
        self.time_input.setDisplayFormat("hh:mm ap")
        self.time_input.setGeometry(QRect(240, 240, 200, 25))

        self.but_ok = QPushButton(self)
        self.but_ok.setText("Aceptar")
        self.but_ok.setGeometry(QRect(200, 320, 100, 25))

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(360, 320, 100, 25))

    def __launch_events(self):
        self.but_ok.clicked.connect(self.__ok)
        self.but_cancel.clicked.connect(self.__cancel)

    def init_window(self):
        self.text_id.setText("")
        self.text_user.setText("")
        self.text_matricula.setText("")

    def __ok(self):
        code = self.text_code.text()
        id = self.text_id.text()
        user = self.text_user.text()
        tuition = self.text_matricula.text()
        if code != "" and id != "" and user != "" and tuition != "" :
            str_date_input = self.date_input.date().toString("dd-MM-yyyy")
            str_time_input = self.time_input.time().toString("hh:mm")

            output = ControlInputOutput(
                code, id, user, tuition, str_date_input, str_time_input)
            self.__vector_parking_log.add_vehicle(output)

            QMessageBox.information(
                self, "Vehículo", "El vehículo ha sido registrado", QMessageBox.Ok)

            self.setVisible(False)
        else:
            QMessageBox.information(
                self, "Vehículo", "Todos los campos son obligatorios", QMessageBox.Ok)

    def __cancel(self):
        self.setVisible(False)
