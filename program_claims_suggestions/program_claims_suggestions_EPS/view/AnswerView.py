from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QRegExp, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from classes.Suggestion import Suggestion
from component.StyleWidget import StyleWidget
from controller.ListSuggestion import ListSuggestion
from controller.ListUser import ListUser
from structures.List import List


class AnswerView(QDialog):
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
        self.setWindowTitle("Respuesta")
        self.resize(700, 550)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("#159438")

        canvas = QPixmap("images/fondo_answer.png")
        self.lab_background = QLabel(self)
        self.lab_background.setGeometry(QRect(0, 0, 700, 550))
        self.lab_background.setPixmap(canvas)

        self.lab_search_id = QLabel(self)
        self.lab_search_id.setText("Identificación:")
        self.lab_search_id.setGeometry(172, 18, 92, 25)
        self.lab_search_id.setObjectName("labelIdSearch")
        style += self.__styleWidget.styleLabel("labelIdSearch", "white", "#4e91cd", 13, "bold")

        self.tex_search_id = QLineEdit(self)
        self.tex_search_id.setGeometry(QRect(268, 18, 127, 25))
        self.tex_search_id.setObjectName("texIdSearch")
        self.tex_search_id.setAlignment(Qt.AlignHCenter)
        self.tex_search_id.setValidator(QtGui.QRegExpValidator(QRegExp("[0-9]{1,10}"), self))
        style += self.__styleWidget.styleLine("texIdSearch", 12)

        self.but_search = QPushButton(self)
        self.but_search.setText("Buscar")
        self.but_search.setGeometry(QRect(410, 18, 65, 25))
        self.but_search.setObjectName("buttonSearch")
        style += self.__styleWidget.styleButton("buttonSearch", "#4e91cd", "white", 12, "bold", 12)

        self.lab_name = QLabel(self)
        self.lab_name.setText("Nombre:")
        self.lab_name.setObjectName("labelUser")
        self.lab_name.setGeometry(QRect(30, 64, 60, 25))
        style += self.__styleWidget.styleLabel("labelUser", "#351C75", "green", 13, "bold")

        self.tex_name = QLineEdit(self)
        self.tex_name.setGeometry(QRect(95, 64, 340, 25))
        self.tex_name.setObjectName("texName")
        self.tex_name.setReadOnly(True)
        style += self.__styleWidget.styleLine("texName",13)

        self.lab_code = QLabel(self)
        self.lab_code.setText("Código:")
        self.lab_code.setObjectName("labelCode")
        self.lab_code.setGeometry(QRect(450, 64, 45, 25))
        style += self.__styleWidget.styleLabel("labelCode", "white", "blue", 13, "bold")

        self.com_code = QComboBox(self)
        self.com_code.setGeometry(QRect(500, 64, 170, 25))
        self.com_code.setObjectName("com")
        style += self.__styleWidget.styleLine("com",  13)

        self.lab_date = QLabel(self)
        self.lab_date.setText("Fecha:")
        self.lab_date.setObjectName("labelDate")
        self.lab_date.setGeometry(QRect(30, 120, 45, 25))
        style += self.__styleWidget.styleLabel("labelDate", "#351C75", "green", 13, "bold")

        self.tex_date = QLineEdit(self)
        self.tex_date.setGeometry(QRect(77, 120, 111, 25))
        self.tex_date.setObjectName("texDate")
        self.tex_date.setReadOnly(True)
        self.tex_date.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texDate", 13)

        self.lab_hour = QLabel(self)
        self.lab_hour.setText("Hora:")
        self.lab_hour.setObjectName("labelHour")
        self.lab_hour.setGeometry(QRect(210, 120, 35, 25))
        style += self.__styleWidget.styleLabel("labelHour", "#351C75", "green", 13, "bold")

        self.tex_hour = QLineEdit(self)
        self.tex_hour.setGeometry(QRect(247, 120, 80, 25))
        self.tex_hour.setObjectName("texHour")
        self.tex_hour.setReadOnly(True)
        self.tex_hour.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texHour", 13)

        self.lab_guy = QLabel(self)
        self.lab_guy.setText("Tipo:")
        self.lab_guy.setGeometry(353, 120, 35, 25)
        self.lab_guy.setObjectName("labelGuy")
        style += self.__styleWidget.styleLabel("labelGuy", "white", "#351C75",  13, "bold")

        self.tex_guy = QLineEdit(self)
        self.tex_guy.setGeometry(QRect(389, 120, 100, 25))
        self.tex_guy.setObjectName("texGuy")
        self.tex_guy.setReadOnly(True)
        self.tex_guy.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texGuy",  13)

        self.lab_state = QLabel(self)
        self.lab_state.setText("Estado:")
        self.lab_state.setGeometry(511, 120, 50, 25)
        self.lab_state.setObjectName("labelState")
        style += self.__styleWidget.styleLabel("labelState", "white", "#351C75",  13, "bold")

        self.tex_state = QLineEdit(self)
        self.tex_state.setGeometry(QRect(570, 120, 100, 25))
        self.tex_state.setObjectName("texState")
        self.tex_state.setReadOnly(True)
        self.tex_state.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texState",  13)

        self.lab_description = QLabel(self)
        self.lab_description.setText("Descripción")
        self.lab_description.setGeometry(QRect(35, 158, 75, 25))
        self.lab_description.setObjectName("labelDes")
        style += self.__styleWidget.styleLabel("labelDes", "#351C75", "green", 13, "bold")

        self.tex_area_description = QPlainTextEdit(self)
        self.tex_area_description.move(30, 180)
        self.tex_area_description.resize(640, 140)
        self.tex_area_description.setObjectName("texPlainDes")
        self.tex_area_description.setReadOnly(True)
        style += self.__styleWidget.styleTexPlain("texPlainDes", 12)

        self.lab_answer = QLabel(self)
        self.lab_answer.setText("Respuesta")
        self.lab_answer.setGeometry(QRect(35, 330, 75, 25))
        self.lab_answer.setObjectName("labelAns")
        style += self.__styleWidget.styleLabel("labelAns", "#351C75", "green", 13, "bold")

        self.tex_area_answer = QPlainTextEdit(self)
        self.tex_area_answer.move(30, 350)
        self.tex_area_answer.resize(640, 140)
        self.tex_area_answer.setObjectName("texPlain")
        self.tex_area_answer.setReadOnly(True)
        style += self.__styleWidget.styleTexPlain("texPlain", 12)

        self.but_acepte = QPushButton(self)
        self.but_acepte.setText("Aceptar")
        self.but_acepte.setGeometry(QRect(287, 506, 125, 30))
        self.but_acepte.setObjectName("buttonAcepte")
        style += self.__styleWidget.styleButton("buttonAcepte", "green", "white",  13, "bold", 12)

        self.setStyleSheet(str(style))

    def __launch_Events(self):
        self.but_search.clicked.connect(self. __show_data)
        self.but_acepte.clicked.connect(self. __ok)
        self.com_code.currentTextChanged.connect(self.__search_data)


    def __show_data(self):
        if self.tex_search_id.text() != "":
            list_code = self.__list_suggestion.search_list_code_by_id(self.tex_search_id.text())

            if list_code.size() > 0:
                user = self.__list_user.search_by_id(self.tex_search_id.text())
                self.tex_name.setText(user.get_name())
                self.com_code.setEnabled(True)
                self.com_code.clear()

                i = list_code.front()
                while i != None:
                    self.com_code.addItem(i.value)
                    i = i.next
            else:
                QMessageBox.warning(self,"Benavides EPS","No se encontraron registros ",QMessageBox.Ok,)
                self.init_window()
        else:
            QMessageBox.critical(self,"Benavides EPS","Error de identificación",QMessageBox.Ok,)

    def __search_data(self):
        if self.com_code.currentText() != "":
            suggestion = self.__list_suggestion.search_by_code(self.com_code.currentText())

            self.tex_date.setText(suggestion.get_date())
            self.tex_guy.setText(suggestion.get_guy())
            self.tex_state.setText("Revisado" if suggestion.get_state() == True else "Pendiente")
            self.tex_area_description.setPlainText(suggestion.get_description())
            self.tex_hour.setText(suggestion.get_hour())
            self.tex_area_answer.setPlainText(suggestion.get_answer())


    def __ok(self):
        self.setVisible(False)

    def init_window(self):
        self.com_code.setEnabled(False)
        self.com_code.clear()
        self.tex_name.clear()
        self.tex_area_description.clear()
        self.tex_area_answer.clear()
        self.tex_hour.clear()
        self.tex_state.clear()
        self.tex_date.clear()
        self.tex_guy.clear()

