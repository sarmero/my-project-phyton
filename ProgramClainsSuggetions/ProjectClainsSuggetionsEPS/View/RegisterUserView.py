

from PyQt5.QtCore import QDate, QDateTime, QRect, Qt
from PyQt5.QtWidgets import QCalendarWidget, QComboBox, QDateTimeEdit, QDialog, QLabel, QLineEdit, QMessageBox, QPushButton

from classes.User import User


class RegisterUserView (QDialog):
    def __init__(self, vector_user):
        super().__init__()
        self.__vector_user = vector_user
        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Registrar usuario")
        self.setFixedSize(628, 365)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        # botones de la ventana
        self.but_acepte = QPushButton(self)
        self.but_cancel = QPushButton(self)

        self.but_acepte.setText("Guardar ")
        self.but_acepte.setGeometry(QRect(162, 286, 108, 30))
        self.but_cancel.setText("Cancelar ")
        self.but_cancel.setGeometry(QRect(333, 286, 108, 30))
        # cuadro de texto de la ventana
        self.tex_ide = QLineEdit(self)
        self.tex_name = QLineEdit(self)
        self.tex_email = QLineEdit(self)
        self.tex_cell = QLineEdit(self)
        self.tex_direction = QLineEdit(self)
        # Ubicar en la ventana
        self.tex_ide.setGeometry(QRect(162, 109, 100, 27))
        self.tex_name.setGeometry(QRect(162, 169, 100, 27))
        self.tex_email.setGeometry(QRect(162, 216, 100, 27))
        self.tex_cell.setGeometry(QRect(470, 52, 100, 27))
        self.tex_direction.setGeometry(QRect(470, 109, 100, 27))
        # Crear una etiqueta y asociar a la ventana
        self.lab_N_ide = QLabel(self)
        self.lab_ide = QLabel(self)
        self.lab_name = QLabel(self)
        self.lab_email = QLabel(self)
        self.lab_cell = QLabel(self)
        self.lab_direction = QLabel(self)
        self.lab_sex = QLabel(self)
        self.lab_date = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_N_ide.setText("N° Identificación:")
        self.lab_ide.setText("Identificación:")
        self.lab_name.setText("Nombre:")
        self.lab_email.setText("Email:")
        self.lab_cell.setText("Celular:")
        self.lab_direction.setText("Dirección:")
        self.lab_sex.setText("Genero:")
        self.lab_date.setText("Fecha de nacimiento:")

        self.lab_N_ide.setGeometry(QRect(28, 112, 79, 21))
        self.lab_ide.setGeometry(QRect(28, 52, 99, 21))
        self.lab_name.setGeometry(QRect(28, 172, 48, 21))
        self.lab_email.setGeometry(QRect(28, 216, 33, 21))
        self.lab_cell.setGeometry(QRect(356, 52, 42, 21))
        self.lab_direction.setGeometry(QRect(356, 112, 50, 21))
        self.lab_sex.setGeometry(QRect(356, 172, 47, 21))
        self.lab_date.setGeometry(QRect(356, 212, 127, 21))
        # combo box
        self.com_ide = QComboBox(self)
        self.com_sex = QComboBox(self)
        self.com_ide.setGeometry(QRect(162, 52, 100, 27))
        self.com_sex.setGeometry(QRect(470, 169, 100, 27))
        self.com_sex.addItems(["Masculino","Femenino"])
        self.com_ide.addItems(["Cédula","Tarjeta de identidad"])
        # date fecha
        self.dat_sex = QDateTimeEdit(self)
        self.dat_sex.setGeometry(QRect(470, 216, 123, 27))
        self.dat_sex.setDateTime(QDateTime.currentDateTime())
        self.dat_sex.setDisplayFormat('dd.MM.yyyy')
        # self.com_sex = QDate(self)

    def __launch_events(self):
        self.but_acepte.clicked.connect(self.__save_user)
        self.but_cancel.clicked.connect(self.__cancel)

    def __save_user(self):
        type_id = self.com_ide.currentText()
        id = self.tex_ide.text()
        name = self.tex_name.text()
        mail = self.tex_email.text()
        cell = self.tex_cell.text()
        address = self.tex_direction.text()
        gender = self.com_sex.currentText()
        date_birth = self.dat_sex.text()

        if id != "" and type_id != "" and name != "" and mail != "" and cell != "" and address != "" and gender != "" and date_birth  != "" :
            exists = self.__vector_user.search_id(id)
            if exists is False:
                user = User(type_id, id, name, mail, cell, address, gender,date_birth)
                self.__vector_user.add_user(user)
                self.setVisible(False)
                QMessageBox.information(self,"Registrar usuario","Usuario agregado",QMessageBox.Ok,)
            else:
                QMessageBox.information(self,"Registrar usuario","la identificación ya existe ya existe",QMessageBox.Ok,)
        else:
            QMessageBox.information(self,"Registrar usuario","Todas los item son obligatorios",QMessageBox.Ok,)
        

    def __cancel(self):
        self.setVisible(False)

    def init_window(self):
        pass
