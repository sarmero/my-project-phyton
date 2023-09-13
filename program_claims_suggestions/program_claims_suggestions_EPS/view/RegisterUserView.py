import re
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, QRect, QRegExp, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from classes.User import User
from component.StyleWidget import StyleWidget
from controller.ListUser import ListUser


class RegisterUserView(QDialog):
    __list_user = ListUser()

    def __init__(self, list_user):
        super().__init__()
        self.__list_user = list_user
        self.__styleWidget = StyleWidget("Comic Sans MS")


        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Registrarse")
        self.resize(500, 500)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("")

        canvas = QPixmap("images/fondo_reg_user.png")
        self.lab_background = QLabel(self)
        self.lab_background.setGeometry(QRect(0, 0, 500, 500))
        self.lab_background.setPixmap(canvas)

        canvas = QPixmap("images/icon_user.png")
        self.lab_icon_user = QLabel(self)
        self.lab_icon_user.setGeometry(QRect(200, 15, 100, 100))
        self.lab_icon_user.setPixmap(canvas)

        self.lab_title = QLabel(self)
        self.lab_title.setText("------- Crear nueva cuenta -------")
        self.lab_title.setGeometry(75, 118, 350, 30)
        self.lab_title.setObjectName("labelTitle")
        self.lab_title.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLabel("labelTitle", "#351C75", "blue", 17, "bold")

        self.lab_id = QLabel(self)
        self.lab_id.setText("Identificación:")
        self.lab_id.setGeometry(80, 150, 100, 25)
        self.lab_id.setObjectName("labelId")
        style += self.__styleWidget.styleLabel("labelId", "#351C75", "green", 13, "bold")

        self.tex_id = QLineEdit(self)
        self.tex_id.setGeometry(QRect(75, 170, 350, 25))
        self.tex_id.setObjectName("texId")
        self.tex_id.setValidator(QtGui.QRegExpValidator(QRegExp("[0-9]{1,10}"), self))
        style += self.__styleWidget.styleLine("texId", 12)

        self.lab_name = QLabel(self)
        self.lab_name.setText("Nombre:")
        self.lab_name.setObjectName("labelUser")
        self.lab_name.setGeometry(QRect(80, 200, 90, 25))
        style += self.__styleWidget.styleLabel("labelUser", "#351C75", "green", 13, "bold")

        self.tex_name = QLineEdit(self)
        self.tex_name.setGeometry(QRect(75, 220, 350, 25))
        self.tex_name.setObjectName("texName")
        self.tex_name.setValidator(QtGui.QRegExpValidator(QRegExp("^[a-zA-Z\s]*$"), self))
        style += self.__styleWidget.styleLine("texName",13)

        self.lab_address = QLabel(self)
        self.lab_address.setText("Dirección: ")
        self.lab_address.setObjectName("labelAddress")
        self.lab_address.setGeometry(QRect(80, 250, 90, 25))
        style += self.__styleWidget.styleLabel("labelAddress", "#351C75", "green", 13, "bold")

        self.tex_address = QLineEdit(self)
        self.tex_address.setGeometry(QRect(75, 270, 350, 25))
        self.tex_address.setObjectName("texAddress")
        style += self.__styleWidget.styleLine("texAddress", 13)

        self.lab_phone = QLabel(self)
        self.lab_phone.setText("Celular:")
        self.lab_phone.setObjectName("labelPhone")
        self.lab_phone.setGeometry(QRect(80, 300, 90, 25))
        style += self.__styleWidget.styleLabel("labelPhone", "#351C75", "green", 13, "bold")

        self.tex_phone = QLineEdit(self)
        self.tex_phone.setGeometry(QRect(75, 320, 350, 25))
        self.tex_phone.setObjectName("texPhone")
        self.tex_phone.setValidator(QtGui.QRegExpValidator(QRegExp("[0-9]{1,10}"), self))
        style += self.__styleWidget.styleLine("texPhone", 13)

        self.lab_mail = QLabel(self)
        self.lab_mail.setText("Email:")
        self.lab_mail.setObjectName("labelMail")
        self.lab_mail.setGeometry(QRect(80, 350, 90, 25))
        style += self.__styleWidget.styleLabel("labelMail", "#351C75", "green", 13, "bold")

        self.tex_mail = QLineEdit(self)
        self.tex_mail.setGeometry(QRect(75, 370, 350, 25))
        self.tex_mail.setObjectName("texMail")
        self.tex_mail.setValidator(QtGui.QRegExpValidator(QRegExp("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"+ "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$"), self))
        style += self.__styleWidget.styleLine("texMail", 13)

        self.chc = QCheckBox(self)
        self.chc.setGeometry(96, 406, 310, 25)
        self.chc.setText("Estoy de acuerdo con los términos y condiciones")
        self.chc.setObjectName("chc")
        style += self.__styleWidget.styleCheckBox("chc", 12,"#351C75")
        
        self.but_save = QPushButton(self)
        self.but_save.setText("Guardar")
        self.but_save.setGeometry(QRect(176, 445, 70, 30))
        self.but_save.setObjectName("save")
        style += self.__styleWidget.styleButton("save", "green", "white", 12, "bold", 7)

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(256, 445, 70, 30))
        self.but_cancel.setObjectName("cancel")
        style += self.__styleWidget.styleButton("cancel", "red", "white",  12, "bold", 7)

        self.setStyleSheet(str(style))

    def __launch_Events(self):
        self.but_save.clicked.connect(self.__save_user)
        self.but_cancel.clicked.connect(self.__cancel)
        self.chc.clicked.connect(self.__acepteTerms)

    def __acepteTerms(self):
        if self.chc.checkState() == 2:
            self.but_save.setEnabled(True)
        else:
            self.but_save.setEnabled(False)

    def __save_user(self):
        msj = self.__validate()
        if msj == "":
            if self.__list_user.validate_id(self.tex_id.text()) == False:
                user = User()
                user.set_id(self.tex_id.text())
                user.set_name(self.tex_name.text())
                user.set_address(self.tex_address.text())
                user.set_phone(self.tex_phone.text())
                user.set_mail(self.tex_mail.text())
                self.__list_user.add_object(user)

                QMessageBox.information(self,"Benavides EPS","Usuario agregado con éxito!",QMessageBox.Ok,)
                self.setVisible(False)
            else:
                QMessageBox.warning(self,"Benavides EPS","El usuario ya existe!",QMessageBox.Ok,)
        else:
            QMessageBox.warning(self,"Benavides EPS",msj,QMessageBox.Ok,)
        
    def __cancel(self):
        self.setVisible(False)


    def init_window(self):
        self.tex_address.clear()
        self.tex_name.clear()
        self.tex_id.clear()
        self.tex_phone.clear()
        self.tex_mail.clear()
        self.but_save.setEnabled(False)

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
        



