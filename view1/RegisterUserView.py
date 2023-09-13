import re
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, QRect, QRegExp, Qt
from PyQt5.QtWidgets import *
from classes.User import User
from component.StyleWidget import StyleWidget
from controller.ListUser import ListUser


class RegisterUserView(QDialog):
    __vector_pccs = ListUser()

    def __init__(self, list_pccs):
        super().__init__()
        self.__vector_pccs = list_pccs
        self.__styleWidget = StyleWidget()


        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Registrar usuario")
        self.resize(300, 200)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("#13293d")

        formLayout = QFormLayout()
        hBoxLayout = QHBoxLayout()
        vBoxLayout = QVBoxLayout()
        gridLayout1 = QGridLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(vBoxLayout)

        formLayout.setFormAlignment
        formLayout.setLabelAlignment(Qt.AlignRight)
        vBoxLayout.setAlignment(Qt.AlignVCenter)
        vBoxLayout.setSpacing(10)

        hBoxLayout.setAlignment(Qt.AlignHCenter)

        self.tex_id = QLineEdit(self)
        self.tex_name = QLineEdit(self)
        self.tex_address = QLineEdit(self)
        self.tex_phone = QLineEdit(self)
        self.tex_mail = QLineEdit(self)

        self.tex_id.setValidator(QtGui.QRegExpValidator(QRegExp("[0-9]{1,10}"), self))
        self.tex_phone.setValidator(QtGui.QRegExpValidator(QRegExp("[0-9]{1,10}"), self))
        self.tex_name.setValidator(QtGui.QRegExpValidator(QRegExp("^[a-zA-Z\s]*$"), self))
        self.tex_mail.setValidator(QtGui.QRegExpValidator(QRegExp("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"+ "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$"), self))

        formLayout.addRow(str("&Identificación: "), self.tex_id)
        formLayout.addRow(str("&Nombre: "), self.tex_name)
        formLayout.addRow(str("&Dirección: "), self.tex_address)
        formLayout.addRow(str("&Teléfono: "), self.tex_phone)
        formLayout.addRow(str("&Email: "), self.tex_mail)

        self.but_save = QPushButton(self)
        self.but_save.setText("Guardar")
        self.but_save.setObjectName("save")
        style += self.__styleWidget.styleButton("save", "orange", "#13293d", "Arial", 12, "bold", 7)
        hBoxLayout.addWidget(self.but_save)

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setObjectName("cancel")
        style += self.__styleWidget.styleButton("cancel", "red", "white", "Arial", 12, "bold", 7)
        hBoxLayout.addWidget(self.but_cancel)

        gridLayout1.addLayout(hBoxLayout,0,0)

        vBoxLayout.addLayout(formLayout)
        vBoxLayout.addLayout(gridLayout1)

        self.setLayout(vBoxLayout)

        self.setStyleSheet(
            """QLineEdit{ 
                border-radius: 7px; 
                border: 2px solid orange;
                font-size: 14;
            }
            QLabel {
                color: orange;
                font-family: "Arial";
                font-size: 14px; }
                QLabel:hover {
                color: #4e91cd;
            }""" + str(style)
        )

    def __launch_Events(self):
        self.but_save.clicked.connect(self.__save_user)
        self.but_cancel.clicked.connect(self.__cancel)

    def __save_user(self):
        msj = self.__validate()
        if msj == "":
            user = User()
            user.set_id(self.tex_id.text())
            user.set_name(self.tex_name.text())
            user.set_address(self.tex_address.text())
            user.set_phone(self.tex_phone.text())
            user.set_mail(self.tex_mail.text())
            self.__vector_pccs.add_user(user)
            self.setVisible(False)

            QMessageBox.information(self,"Gestor EPS","Usuario Agregado correctamente",QMessageBox.Ok,)
        else:
            QMessageBox.information(self,"Gestor EPS",msj,QMessageBox.Ok,)

        
    def __cancel(self):
        self.setVisible(False)


    def initWindow(self):
        self.tex_address.setText("")
        self.tex_name.setText("")
        self.tex_id.setText("")
        self.tex_phone.setText("")
        self.tex_mail.setText("")

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
        



