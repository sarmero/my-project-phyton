import datetime
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from component.StyleWidget import StyleWidget
from controller.ListSuggestion import ListSuggestion
from controller.ListUser import ListUser


class ReplyView(QDialog):
    __list_suggestion = ListSuggestion()

    def __init__(self, list_suggestion):
        super().__init__()
        self.__list_suggestion = list_suggestion
        self.suggestion = None
        self.__styleWidget = StyleWidget("Comic Sans MS")

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Responder sugestión")
        self.resize(620, 375)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("white")

        canvas = QPixmap("images/fondo_reply1.png")
        self.lab_background = QLabel(self)
        self.lab_background.setGeometry(QRect(0, 0, 620, 375))
        self.lab_background.setPixmap(canvas)

        self.lab_search_code = QLabel(self)
        self.lab_search_code.setText("Código:")
        self.lab_search_code.setGeometry(25, 20, 45, 25)
        self.lab_search_code.setObjectName("labelCodeSearch")
        style += self.__styleWidget.styleLabel("labelCodeSearch", "white", "#4e91cd", 13, "bold")

        self.tex_code = QLineEdit(self)
        self.tex_code.setGeometry(QRect(78, 20, 118, 25))
        self.tex_code.setObjectName("texCode")
        self.tex_code.setReadOnly(True)
        style += self.__styleWidget.styleLine("texCode",13)

        self.lab_guy = QLabel(self)
        self.lab_guy.setText("Tipo:")
        self.lab_guy.setGeometry(230, 20, 35, 25)
        self.lab_guy.setObjectName("labelGuy")
        style += self.__styleWidget.styleLabel("labelGuy", "white", "#351C75",  13, "bold")

        self.tex_guy = QLineEdit(self)
        self.tex_guy.setGeometry(QRect(270, 20, 132, 25))
        self.tex_guy.setObjectName("texGuy")
        self.tex_guy.setReadOnly(True)
        self.tex_guy.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texGuy",  13)

        self.lab_date = QLabel(self)
        self.lab_date.setText("Fecha:")
        self.lab_date.setObjectName("labelDate")
        self.lab_date.setGeometry(QRect(440, 20, 45, 25))
        style += self.__styleWidget.styleLabel("labelDate", "white", "#351C75", 13, "bold")

        self.tex_date = QLineEdit(self)
        self.tex_date.setGeometry(QRect(490, 20, 106, 25))
        self.tex_date.setObjectName("texDate")
        self.tex_date.setReadOnly(True)
        self.tex_date.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texDate", 13)

        self.tex_area_answer = QPlainTextEdit(self)
        self.tex_area_answer.move(25, 60)
        self.tex_area_answer.resize(570, 268)
        self.tex_area_answer.setObjectName("texPlainDes")
        style += self.__styleWidget.styleTexPlain("texPlainDes", 12)

        self.but_send = QPushButton(self)
        self.but_send.setText("Enviar")
        self.but_send.setGeometry(QRect(228, 338, 80, 30))
        self.but_send.setObjectName("save")
        style += self.__styleWidget.styleButton("save", "green", "white", 12, "bold", 7)

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(315, 338, 80, 30))
        self.but_cancel.setObjectName("cancel")
        style += self.__styleWidget.styleButton("cancel", "red", "white",  12, "bold", 7)

        self.setStyleSheet(str(style))

    def __launch_Events(self):
        self.but_send.clicked.connect(self. __send)
        self.but_cancel.clicked.connect(self. __cancel)

    def init_window(self):
        self.tex_area_answer.clear()

    def __cancel(self):
        self.setVisible(False)

    def __send(self):
        if self.tex_area_answer.toPlainText() != "":
            self.suggestion.set_answer(self.tex_area_answer.toPlainText())
            self.suggestion.set_state(True)
            self.__list_suggestion.answer(self.suggestion)
            QMessageBox.information(self,"Benavides EPS","Respuesta enviada con éxito!",QMessageBox.Ok,)
            self.setVisible(False)
        else:
            QMessageBox.warning(self,"Benavides EPS","Por favor redacte una respuesta",QMessageBox.Ok,)

    def set_suggestion(self, suggestion):
        if suggestion != None:
            self.suggestion = suggestion
            self.tex_code.setText(suggestion.get_code())
            self.tex_guy.setText(suggestion.get_guy())
            self.tex_date.setText(datetime.datetime.now().strftime('%d-%m-%Y'))

