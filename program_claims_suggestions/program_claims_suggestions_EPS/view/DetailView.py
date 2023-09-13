from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QRegExp, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from component.StyleWidget import StyleWidget
from controller.ListSuggestion import ListSuggestion
from controller.ListUser import ListUser


class DetailView(QDialog):
    __list_suggestion = ListSuggestion()
    __list_user = ListUser()

    def __init__(self, list_suggestion, list_user):
        super().__init__()
        self.__list_suggestion = list_suggestion
        self.__list_user = list_user
        self.__styleWidget = StyleWidget("Comic Sans MS")
        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Detalle de sugestiones")
        self.resize(802, 530)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("white")

        canvas = QPixmap("images/fondo_detail.png")
        self.lab_background = QLabel(self)
        self.lab_background.setGeometry(QRect(0, 0, 526, 530))
        self.lab_background.setPixmap(canvas)

        canvas = QPixmap("images/fondo_detail2.png")
        self.lab_background1 = QLabel(self)
        self.lab_background1.setGeometry(QRect(527, 0, 276, 530))
        self.lab_background1.setPixmap(canvas)

        self.lab_code = QLabel(self)
        self.lab_code.setText("Código:")
        self.lab_code.setObjectName("labelCode")
        self.lab_code.setGeometry(QRect(155, 30, 45, 25))
        style += self.__styleWidget.styleLabel("labelCode", "#351C75", "green", 13, "bold")

        self.tex_code = QLineEdit(self)
        self.tex_code.setGeometry(QRect(213, 30, 100, 25))
        self.tex_code.setObjectName("texCode")
        self.tex_code.setAlignment(Qt.AlignHCenter)
        self.tex_code.setValidator(QtGui.QRegExpValidator(QRegExp("[A-Z0-9]{1,10}"), self))
        style += self.__styleWidget.styleLine("texCode",13)

        self.but_search_code = QPushButton(self)
        self.but_search_code.setText("Buscar")
        self.but_search_code.setGeometry(QRect(320, 30, 65, 25))
        self.but_search_code.setObjectName("buttonSearch")
        style += self.__styleWidget.styleButton("buttonSearch", "#4e91cd", "lightgreen", 12, "bold", 12)

        self.lab_guy = QLabel(self)
        self.lab_guy.setText("Tipo:")
        self.lab_guy.setGeometry(27, 80, 35, 25)
        self.lab_guy.setObjectName("labelGuy")
        style += self.__styleWidget.styleLabel("labelGuy", "white", "#351C75",  13, "bold")

        self.tex_guy = QLineEdit(self)
        self.tex_guy.setGeometry(QRect(74, 80, 190, 25))
        self.tex_guy.setObjectName("texGuy")
        self.tex_guy.setReadOnly(True)
        self.tex_guy.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texGuy",  13)

        self.lab_state = QLabel(self)
        self.lab_state.setText("Estado:")
        self.lab_state.setGeometry(281, 80, 50, 25)
        self.lab_state.setObjectName("labelState")
        style += self.__styleWidget.styleLabel("labelState", "#351C75", "green",  13, "bold")

        self.tex_state = QLineEdit(self)
        self.tex_state.setGeometry(QRect(329, 80, 180, 25))
        self.tex_state.setObjectName("texState")
        self.tex_state.setReadOnly(True)
        self.tex_state.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texState",  13)

        self.lab_date = QLabel(self)
        self.lab_date.setText("Fecha:")
        self.lab_date.setObjectName("labelDate")
        self.lab_date.setGeometry(QRect(27, 112, 45, 25))
        style += self.__styleWidget.styleLabel("labelDate", "white", "#351C75", 13, "bold")

        self.tex_date = QLineEdit(self)
        self.tex_date.setGeometry(QRect(74, 112, 190, 25))
        self.tex_date.setObjectName("texDate")
        self.tex_date.setReadOnly(True)
        self.tex_date.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texDate", 13)

        self.lab_hour = QLabel(self)
        self.lab_hour.setText("Hora:")
        self.lab_hour.setObjectName("labelHour")
        self.lab_hour.setGeometry(QRect(280, 112, 35, 25))
        style += self.__styleWidget.styleLabel("labelHour","#351C75", "green", 13, "bold")

        self.tex_hour = QLineEdit(self)
        self.tex_hour.setGeometry(QRect(329, 112, 180, 25))
        self.tex_hour.setObjectName("texHour")
        self.tex_hour.setReadOnly(True)
        self.tex_hour.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texHour", 13)

        self.lab_description = QLabel(self)
        self.lab_description.setText("Descripción")
        self.lab_description.setGeometry(QRect(33, 155, 80, 25))
        self.lab_description.setObjectName("labelDes")
        style += self.__styleWidget.styleLabel("labelDes", "white", "#351C75", 13, "bold")

        self.tex_area_description = QPlainTextEdit(self)
        self.tex_area_description.move(27, 180)
        self.tex_area_description.resize(480, 125)
        self.tex_area_description.setObjectName("texPlainDes")
        self.tex_area_description.setReadOnly(True)
        style += self.__styleWidget.styleTexPlain("texPlainDes", 12)

        self.lab_answer = QLabel(self)
        self.lab_answer.setText("Respuesta")
        self.lab_answer.setGeometry(QRect(33, 315, 75, 25))
        self.lab_answer.setObjectName("labelAns")
        style += self.__styleWidget.styleLabel("labelAns", "white", "#351C75", 13, "bold")

        self.tex_area_answer = QPlainTextEdit(self)
        self.tex_area_answer.move(27, 340)
        self.tex_area_answer.resize(480, 135)
        self.tex_area_answer.setObjectName("texPlain")
        self.tex_area_answer.setReadOnly(True)
        style += self.__styleWidget.styleTexPlain("texPlain", 12)

        self.but_acepte = QPushButton(self)
        self.but_acepte.setText("Aceptar")
        self.but_acepte.setGeometry(QRect(230, 490, 80, 30))
        self.but_acepte.setObjectName("buttonAcepte")
        style += self.__styleWidget.styleButton("buttonAcepte", "green", "white",  13, "bold", 12)

        canvas = QPixmap("images/icon_user.png")
        self.lab_background2 = QLabel(self)
        self.lab_background2.setGeometry(QRect(615, 45, 96, 96))
        self.lab_background2.setPixmap(canvas)

        self.lab_title = QLabel(self)
        self.lab_title.setText("Información de usuario")
        self.lab_title.setObjectName("title")
        self.lab_title.setGeometry(QRect(593, 150, 180, 28))
        style += self.__styleWidget.styleLabel("title", "#351C75", "green", 13, "bold")

        canvas = QPixmap("images/icon_name.png")
        self.lab_icon_name = QLabel(self)
        self.lab_icon_name.setGeometry(QRect(538, 192, 32, 32))
        self.lab_icon_name.setPixmap(canvas)

        self.lab_name = QLabel(self)
        self.lab_name.setText("Nombre")
        self.lab_name.setObjectName("labelName")
        self.lab_name.setGeometry(QRect(578, 190, 90, 25))
        style += self.__styleWidget.styleLabel("labelName", "#351C75", "green", 13, "bold")

        self.lab_tex_name = QLabel(self)
        self.lab_tex_name.setGeometry(QRect(580, 210, 200, 25))
        self.lab_tex_name.setObjectName("texName")
        style += self.__styleWidget.styleLabel("texName", "green", "lightgreen", 13, "bold")

        canvas = QPixmap("images/icon_id.png")
        self.lab_icon_id = QLabel(self)
        self.lab_icon_id.setGeometry(QRect(541, 260, 32, 32))
        self.lab_icon_id.setPixmap(canvas)

        self.lab_id = QLabel(self)
        self.lab_id.setText("Identificación")
        self.lab_id.setGeometry(580, 255, 100, 25)
        self.lab_id.setObjectName("labelId")
        style += self.__styleWidget.styleLabel("labelId", "#351C75", "green", 13, "bold")

        self.lab_tex_id = QLabel(self)
        self.lab_tex_id.setGeometry(QRect(580, 276, 200, 25))
        self.lab_tex_id.setObjectName("texId")
        style += self.__styleWidget.styleLabel("texId", "green", "lightgreen", 13, "bold")

        canvas = QPixmap("images/icon_address.png")
        self.lab_icon_address = QLabel(self)
        self.lab_icon_address.setGeometry(QRect(541, 320, 32, 32))
        self.lab_icon_address.setPixmap(canvas)

        self.lab_address = QLabel(self)
        self.lab_address.setText("Dirección")
        self.lab_address.setObjectName("labelAddress")
        self.lab_address.setGeometry(QRect(580, 320, 90, 25))
        style += self.__styleWidget.styleLabel("labelAddress", "#351C75", "green", 13, "bold")

        self.lab_tex_address = QLabel(self)
        self.lab_tex_address.setGeometry(QRect(580, 340, 200, 25))
        self.lab_tex_address.setObjectName("texAddress")
        style += self.__styleWidget.styleLabel("texAddress", "green", "lightgreen", 13, "bold")

        canvas = QPixmap("images/icon_phone.png")
        self.lab_icon_phone = QLabel(self)
        self.lab_icon_phone.setGeometry(QRect(541, 389, 32, 32))
        self.lab_icon_phone.setPixmap(canvas)

        self.lab_phone = QLabel(self)
        self.lab_phone.setText("Celular")
        self.lab_phone.setObjectName("labelPhone")
        self.lab_phone.setGeometry(QRect(580, 385, 90, 25))
        style += self.__styleWidget.styleLabel("labelPhone", "#351C75", "green", 13, "bold")

        self.lab_tex_phone = QLabel(self)
        self.lab_tex_phone.setGeometry(QRect(580, 405, 200, 25))
        self.lab_tex_phone.setObjectName("texPhone")
        style += self.__styleWidget.styleLabel("texPhone", "green", "lightgreen", 13, "bold")

        canvas = QPixmap("images/icon_mail.png")
        self.lab_icon_mail = QLabel(self)
        self.lab_icon_mail.setGeometry(QRect(541, 454, 32, 32))
        self.lab_icon_mail.setPixmap(canvas)

        self.lab_mail = QLabel(self)
        self.lab_mail.setText("Email")
        self.lab_mail.setObjectName("labelMail")
        self.lab_mail.setGeometry(QRect(580, 450, 90, 25))
        style += self.__styleWidget.styleLabel("labelMail", "#351C75", "green", 13, "bold")

        self.lab_tex_mail = QLabel(self)
        self.lab_tex_mail.setGeometry(QRect(580, 470, 350, 25))
        self.lab_tex_mail.setObjectName("texMail")
        style += self.__styleWidget.styleLabel("texMail", "green", "lightgreen", 13, "bold")

        self.setStyleSheet(str(style))

    def __launch_Events(self):
        self.but_search_code.clicked.connect(self. __show_data)
        self.but_acepte.clicked.connect(self. __ok)

    def __show_data(self):
        if self.tex_code.text() != "":
            suggestion = self.__list_suggestion.search_by_code(self.tex_code.text())

            if suggestion != None:

                self.tex_guy.setText(suggestion.get_guy())
                self.tex_state.setText("Revisado" if suggestion.get_state() == True else "Pendiente")
                self.tex_date.setText(suggestion.get_date())
                self.tex_hour.setText(suggestion.get_hour())
                self.tex_area_description.setPlainText(suggestion.get_description())
                self.tex_area_answer.setPlainText(suggestion.get_answer())
                
                user = self.__list_user.search_by_id(suggestion.get_id_user())

                if user != None:
                    self.lab_tex_id.setText(user.get_id())
                    self.lab_tex_name.setText(user.get_name())
                    self.lab_tex_phone.setText(user.get_phone())
                    self.lab_tex_mail.setText(user.get_mail())
                    self.lab_tex_address.setText(user.get_address())

                    
            else:
                QMessageBox.warning(self,"Benavides EPS","Registro no encontrado",QMessageBox.Ok,)
                self.init_window()
        else:
            QMessageBox.critical(self,"Benavides EPS", "Por favor escriba un código",QMessageBox.Ok,)
    
    def __ok(self):
        self.setVisible(False)

    def set_data(self, code):
        self.tex_code.setText(code)
        self.tex_code.setReadOnly(True)
        self.but_search_code.setEnabled(False)
        self.__show_data()


    def init_window(self):
        self.lab_tex_address.clear()
        self.lab_tex_name.clear()
        self.lab_tex_id.clear()
        self.lab_tex_phone.clear()
        self.lab_tex_mail.clear()
        self.tex_state.clear()
        self.tex_guy.clear()
        self.tex_area_description.clear()
        self.tex_area_answer.clear()
        self.tex_date.clear()
        self.tex_hour.clear()
        self.tex_code.clear()
      
