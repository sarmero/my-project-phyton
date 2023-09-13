from PyQt5.QtCore import QDate, QRect, QSize, Qt
from PyQt5.QtGui import QColor, QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QDateTimeEdit, QDialog, QAction, QColorDialog, QComboBox, QLabel, QLineEdit, QMainWindow, QMessageBox, QPlainTextEdit, QPushButton, QStyle, QTableWidget, QTableWidgetItem, QToolBar

from controller.ListEquipment import ListEquipment


class RegisterReparationsView(QDialog):

    def __init__(self, vector_equipment, vector_maintenance):
        super().__init__()  # Constructor de la clase padre
        self.__vector_equipment = vector_equipment
        self.__vector_maintenance = vector_maintenance
        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Reparaciones")
        self.setFixedSize(558, 590)
        # Activar una ventana modal(no funciona la principal hasta que termine la secundaria)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        # Quita el botón de ayuda de la ventana
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Crear una etiqueta y asociarla a la ventana
        self.lab_info_equipment = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_info_equipment.setText("Información del equipo:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_info_equipment.setGeometry(QRect(20, 10, 150, 25))

        # Crea una tabla y la asocia a la ventana
        self.tab_info_equipment = QTableWidget(self)
        # Ubicar tabla en la ventana (x,y,ancho,largo)
        self.tab_info_equipment.setGeometry(QRect(20, 40, 510, 80))
        # Agregar filas y columnas a la tabla
        self.tab_info_equipment.setColumnCount(5)
        self.tab_info_equipment.setRowCount(0)
        # Agregar ancho a las columnas (indice, ancho)
        self.tab_info_equipment.setColumnWidth(0, 80)  # columna 1 (marca)
        self.tab_info_equipment.setColumnWidth(1, 80)  # columna 2 (modelo)
        self.tab_info_equipment.setColumnWidth(
            2, 200)  # columna 2 (descripción)
        self.tab_info_equipment.setColumnWidth(
            3, 90)  # columna 2 (propietario)
        self.tab_info_equipment.setColumnWidth(4, 90)  # columna 2 (teléfono)
        # Nombre en cabecera de la tabla

        ite_mark = QTableWidgetItem("Marca")
        self.tab_info_equipment.setHorizontalHeaderItem(0, ite_mark)
        ite_model = QTableWidgetItem("Modelo")
        self.tab_info_equipment.setHorizontalHeaderItem(1, ite_model)
        ite_description = QTableWidgetItem("Descripción")
        self.tab_info_equipment.setHorizontalHeaderItem(2, ite_description)
        ite_owner = QTableWidgetItem("Propietario")
        self.tab_info_equipment.setHorizontalHeaderItem(3, ite_owner)
        ite_phone = QTableWidgetItem("Teléfono")
        self.tab_info_equipment.setHorizontalHeaderItem(4, ite_phone)

        # Crear una etiqueta y asociarla a la ventana
        self.lab_info_equipment = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_info_equipment.setText("Información del mantenimiento:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_info_equipment.setGeometry(QRect(20, 134, 150, 25))

        # Crea una tabla y la asocia a la ventana
        self.tab_info_maintenance = QTableWidget(self)
        # Ubicar tabla en la ventana (x,y,ancho,largo)
        self.tab_info_maintenance.setGeometry(QRect(20, 170, 510, 70))
        # Agregar filas y columnas a la tabla
        self.tab_info_maintenance.setColumnCount(3)
        self.tab_info_maintenance.setRowCount(0)
        # Agregar ancho a las columnas (indice, ancho)
        self.tab_info_maintenance.setColumnWidth(0, 135)  # columna 1 (código)
        self.tab_info_maintenance.setColumnWidth(1, 120)  # columna 2 (fecha)
        self.tab_info_maintenance.setColumnWidth(
            2, 220)  # columna 2 (descripción)
        # Nombre en cabecera de la tabla

        ite_code_maintenance = QTableWidgetItem("Código mantenimiento")
        self.tab_info_maintenance.setHorizontalHeaderItem(
            0, ite_code_maintenance)
        ite_date_input = QTableWidgetItem("Fecha entrada")
        self.tab_info_maintenance.setHorizontalHeaderItem(1, ite_date_input)
        ite_description = QTableWidgetItem("Descripción")
        self.tab_info_maintenance.setHorizontalHeaderItem(2, ite_description)

        # Crear una etiqueta y asociarla a la ventana
        self.lab_info_equipment = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_info_equipment.setText("Información de la reparación:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_info_equipment.setGeometry(QRect(20, 248, 150, 25))

        self.lab_data_time = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_data_time.setText("Fecha de reparación:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_data_time.setGeometry(QRect(20, 280, 150, 25))

        self.date_input = QDateTimeEdit(
            QDate.currentDate(), self, calendarPopup=True)
        self.date_input.setGeometry(QRect(20, 305, 150, 25))
        self.date_input.setMinimumDate(QDate.currentDate().addDays(-365))
        self.date_input.setMaximumDate(QDate.currentDate().addDays(365))
        self.date_input.setDisplayFormat("yyyy-MM-dd hh:mm:ss")

        self.lab_diagnostic = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_diagnostic.setText("Descripción de diagnostico:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_diagnostic.setGeometry(QRect(20, 335, 200, 25))
        self.text_area_diagnostic = QPlainTextEdit(self)
        self.text_area_diagnostic.insertPlainText("")
        self.text_area_diagnostic.move(20, 360)
        self.text_area_diagnostic.resize(510, 50)

        self.lab_solution = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_solution.setText("Solución:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_solution.setGeometry(QRect(20, 410, 100, 25))
        self.text_area_solution = QPlainTextEdit(self)
        self.text_area_solution.insertPlainText("")
        self.text_area_solution.move(20, 430)
        self.text_area_solution.resize(510, 50)

        self.lab_cost = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_cost.setText("Costo:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_cost.setGeometry(QRect(20, 500, 90, 25))

        self.text_cost = QLineEdit(self)
        # Ubicar en la ventana (x,y,ancho,largo)
        self.text_cost.setGeometry(QRect(80, 500, 50, 25))

        # Crear un botón y asociarlo a la ventana
        self.but_ok = QPushButton(self)
        # Colocar el texto al botón
        self.but_ok.setText("Aceptar")
        # Ubicar en la ventana(x,y,ancho,largo)
        self.but_ok.setGeometry(QRect(320, 530, 100, 30))
        # Crear un botón y asociarlo a la ventana
        self.but_cancel = QPushButton(self)
        # Colocar el texto al botón
        self.but_cancel.setText("Cancelar")
        # Ubicar en la ventana(x,y,ancho,largo)
        self.but_cancel.setGeometry(QRect(430, 530, 100, 30))

    def __launch_events(self):
        pass

    def __load_equipment(self):

        if self.equipment != None:
            self.tab_info_equipment.setRowCount(0)
        self.equipment = self.__vector_equipment.get_equipment()
        i = self.equipment.front()
        while i != None:
            ite_mark = QTableWidgetItem(str(i.value.mark))
            ite_model = QTableWidgetItem(str(i.value.model))
            ite_description = QTableWidgetItem(str(i.value.description))
            ite_owner = QTableWidgetItem(str(i.value.owner))
            ite_phone = QTableWidgetItem(str(i.value.phone))
            # Insertar fila al final de la tabla
            # rowcount() devuelve la cantidad de filas de la tabla
            self.tab_info_equipment.insertRow(
                self.tab_info_equipment.rowCount())
            # Colocar la celda de x en la fila insertada anteriormente (fila,columna,celda)
            self.tab_info_equipment.setItem(
                self.tab_info_equipment.rowCount()-1, 0, ite_mark)
            # Colocar la celda de x en la fila insertada anteriormente (fila,columna,celda)
            self.tab_info_equipment.setItem(
                self.tab_info_equipment.rowCount()-1, 1, ite_model)
            # Colocar la celda de x en la fila insertada anteriormente (fila,columna,celda)
            self.tab_info_equipment.setItem(
                self.tab_info_equipment.rowCount()-1, 2, ite_description)
            # Colocar la celda de x en la fila insertada anteriormente (fila,columna,celda)
            self.tab_info_equipment.setItem(
                self.tab_info_equipment.rowCount()-1, 3, ite_owner)
            # Colocar la celda de x en la fila insertada anteriormente (fila,columna,celda)
            self.tab_info_equipment.setItem(
                self.tab_info_equipment.rowCount()-1, 4, ite_phone)
            i = i.next

    def __data_maintenance(self):
        maintenance = self.__vector_equipment
        self.tab_info_maintenance.setRowCount(0)

        list = self.__vector_equipment.get_maintenance()

        i = list.front()
        while i != None:
            maintenance = i.value
            ite_code_maintenance = QTableWidgetItem(maintenance.code)
            ite_date_input = QTableWidgetItem(
                str(maintenance.mark))
            ite_description = QTableWidgetItem(
                str(maintenance.model))

            self.tab_info_maintenance.insertRow(
                self.tab_info_maintenance.rowCount())
            self.tab_info_maintenance.setItem(
                self.tab_info_maintenance.rowCount() - 1, 0, ite_code_maintenance)
            self.tab_info_maintenance.setItem(
                self.tab_info_maintenance.rowCount() - 1, 1, ite_date_input)
            self.tab_info_maintenance.setItem(
                self.tab_info_maintenance.rowCount() - 1, 2, ite_description)
            i = i.next

    # falta código e interfaz para visualizar reparaciones
