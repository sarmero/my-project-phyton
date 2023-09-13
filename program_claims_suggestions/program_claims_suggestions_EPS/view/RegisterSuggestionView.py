import datetime
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QRegExp, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QComboBox,
    QDialog,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
)
from classes.Suggestion import Suggestion
from classes.User import User
from component.StyleWidget import StyleWidget

from controller.ListSuggestion import ListSuggestion


class RegisterSuggestionView(QDialog):
    __list_suggestion = ListSuggestion()

    def __init__(self, list_suggestion, list_users):
        super().__init__()
        self.__list_suggestion = list_suggestion
        self.__list_users = list_users
        self.code =""
        self.__styleWidget = StyleWidget("Comic Sans MS")

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Realizar sugestión")
        self.setFixedSize(600, 475)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("green")

        canvas = QPixmap("images/fondo_reg_sug.png")
        self.lab_background = QLabel(self)
        self.lab_background.setGeometry(QRect(0, 0, 600, 475))
        self.lab_background.setPixmap(canvas)

        self.lab_id = QLabel(self)
        self.lab_id.setText("Identificación:")
        self.lab_id.setGeometry(135, 18, 92, 25)
        self.lab_id.setObjectName("labelId")
        style += self.__styleWidget.styleLabel("labelId", "white", "#4e91cd", 13, "bold")

        self.tex_id = QLineEdit(self)
        self.tex_id.setGeometry(QRect(231, 18, 127, 25))
        self.tex_id.setObjectName("texId")
        self.tex_id.setAlignment(Qt.AlignHCenter)
        self.tex_id.setValidator(QtGui.QRegExpValidator(QRegExp("[0-9]{1,10}"), self))
        style += self.__styleWidget.styleLine("texId", 12)

        self.but_search = QPushButton(self)
        self.but_search.setText("Buscar")
        self.but_search.setGeometry(QRect(365, 18, 65, 25))
        self.but_search.setObjectName("buttonSearch")
        style += self.__styleWidget.styleButton("buttonSearch", "#4e91cd", "white", 12, "bold", 12)

        self.lab_name = QLabel(self)
        self.lab_name.setText("Nombre:")
        self.lab_name.setObjectName("labelUser")
        self.lab_name.setGeometry(QRect(30, 58, 70, 25))
        style += self.__styleWidget.styleLabel("labelUser", "#351C75", "green", 13, "bold")

        self.tex_name = QLineEdit(self)
        self.tex_name.setGeometry(QRect(25, 80, 300, 25))
        self.tex_name.setObjectName("texName")
        self.tex_name.setReadOnly(True)
        self.tex_name.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texName",13)

        self.lab_phone = QLabel(self)
        self.lab_phone.setText("Celular:")
        self.lab_phone.setObjectName("labelPhone")
        self.lab_phone.setGeometry(QRect(347, 58, 70, 25))
        style += self.__styleWidget.styleLabel("labelPhone", "white", "blue", 13, "bold")

        self.tex_phone = QLineEdit(self)
        self.tex_phone.setGeometry(QRect(342, 80, 231, 25))
        self.tex_phone.setObjectName("texPhone")
        self.tex_phone.setReadOnly(True)
        self.tex_phone.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texPhone", 13)

        self.lab_mail = QLabel(self)
        self.lab_mail.setText("Email: ")
        self.lab_mail.setObjectName("labelMail")
        self.lab_mail.setGeometry(QRect(30, 113, 70, 25))
        style += self.__styleWidget.styleLabel("labelMail", "#351C75", "green", 13, "bold")

        self.tex_mail = QLineEdit(self)
        self.tex_mail.setGeometry(QRect(25, 135, 300, 25))
        self.tex_mail.setObjectName("texMail")
        self.tex_mail.setReadOnly(True)
        self.tex_mail.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texMail", 13)

        self.lab_address = QLabel(self)
        self.lab_address.setText("Dirección: ")
        self.lab_address.setObjectName("labelAddress")
        self.lab_address.setGeometry(QRect(347, 113, 70, 25))
        style += self.__styleWidget.styleLabel("labelAddress", "white", "blue", 13, "bold")

        self.tex_address = QLineEdit(self)
        self.tex_address.setGeometry(QRect(342, 135, 231, 25))
        self.tex_address.setObjectName("texAddress")
        self.tex_address.setReadOnly(True)
        self.tex_address.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texAddress", 13)

        self.lab_title = QLabel(self)
        self.lab_title.setText("Realizar sugestión")
        self.lab_title.setObjectName("title")
        self.lab_title.setGeometry(QRect(210, 190, 179, 28))
        style += self.__styleWidget.styleLabel("title", "#351C75", "green", 18, "bold")

        self.lab_date = QLabel(self)
        self.lab_date.setText("Fecha:")
        self.lab_date.setObjectName("labelDate")
        self.lab_date.setGeometry(QRect(90, 234, 43, 25))
        style += self.__styleWidget.styleLabel("labelDate", "#351C75", "green", 13, "bold")

        self.tex_date = QLineEdit(self)
        self.tex_date.setGeometry(QRect(139, 234, 140, 25))
        self.tex_date.setObjectName("texDate")
        self.tex_date.setReadOnly(True)
        self.tex_date.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texDate", 13)

        self.lab_guy = QLabel(self)
        self.lab_guy.setText("Tipo:")
        self.lab_guy.setGeometry(313, 234, 35, 25)
        self.lab_guy.setObjectName("labelGuy")
        style += self.__styleWidget.styleLabel("labelGuy", "#351C75", "green",  13, "bold")

        self.com_guy = QComboBox(self)
        self.com_guy.setGeometry(QRect(348, 234, 150, 25))
        self.com_guy.setObjectName("com")
        self.com_guy.addItems(["Petición", "Queja", "Reclamo", "Sugerencia"])
        style += self.__styleWidget.styleLine("com",  13)

        self.lab_code = QLabel(self)
        self.lab_code.setText("Código: 200445")
        self.lab_code.setObjectName("labelCode")
        self.lab_code.setGeometry(QRect(458, 273, 150, 25))
        style += self.__styleWidget.styleLabel("labelCode", "white", "lightgreen", 13, "bold")

        self.lab_description = QLabel(self)
        self.lab_description.setText("Descripción")
        self.lab_description.setGeometry(QRect(30, 273, 75, 25))
        self.lab_description.setObjectName("labelDes")
        style += self.__styleWidget.styleLabel("labelDes", "#351C75", "green", 13, "bold")

        self.tex_area_description = QPlainTextEdit(self)
        self.tex_area_description.move(25, 296)
        self.tex_area_description.resize(547, 128)
        self.tex_area_description.setObjectName("texPlain")
        style += self.__styleWidget.styleTexPlain("texPlain", 12)

        self.but_send = QPushButton(self)
        self.but_send.setText("Enviar")
        self.but_send.setGeometry(QRect(214, 440, 80, 30))
        self.but_send.setObjectName("buttonSend")
        style += self.__styleWidget.styleButton("buttonSend", "green", "white",  13, "bold", 12)

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(306, 440, 80, 30))
        self.but_cancel.setObjectName("buttonCancel")
        style += self.__styleWidget.styleButton("buttonCancel", "red", "White", 13, "bold", 12)

        self.setStyleSheet(str(style))

    def __launch_Events(self):
        self.but_search.clicked.connect(self. __show_data)
        self.but_send.clicked.connect(self. __send)
        self.but_cancel.clicked.connect(self. __cancel)


    def __show_data(self):
        if self.tex_id.text() != "":
            user = self.__list_users.search_by_id(self.tex_id.text())

            if user != None:
                self.code = self.__list_suggestion.generate_code()
                self.tex_name.setText(user.get_name())
                self.tex_phone.setText(user.get_phone())
                self.tex_mail.setText(user.get_mail())
                self.tex_address.setText(user.get_address())
                self.lab_code.setText("Código: "+self.code)
                self.tex_area_description.setEnabled(True)
                self.com_guy.setEnabled(True)
                self.but_send.setEnabled(True)
            else:
                QMessageBox.warning(self,"Benavides EPS","Usuario no registrado ",QMessageBox.Ok,)
                self.init_window()
        else:
            QMessageBox.critical(self,"Benavides EPS","Error de identificación",QMessageBox.Ok,)

    def __send(self):
        if self.tex_area_description.toPlainText() != "":
            suggestion = Suggestion()
            suggestion.set_id_user(self.tex_id.text())
            suggestion.set_date(datetime.datetime.now().strftime('%d-%m-%Y'))
            suggestion.set_hour(datetime.datetime.now().strftime('%H:%M'))
            suggestion.set_code(self.code)
            suggestion.set_guy(self.com_guy.currentText())
            suggestion.set_description(self.tex_area_description.toPlainText())
            self.__list_suggestion.add_object(suggestion)
            QMessageBox.information(self,"Benavides EPS","Sugestión agregada con éxito!",QMessageBox.Ok,)
            self.setVisible(False)
        else:
            QMessageBox.warning(self,"Benavides EPS","Por favor redacte su sugestión",QMessageBox.Ok,)

    def __cancel(self):
        self.setVisible(False)

    def init_window(self):
        self.tex_name.clear()
        self.tex_phone.clear()
        self.tex_mail.clear()
        self.tex_address.clear()
        self.tex_id.clear()
        self.tex_area_description.clear()
        self.lab_code.setText("")
        self.tex_date.setText(datetime.datetime.now().strftime('%d-%m-%Y'))
        self.code = ""
        self.tex_area_description.setEnabled(False)
        self.com_guy.setEnabled(False)
        self.but_send.setEnabled(False)


