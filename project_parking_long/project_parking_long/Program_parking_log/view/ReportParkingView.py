from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import QDate, QRect, QRegExp, Qt
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QDateEdit, QDialog, QLabel, QLineEdit, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem


class ReportParkingView(QDialog):
    def __init__(self, vector_parking_log):
        super().__init__()  # Constructor de la clase padre
        self.__vector_parking_log = vector_parking_log
        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Reporte vehículo")
        self.setFixedSize(1024, 600)
        # Activar una ventana modal(no funciona la principal hasta que termine la secundaria)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        # Quita el botón de ayuda de la ventana
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.tab_parking = QTableWidget(self)
        self.tab_parking.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        # Ubicar tabla en la ventana (x,y,ancho,largo)
        self.tab_parking.setGeometry(QRect(20, 110, 984, 380))
        # Agregar filas y columnas a la tabla
        self.tab_parking.setColumnCount(9)
        self.tab_parking.setRowCount(0)
        # Agregar ancho a las columnas (indice, ancho)
        self.tab_parking.setColumnWidth(0, 80)  # columna 1 (ID)
        self.tab_parking.setColumnWidth(1, 80)  # columna 2 (Usuario)
        self.tab_parking.setColumnWidth(2, 150)  # columna 3 (Matricula)
        self.tab_parking.setColumnWidth(3, 150)  # columna 4 (Fecha entrada)
        self.tab_parking.setColumnWidth(4, 150)  # columna 5 (Hora entrada)
        self.tab_parking.setColumnWidth(5, 150)  # columna 6 (Fecha salida)
        self.tab_parking.setColumnWidth(6, 150)  # columna 7 (Hora salida)
        self.tab_parking.setColumnWidth(7, 150)  # columna 8 (Tiempo)
        self.tab_parking.setColumnWidth(8, 150)  # columna 9 (Costo)

        # Nombre en cabecera de la tabla
        ite_id = QTableWidgetItem("ID")
        self.tab_parking.setHorizontalHeaderItem(0, ite_id)
        ite_usuario = QTableWidgetItem("Usuario")
        self.tab_parking.setHorizontalHeaderItem(1, ite_usuario)
        ite_matricula = QTableWidgetItem("Matricula")
        self.tab_parking.setHorizontalHeaderItem(2, ite_matricula)
        ite_f_entrada = QTableWidgetItem("Fecha entrada")
        self.tab_parking.setHorizontalHeaderItem(3, ite_f_entrada)
        ite_h_entrada = QTableWidgetItem("Hora de entrada")
        self.tab_parking.setHorizontalHeaderItem(4, ite_h_entrada)
        ite_f_salida = QTableWidgetItem("Fecha salida")
        self.tab_parking.setHorizontalHeaderItem(5, ite_f_salida)
        ite_h_salida = QTableWidgetItem("Hora salida")
        self.tab_parking.setHorizontalHeaderItem(6, ite_h_salida)
        ite_tiempo = QTableWidgetItem("Tiempo")
        self.tab_parking.setHorizontalHeaderItem(7, ite_tiempo)
        ite_costo = QTableWidgetItem("Costo")
        self.tab_parking.setHorizontalHeaderItem(8, ite_costo)

        self.but_ok = QPushButton(self)
        self.but_ok.setText("Aceptar")
        self.but_ok.setGeometry(QRect(580, 520, 100, 25))

        self.but_filter = QPushButton(self)
        self.but_filter.setText(" Filtrar")
        self.but_filter.setGeometry(QRect(210, 20, 100, 25))

        self.but_buscar2 = QPushButton(self)
        self.but_buscar2.setText(" Buscar")
        self.but_buscar2.setGeometry(QRect(620, 20, 100, 25))

        self.lab_t_recaudado = QLabel(self)
        self.lab_t_recaudado.setText("Total recaudado: ")
        self.lab_t_recaudado.setGeometry(QRect(50, 520, 150, 25))
        self.text_t_recaudado = QLineEdit(self)
        self.text_t_recaudado.setGeometry(QRect(150, 520, 200, 25))
        self.text_t_recaudado.setReadOnly(True)

        self.lab_fecha = QLabel(self)
        self.lab_fecha.setText("Fecha: ")
        self.lab_fecha.setGeometry(QRect(50, 20, 150, 25))

        self.date_input = QDateEdit(QDate.currentDate(), self, calendarPopup=True)
        self.date_input.setDisplayFormat("yyyy/MM/dd")
        self.date_input.setGeometry(QRect(90, 20, 100, 25))
        self.date_input.setMinimumDate(QDate.currentDate().addDays(-365))
        self.date_input.setMaximumDate(QDate.currentDate().addDays(365))
        

        self.lab_matricula = QLabel(self)
        self.lab_matricula.setText("Matricula: ")
        self.lab_matricula.setGeometry(QRect(450, 20, 150, 25))

        matricula = QRegExp("^[A-Z0-9]{3}-[A-Z0-9]{3}$")
        self.text_matricula = QLineEdit(self)
        self.text_matricula.setGeometry(QRect(500, 20, 100, 25))
        self.text_matricula.setValidator(QtGui.QRegExpValidator(matricula))

    def __launch_events(self):
        self.but_filter.clicked.connect(self.__report_vehicle_date)
        self.but_buscar2.clicked.connect(self.__report_vehicle_tuition)
        self.but_ok.clicked.connect(self.__ok)

    def __report_vehicle_date(self):
        self.tab_parking.setRowCount(0)
        date = self.date_input.date().toString("dd-MM-yyyy")
        self.text_t_recaudado.setText("")
        list = self.__vector_parking_log.list_report_service_date(date)
        if list.size() > 0:
            cost_total = 0
            i = list.front()
            while i != None:
                id = i.value.get_id()
                user = i.value.get_user()
                tuition = i.value.get_tuition()
                date_input = i.value.get_date_input()
                time_input = i.value.get_time_input()

                if  i.value.is_service() is False:
                    date_output = i.value.get_date_output()
                    time_output = i.value.get_time_output()
                    time = i.value.get_time()
                    cost = i.value.get_cost()
                    cost_total += cost
                else:
                    date_output = " -- -- --"
                    time_output = " --:-- "
                    time = ""
                    cost = ""

                ite_id = QTableWidgetItem(str(id))
                ite_user = QTableWidgetItem(str(user))
                ite_tuition = QTableWidgetItem(str(tuition))
                ite_date_input = QTableWidgetItem(str(date_input))
                ite_time_input = QTableWidgetItem(str(time_input))
                ite_date_output = QTableWidgetItem(str(date_output))
                ite_time_output = QTableWidgetItem(str(time_output))
                ite_time = QTableWidgetItem(str(time))
                ite_cost = QTableWidgetItem(str(cost))

                self.tab_parking.insertRow(self.tab_parking.rowCount())
                self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 0, ite_id)
                self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 1, ite_user)
                self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 2, ite_tuition)
                self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 3, ite_date_input)
                self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 4, ite_time_input)
                self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 5, ite_date_output)
                self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 6, ite_time_output)
                self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 7, ite_time)
                self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 8, ite_cost)
        
                i = i.next

            self.text_t_recaudado.setText(str(cost_total))

    def __report_vehicle_tuition(self):
        self.tab_parking.setRowCount(0)
        self.text_t_recaudado.setText("")
        tuition = self.text_matricula.text()
        vehicle = self.__vector_parking_log.list_report_service_tuition(tuition)
        if vehicle is not None:

            id = vehicle.get_id()
            user = vehicle.get_user()
            tuition = vehicle.get_tuition()
            date_input = vehicle.get_date_input()
            time_input = vehicle.get_time_input()

            if  vehicle.is_service() is False:
                date_output = vehicle.get_date_output()
                time_output = vehicle.get_time_output()
                time = vehicle.get_time()
                cost = vehicle.get_cost()
                self.text_t_recaudado.setText(str(cost))
            else:
                date_output = " -- -- --"
                time_output = " --:-- "
                time = ""
                cost = ""


            ite_id = QTableWidgetItem(str(id))
            ite_user = QTableWidgetItem(str(user))
            ite_tuition = QTableWidgetItem(str(tuition))
            ite_date_input = QTableWidgetItem(str(date_input))
            ite_time_input = QTableWidgetItem(str(time_input))
            ite_date_output = QTableWidgetItem(str(date_output))
            ite_time_output = QTableWidgetItem(str(time_output))
            ite_time = QTableWidgetItem(str(time))
            ite_cost = QTableWidgetItem(str(cost))

            self.tab_parking.insertRow(self.tab_parking.rowCount())
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 0, ite_id)
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 1, ite_user)
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 2, ite_tuition)
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 3, ite_date_input)
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 4, ite_time_input)
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 5, ite_date_output)
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 6, ite_time_output)
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 7, ite_time)
            self.tab_parking.setItem(self.tab_parking.rowCount() - 1, 8, ite_cost)

    def __ok(self):
        self.setVisible(False)

    def ini_window(self):
        self.tab_parking.setRowCount(0)
        self.text_matricula.setText("")

