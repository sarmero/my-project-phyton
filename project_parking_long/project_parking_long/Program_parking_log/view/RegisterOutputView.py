from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, QRect, QTime, Qt
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QComboBox, QDateEdit, QDateTimeEdit, QDialog, QLabel, QLineEdit, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem, QTimeEdit


class RegisterOutputView(QDialog):
    def __init__(self, vector_parking_log):
        super().__init__()  # Constructor de la clase padre
        self.__vector_parking_log = vector_parking_log
        self.__vehicle = None
        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Registro  salida de vehículo")
        self.setFixedSize(700, 490)
        # Activar una ventana modal(no funciona la principal hasta que termine la secundaria)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        # Quita el botón de ayuda de la ventana
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.lab_code = QLabel(self)
        self.lab_code.setText("Código de entrada: ")
        self.lab_code.setGeometry(QRect(100, 20, 150, 25))

        self.com_code = QComboBox(self)
        self.com_code.setGeometry(QRect(240, 20, 70, 25))

        self.lab_f_salida = QLabel(self)
        self.lab_f_salida.setText("Fecha de salida: ")
        self.lab_f_salida.setGeometry(QRect(100, 160, 150, 25))

        self.tab_parking = QTableWidget(self)
        self.tab_parking.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        # Ubicar tabla en la ventana (x,y,ancho,largo)
        self.tab_parking.setGeometry(QRect(100, 60, 490, 70))
        # Agregar filas y columnas a la tabla
        self.tab_parking.setColumnCount(5)
        self.tab_parking.setRowCount(0)
        # Agregar ancho a las columnas (indice, ancho)
        self.tab_parking.setColumnWidth(0, 80)  # columna 1 (ID)
        self.tab_parking.setColumnWidth(1, 120)  # columna 2 (Usuario)
        self.tab_parking.setColumnWidth(2, 80)  # columna 3 (Matricula)
        self.tab_parking.setColumnWidth(3, 100)  # columna 4 (Fecha entrada)
        self.tab_parking.setColumnWidth(4, 100)  # columna 5 (Hora entrada)
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

        self.date_input = QDateEdit(
            QDate.currentDate(), self, calendarPopup=True)
        self.date_input.setDisplayFormat("yyyy/MM/dd")
        self.date_input.setGeometry(QRect(240, 160, 200, 25))
        self.date_input.setMinimumDate(QDate.currentDate().addDays(-365))
        self.date_input.setMaximumDate(QDate.currentDate().addDays(365))

        self.lab_h_salida = QLabel(self)
        self.lab_h_salida.setText("Hora de salida: ")
        self.lab_h_salida.setGeometry(QRect(100, 200, 150, 25))
        self.time_input = QTimeEdit(QTime.currentTime(), self)
        self.time_input.setDisplayFormat("hh:mm ap")
        self.time_input.setGeometry(QRect(240, 200, 200, 25))

        self.lab_c_minutos = QLabel(self)
        self.lab_c_minutos.setText("Cantidad de minutos: ")
        self.lab_c_minutos.setGeometry(QRect(100, 250, 150, 25))
        self.text_c_minutos = QLineEdit(self)
        self.text_c_minutos.setGeometry(QRect(240, 250, 60, 25))
        self.text_c_minutos.setReadOnly(True)

        self.lab_cos_servicio = QLabel(self)
        self.lab_cos_servicio.setText("Costo de servicio: ")
        self.lab_cos_servicio.setGeometry(QRect(100, 290, 150, 25))
        self.text_cos_servicio = QLineEdit(self)
        self.text_cos_servicio.setGeometry(QRect(240, 290, 60, 25))
        self.text_cos_servicio.setReadOnly(True)

        self.but_ok = QPushButton(self)
        self.but_ok.setText("Aceptar")
        self.but_ok.setGeometry(QRect(200, 420, 100, 25))

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(360, 420, 100, 25))
        

    def __launch_events(self):
        self.but_ok.clicked.connect(self.__ok)
        self.but_cancel.clicked.connect(self.__cancel)
        self.com_code.currentTextChanged.connect(self.__search_vehicle)
        self.date_input.dateChanged.connect(self.__report_data)
        self.time_input.timeChanged.connect(self.__report_data)

    def init_window(self):
        self.__init_combo()

        pass

    def __init_combo(self):
        # limpiar el contenido del combo
        self.com_code.clear()
        # obtener el arreglo de polígonos
        list = self.__vector_parking_log.get_list()
        # ciclo para recorrer el arreglo de
        i = list.front()
        while i != None:
            control = i.value
            # Adicionar item al combo
            self.com_code.addItem(control.get_code())
            i = i.next

    def __ok(self):
        if self.__vehicle is not None:
            self.__vector_parking_log.register_output(self.__vehicle)
            QtWidgets.QMessageBox.information(
                self, "Vehículo", "la salida del  vehículo ha sido registrada", QtWidgets.QMessageBox.Ok)

            self.setVisible(False)

    def __search_vehicle(self):
        self.tab_parking.setRowCount(0)
        code = self.com_code.currentText()
        control = self.__vector_parking_log.search_by_code(code)
        self.__vehicle = control

        if self.__vehicle is not None:
            id = control.get_id()
            user = control.get_user()
            tuition = control.get_tuition()
            date_input = control.get_date_input()
            time_input = control.get_time_input()

            ite_id = QTableWidgetItem(str(id))
            ite_user = QTableWidgetItem(str(user))
            ite_tuition = QTableWidgetItem(str(tuition))
            ite_date_input = QTableWidgetItem(str(date_input))
            ite_time_input = QTableWidgetItem(str(time_input))

            self.tab_parking.insertRow(self.tab_parking.rowCount())
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 0, ite_id)
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 1, ite_user)
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 2, ite_tuition)
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 3, ite_date_input)
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 4, ite_time_input)
           
    def __report_data(self):
        if self.__vehicle is not None:
            date_output = self.date_input.date().toString("dd-MM-yyyy")
            time_output = self.time_input.time().toString("hh:mm")

            self.__vehicle.set_departure_date(date_output, time_output)
            self.__vehicle.set_tarife(2500)
            cost = self.__vehicle.parking_cost()
            self.text_c_minutos.setText(self.__vehicle.time())
            self.text_cos_servicio.setText(str(cost))

    def __cancel(self):
        self.setVisible(False)
