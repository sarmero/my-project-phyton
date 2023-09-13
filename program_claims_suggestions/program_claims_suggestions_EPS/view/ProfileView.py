import re
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QRegExp, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from classes.User import User
from component.StyleWidget import StyleWidget
from controller.ListSuggestion import ListSuggestion
from controller.ListUser import ListUser


class ProfileView(QDialog):

    __list_user = ListUser()

    def __init__(self, list_user):
        super().__init__()
        self.__list_user = list_user
        self.__styleWidget = StyleWidget("Comic Sans MS")

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Perfil de usuario")
        self.resize(740, 400)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("#159438")

        canvas = QPixmap("images/fondo_profile.png")
        self.lab_background = QLabel(self)
        self.lab_background.setGeometry(QRect(240, 0, 500, 400))
        self.lab_background.setPixmap(canvas)

        canvas = QPixmap("images/icon_user.png")
        self.lab_icon_user = QLabel(self)
        self.lab_icon_user.setGeometry(QRect(72, 50, 100, 100))
        self.lab_icon_user.setPixmap(canvas)

        self.lab_style = QLabel(self)
        self.lab_style.setText("---------------------")
        self.lab_style.setGeometry(48, 173, 144, 25)
        self.lab_style.setObjectName("labelStyle")
        self.lab_style.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLabel("labelStyle", "white", "blue", 13, "bold")

        message = str("...sinceramente, creo que eres "
                      +"\nuna de las razones por la cual "
                      +"\nnuestra EPS tiene tanto éxito... "
                      +"\n\nGracias por ser parte de esta \ncomunidad")

        self.lab_message = QLabel(self)
        self.lab_message.setText(message)
        self.lab_message.setGeometry(16, 203, 208, 118)
        self.lab_message.setObjectName("labelMessage")
        self.lab_message.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLabel("labelMessage", "white", "blue", 13, "bold")

        self.lab_style1 = QLabel(self)
        self.lab_style1.setText("---------------------")
        self.lab_style1.setGeometry(48, 321, 144, 25)
        self.lab_style1.setObjectName("labelStyle1")
        self.lab_style1.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLabel("labelStyle1", "white", "blue", 13, "bold")

        self.lab_search_id = QLabel(self)
        self.lab_search_id.setText("Identificación:")
        self.lab_search_id.setGeometry(342, 17, 92, 25)
        self.lab_search_id.setObjectName("labelIdSearch")
        style += self.__styleWidget.styleLabel("labelIdSearch", "white", "#4e91cd", 13, "bold")

        self.tex_search_id = QLineEdit(self)
        self.tex_search_id.setGeometry(QRect(438, 17, 127, 25))
        self.tex_search_id.setObjectName("texIdSearch")
        self.tex_search_id.setAlignment(Qt.AlignHCenter)
        self.tex_search_id.setValidator(QtGui.QRegExpValidator(QRegExp("[0-9]{1,10}"), self))
        style += self.__styleWidget.styleLine("texIdSearch", 12)

        self.but_search = QPushButton(self)
        self.but_search.setText("Buscar")
        self.but_search.setGeometry(QRect(583, 17, 65, 25))
        self.but_search.setObjectName("buttonSearch")
        style += self.__styleWidget.styleButton("buttonSearch", "#4e91cd", "white", 12, "bold", 12)

        self.lab_id = QLabel(self)
        self.lab_id.setText("Identificación:")
        self.lab_id.setGeometry(325, 75, 100, 25)
        self.lab_id.setObjectName("labelId")
        style += self.__styleWidget.styleLabel("labelId", "#351C75", "green", 13, "bold")

        self.tex_id = QLineEdit(self)
        self.tex_id.setGeometry(QRect(320, 97, 350, 25))
        self.tex_id.setObjectName("texId")
        self.tex_id.setReadOnly(True)
        self.tex_id.setValidator(QtGui.QRegExpValidator(QRegExp("[0-9]{1,10}"), self))
        style += self.__styleWidget.styleLine("texId", 12)

        self.lab_name = QLabel(self)
        self.lab_name.setText("Nombre:")
        self.lab_name.setObjectName("labelUser")
        self.lab_name.setGeometry(QRect(325, 125, 90, 25))
        style += self.__styleWidget.styleLabel("labelUser", "#351C75", "green", 13, "bold")

        self.tex_name = QLineEdit(self)
        self.tex_name.setGeometry(QRect(320, 145, 350, 25))
        self.tex_name.setObjectName("texName")
        self.tex_name.setValidator(QtGui.QRegExpValidator(QRegExp("^[a-zA-Z\s]*$"), self))
        style += self.__styleWidget.styleLine("texName",13)

        self.lab_address = QLabel(self)
        self.lab_address.setText("Dirección: ")
        self.lab_address.setObjectName("labelAddress")
        self.lab_address.setGeometry(QRect(325, 175, 90, 25))
        style += self.__styleWidget.styleLabel("labelAddress", "#351C75", "green", 13, "bold")

        self.tex_address = QLineEdit(self)
        self.tex_address.setGeometry(QRect(320, 195, 350, 25))
        self.tex_address.setObjectName("texAddress")
        style += self.__styleWidget.styleLine("texAddress", 13)

        self.lab_phone = QLabel(self)
        self.lab_phone.setText("Celular:")
        self.lab_phone.setObjectName("labelPhone")
        self.lab_phone.setGeometry(QRect(325, 225, 90, 25))
        style += self.__styleWidget.styleLabel("labelPhone", "#351C75", "green", 13, "bold")

        self.tex_phone = QLineEdit(self)
        self.tex_phone.setGeometry(QRect(320, 245, 350, 25))
        self.tex_phone.setObjectName("texPhone")
        self.tex_phone.setValidator(QtGui.QRegExpValidator(QRegExp("[0-9]{1,10}"), self))
        style += self.__styleWidget.styleLine("texPhone", 13)

        self.lab_mail = QLabel(self)
        self.lab_mail.setText("Email:")
        self.lab_mail.setObjectName("labelMail")
        self.lab_mail.setGeometry(QRect(325, 275, 90, 25))
        style += self.__styleWidget.styleLabel("labelMail", "#351C75", "green", 13, "bold")

        self.tex_mail = QLineEdit(self)
        self.tex_mail.setGeometry(QRect(320, 295, 350, 25))
        self.tex_mail.setObjectName("texMail")
        self.tex_mail.setValidator(QtGui.QRegExpValidator(QRegExp("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"+ "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$"), self))
        style += self.__styleWidget.styleLine("texMail", 13)
        
        self.but_update = QPushButton(self)
        self.but_update.setText("Actualizar")
        self.but_update.setGeometry(QRect(411, 348, 80, 30))
        self.but_update.setObjectName("save")
        style += self.__styleWidget.styleButton("save", "green", "white", 12, "bold", 7)

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(498, 348, 80, 30))
        self.but_cancel.setObjectName("cancel")
        style += self.__styleWidget.styleButton("cancel", "red", "white",  12, "bold", 7)

        self.setStyleSheet(str(style))

    def __launch_Events(self):
        self.but_search.clicked.connect(self. __show_data)
        self.but_update.clicked.connect(self. __update)
        self.but_cancel.clicked.connect(self. __cancel)

    def __show_data(self):
        if self.tex_search_id.text() != "":
            user = self.__list_user.search_by_id(self.tex_search_id.text())

            if user != None:
                self.tex_id.setText(user.get_id())
                self.tex_name.setText(user.get_name())
                self.tex_phone.setText(user.get_phone())
                self.tex_mail.setText(user.get_mail())
                self.tex_address.setText(user.get_address())
                self.but_update.setEnabled(True)
            else:
                QMessageBox.warning(self,"Benavides EPS","Usuario no registrado ",QMessageBox.Ok,)
                self.init_window()
        else:
            QMessageBox.critical(self,"Benavides EPS","Error de identificación",QMessageBox.Ok,)

    def init_window(self):
        self.tex_name.clear()
        self.tex_phone.clear()
        self.tex_mail.clear()
        self.tex_address.clear()
        self.tex_id.clear()
        self.tex_search_id.clear()
        self.but_update.setEnabled(False)

    def __cancel(self):
        self.setVisible(False)
        
    def __update(self):
        msj = self.__validate()
        if msj == "":
            user = User()
            user.set_id(self.tex_id.text())
            user.set_name(self.tex_name.text())
            user.set_address(self.tex_address.text())
            user.set_phone(self.tex_phone.text())
            user.set_mail(self.tex_mail.text())
            self.__list_user.update_user(user)
            self.setVisible(False)

            QMessageBox.information(self,"Benavides EPS","Usuario Actualizado con  éxito!",QMessageBox.Ok,)
        else:
            QMessageBox.information(self,"Benavides EPS",msj,QMessageBox.Ok,)

    def __validate(self):
        tex:str
        mail = re.compile("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"+ "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$")
        
        if self.tex_id.text() == "":
            return "Por favor escriba una identificación"
        
        elif self.tex_name.text() == "":
            return "Por favor escriba un nombre"
        
        elif self.tex_address.text() == "":
            return "Por favor escriba una dirección"
        
        elif self.tex_phone.text() == "":
            return "Por favor escriba un teléfono"
        
        elif self.tex_mail.text() == "":
            return "Por favor escriba una dirección de correo"
        
        elif mail.search(self.tex_mail.text()) == None:
            return "Por favor escriba una dirección de correo valida"
        
        elif len( self.tex_phone.text())<10: 
            return "Por favor escriba un teléfono valido"
        
        else:
            return ""
        