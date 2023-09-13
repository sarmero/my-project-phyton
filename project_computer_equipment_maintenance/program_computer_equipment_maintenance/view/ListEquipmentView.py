from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QTableWidget, QTableWidgetItem

from controller.ListEquipment import ListEquipment


class ListEquipmentView(QDialog):

    def __init__(self, vector_equipment):
        super().__init__()  # Constructor de la clase padre
        self.__vector_equipment = vector_equipment
        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Lista de equipos")
        self.setFixedSize(450, 400)
        # Activar una ventana modal(no funciona la principal hasta que termine la secundaria)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        # Quita el botón de ayuda de la ventana
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Crea una tabla y la asocia a la ventana
        self.tab_equipment = QTableWidget(self)
        # Ubicar tabla en la ventana (x,y,ancho,largo)
        self.tab_equipment.setGeometry(QRect(20, 20, 400, 280))
        # Agregar filas y columnas a la tabla
        self.tab_equipment.setColumnCount(4)
        self.tab_equipment.setRowCount(0)
        # Agregar ancho a las columnas (indice, ancho)
        self.tab_equipment.setColumnWidth(0, 90)  # columna 1 (código)
        self.tab_equipment.setColumnWidth(1, 90)  # columna 2 (marca)
        self.tab_equipment.setColumnWidth(2, 90)  # columna 3 (modelo)
        self.tab_equipment.setColumnWidth(3, 90)  # columna 4 (propietario)
        self.tab_equipment.setColumnWidth(4, 90)  # columna 5 (teléfono)
        # Nombre en cabecera de la tabla
        ite_code = QTableWidgetItem("Código")
        self.tab_equipment.setHorizontalHeaderItem(0, ite_code)
        ite_mark = QTableWidgetItem("Marca")
        self.tab_equipment.setHorizontalHeaderItem(1, ite_mark)
        ite_model = QTableWidgetItem("Modelo")
        self.tab_equipment.setHorizontalHeaderItem(2, ite_model)
        ite_owner = QTableWidgetItem("Propietario")
        self.tab_equipment.setHorizontalHeaderItem(3, ite_owner)
        ite_phone = QTableWidgetItem("Teléfono")
        self.tab_equipment.setHorizontalHeaderItem(4, ite_phone)

        # Crear un botón y asociarlo a la ventana
        self.but_ok = QPushButton(self)
        # Colocar el texto al botón

        self.but_ok.setText("Aceptar")
        # Ubicar en la ventana(x,y,ancho,largo)
        self.but_ok.setGeometry(QRect(180, 340, 100, 30))

    def __launch_events(self):
        self.but_ok.clicked.connect(self.__ok)  # Evento para botón ok

    def init_window(self):
        self.tab_equipment.setRowCount(0)
        self.equipment = self.__vector_equipment.get_equipment()
        i = self.equipment.front()
        while i != None:
            ite_code = QTableWidgetItem(str(i.value.code))
            ite_mark = QTableWidgetItem(str(i.value.mark))
            ite_model = QTableWidgetItem(str(i.value.model))
            ite_owner = QTableWidgetItem(str(i.value.owner))
            ite_phone = QTableWidgetItem(str(i.value.phone))
            # Insertar fila al final de la tabla
            # rowcount() devuelve la cantidad de filas de la tabla
            self.tab_equipment.insertRow(
                self.tab_equipment.rowCount())
            self.tab_equipment.setItem(
                self.tab_equipment.rowCount()-1, 0, ite_code)
            self.tab_equipment.setItem(
                self.tab_equipment.rowCount()-1, 1, ite_mark)
            self.tab_equipment.setItem(
                self.tab_equipment.rowCount()-1, 2, ite_model)
            self.tab_equipment.setItem(
                self.tab_equipment.rowCount()-1, 3, ite_owner)
            self.tab_equipment.setItem(
                self.tab_equipment.rowCount()-1, 4, ite_phone)
            i = i.next

    def __ok(self):  # Oculta la ventana
        self.setVisible(False)
