from PyQt5 import QtCore
from PyQt5.QtCore import QDate, QRect, Qt
from PyQt5.QtWidgets import QDateTimeEdit, QDialog, QComboBox, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QPushButton, QTableWidget, QTableWidgetItem
from classes.Maintenance import Maintenance


class RegisterMaintenanceView(QDialog):

    def __init__(self, vector_equipment, vector_maintenance):
        super().__init__()
        self.__vector_equipment = vector_equipment
        self.__vector_maintenance = vector_maintenance
        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Registrar mantenimiento")
        self.setFixedSize(558, 620)
        # Activar una ventana modal(no funciona la principal hasta que termine la secundaria)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        # Quita el botón de ayuda de la ventana
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Crear una etiqueta y asociarla a la ventana
        self.lab_code_equipment = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_code_equipment.setText("Código equipo:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_code_equipment.setGeometry(QRect(20, 10, 150, 25))
        # Crear una etiqueta y asociarla a la ventana
        self.com_code = QComboBox(self)
        # Ubicar en la ventana (x,y,ancho,largo)
        self.com_code.setGeometry(QRect(160, 10, 50, 25))

        # Crear una etiqueta y asociarla a la ventana
        self.lab_info = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_info.setText("Información del equipo")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_info.setGeometry(QRect(20, 40, 150, 25))

        # Crea una tabla y la asocia a la ventana
        self.tab_info_equipment = QTableWidget(self)
        # Ubicar tabla en la ventana (x,y,ancho,largo)
        self.tab_info_equipment.setGeometry(QRect(30, 70, 500, 150))
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
        self.lab_code_maintenance = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_code_maintenance.setText("Código mantenimiento:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_code_maintenance.setGeometry(QRect(20, 240, 150, 25))

        self.text_code_maintenance = QLineEdit(self)
        self.text_code_maintenance.setGeometry(QRect(160, 240, 90, 25))

        self.lab_date_input = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_date_input.setText("Fecha de entrada:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_date_input.setGeometry(QRect(20, 275, 150, 25))

        self.date_input = QDateTimeEdit(
            QDate.currentDate(), self, calendarPopup=True)
        self.date_input.setGeometry(QRect(160, 275, 150, 25))
        self.date_input.setMinimumDate(QDate.currentDate().addDays(-365))
        self.date_input.setMaximumDate(QDate.currentDate().addDays(365))
        self.date_input.setDisplayFormat("yyyy-MM-dd hh:mm:ss")

        self.lab_description_fail = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_description_fail.setText("Descripción falla:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_description_fail.setGeometry(QRect(20, 320, 150, 25))
        self.text_area_description_fail = QPlainTextEdit(self)
        self.text_area_description_fail.insertPlainText("")
        self.text_area_description_fail.move(160, 327)
        self.text_area_description_fail.resize(350, 200)

        # Crear un botón y asociarlo a la ventana
        self.but_ok = QPushButton(self)
        # Colocar el texto al botón
        self.but_ok.setText("Aceptar")
        # Ubicar en la ventana(x,y,ancho,largo)
        self.but_ok.setGeometry(QRect(170, 580, 100, 30))
        # Crear un botón y asociarlo a la ventana
        self.but_cancel = QPushButton(self)
        # Colocar el texto al botón
        self.but_cancel.setText("Cancelar")
        # Ubicar en la ventana(x,y,ancho,largo)
        self.but_cancel.setGeometry(QRect(290, 580, 100, 30))

    def __launch_events(self):
        self.com_code.currentTextChanged.connect(self.__load_equipment)
        self.but_ok.clicked.connect(self.__ok)  # Evento para botón ok

    def init_window(self):
        self.tab_info_equipment.setRowCount(0)
        self.text_area_description_fail.setPlainText("")
        self.text_code_maintenance.setText("")
        self.__init_combo()

    def __init_combo(self):
        # Limpiar el contenido del combo
        self.com_code.clear()
        # obtener el arreglo de polígonos
        list = self.__vector_equipment.get_equipment()
        # Ciclo para recorrer el arreglo de polígonos
        i = list.front()
        while i != None:
            equipment = i.value
            # adicionar item al combo
            self.com_code.addItem(equipment.code)
            i = i.next

    def __load_equipment(self):
        # Obtener el código del item seleccionado
        code = self.com_code.currentText()
        # Buscar el equipo usando el código
        self.equipment = self.__vector_equipment.search_by_code(code)

        if self.equipment != None:
            self.tab_info_equipment.setRowCount(0)
        self.equipment = self.__vector_equipment.get_equipment()
        i = self.equipment.back()
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

    def __ok(self):
        code_equipment = self.com_code.currentText()
        code = self.text_code_maintenance.text()
        date_input = self.date_input.dateTime()
        date_time_string = date_input.toString(self.date_input.displayFormat())
        description_fail = self.text_area_description_fail.toPlainText()

        maintenance = Maintenance(
            code, code_equipment,  date_time_string, description_fail)
        self.__vector_maintenance.add_maintenance(maintenance)
        QMessageBox.information(
            self, "Gestor de mantenimiento de equipos", "Mantenimiento registrado exitosamente", QMessageBox.Ok)

        self.setVisible(False)

    def __cancel(self):
        pass
