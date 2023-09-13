from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QPlainTextEdit, QDialog, QLabel, QLineEdit, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem
from classes.Equipment import Equipment
from classes.Maintenance import Maintenance


from controller.ListEquipment import ListEquipment
from structures.List import List


class RegisterEquipmentView(QDialog):

    def __init__(self, vector_equipment):
        super().__init__()  # Constructor de la clase padre

        self.__vector_equipment = vector_equipment
        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Registrar equipos")
        self.setFixedSize(450, 479)
        # Activar una ventana modal(no funciona la principal hasta que termine la secundaria)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        # Quita el botón de ayuda de la ventana
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Crear una etiqueta y asociarla a la ventana
        self.lab_code = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_code.setText("Código:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_code.setGeometry(QRect(20, 10, 50, 25))
        # Crear una caja de texto y asociarla a la ventana
        self.text_code = QLineEdit(self)
        # Ubicar en la ventana (x,y,ancho,largo)
        self.text_code.setGeometry(QRect(80, 10, 100, 25))

        self.lab_mark = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_mark.setText("Marca:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_mark.setGeometry(QRect(20, 50, 50, 25))
        # Crear una caja de texto y asociarla a la ventana
        self.text_mark = QLineEdit(self)
        # Ubicar en la ventana (x,y,ancho,largo)
        self.text_mark.setGeometry(QRect(80, 50, 100, 25))

        self.lab_model = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_model.setText("Modelo:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_model.setGeometry(QRect(20, 90, 50, 25))
        # Crear una caja de texto y asociarla a la ventana
        self.text_model = QLineEdit(self)
        # Ubicar en la ventana (x,y,ancho,largo)
        self.text_model.setGeometry(QRect(80, 90, 100, 25))

        # Crear una etiqueta y asociarla a la ventana
        self.lab_description = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_description.setText("Descripción:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_description.setGeometry(QRect(20, 130, 70, 25))
        self.text_area_description = QPlainTextEdit(self)
        self.text_area_description.insertPlainText("")
        self.text_area_description.setPlaceholderText(
            "Escriba una descripción")
        self.text_area_description.move(20, 160)
        self.text_area_description.resize(400, 90)

        self.lab_owner = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_owner.setText("Propietario:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_owner.setGeometry(QRect(20, 270, 100, 25))
        # Crear una caja de texto y asociarla a la ventana
        self.text_owner = QLineEdit(self)
        # Ubicar en la ventana (x,y,ancho,largo)
        self.text_owner.setGeometry(QRect(80, 270, 120, 25))

        self.lab_phone = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_phone.setText("Teléfono:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_phone.setGeometry(QRect(20, 310, 100, 25))
        # Crear una caja de texto y asociarla a la ventana
        self.text_phone = QLineEdit(self)
        # Ubicar en la ventana (x,y,ancho,largo)
        self.text_phone.setGeometry(QRect(80, 310, 100, 25))

        self.lab_email = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_email.setText("Email:")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_email.setGeometry(QRect(20, 340, 90, 25))
        # Crear una caja de texto y asociarla a la ventana
        self.text_email = QLineEdit(self)
        # Ubicar en la ventana (x,y,ancho,largo)
        self.text_email.setGeometry(QRect(80, 340, 150, 25))

        # Crear un botón y asociarlo a la ventana
        self.but_ok = QPushButton(self)
        # Colocar el texto al botón
        self.but_ok.setText("Aceptar")
        # Ubicar en la ventana(x,y,ancho,largo)
        self.but_ok.setGeometry(QRect(120, 400, 100, 30))
        # Crear un botón y asociarlo a la ventana
        self.but_cancel = QPushButton(self)
        # Colocar el texto al botón
        self.but_cancel.setText("Cancelar")
        # Ubicar en la ventana(x,y,ancho,largo)
        self.but_cancel.setGeometry(QRect(240, 400, 100, 30))

    def __launch_events(self):
        self.but_cancel.clicked.connect(
            self.__cancel)  # Evento para botón cancel

        self.but_ok.clicked.connect(self.__ok)  # Evento para botón ok

    def init_window(self):
        self.text_code.setText("")
        self.text_email.setText("")
        self.text_mark.setText("")
        self.text_model.setText("")
        self.text_owner.setText("")
        self.text_phone.setText("")
        self.text_area_description.setPlainText("")

    def __ok(self):
        code = self.text_code.text()
        email = self.text_email.text()
        mark = self.text_mark.text()
        model = self.text_model.text()
        owner = self.text_owner.text()
        phone = self.text_phone.text()
        description = self.text_area_description.toPlainText()

        equipment = Equipment(
            code, mark, model, description, owner, phone, email)
        self.__vector_equipment.add_equipment(equipment)

        QMessageBox.information(
            self, "Gestor de mantenimiento de equipos", "Equipo registrado exitosamente", QMessageBox.Ok)

        self.setVisible(False)

    def __cancel(self):  # Oculta la ventana
        self.setVisible(False)
