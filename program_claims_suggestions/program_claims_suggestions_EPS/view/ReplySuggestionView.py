from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QRegExp, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from component.StyleWidget import StyleWidget

from controller.ListSuggestion import ListSuggestion
from view.ReplyView import ReplyView


class ReplySuggestionView(QDialog):
    

    def __init__(self, list_suggestion, list_users):
        super().__init__()
        self.__window_reply = ReplyView(list_suggestion)
        self.__list_suggestion = list_suggestion
        self.__list_users = list_users
        self.__suggestion = None
        self.__styleWidget = StyleWidget("Comic Sans MS")

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Responder sugestión")
        self.resize(620, 530)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("#159438")

        canvas = QPixmap("images/fondo_reply.png")
        self.lab_background = QLabel(self)
        self.lab_background.setGeometry(QRect(0, 0, 620, 530))
        self.lab_background.setPixmap(canvas)

        self.lab_search_code = QLabel(self)
        self.lab_search_code.setText("Código:")
        self.lab_search_code.setGeometry(204, 40, 50, 25)
        self.lab_search_code.setObjectName("labelCodeSearch")
        style += self.__styleWidget.styleLabel("labelCodeSearch", "white", "#4e91cd", 13, "bold")

        self.com_code = QComboBox(self)
        self.com_code.setGeometry(QRect(252, 40, 115, 25))
        self.com_code.setObjectName("texIdSearch")
        style += self.__styleWidget.styleLine("texIdSearch", 12)

        self.lab_id = QLabel(self)
        self.lab_id.setText("Identificación:")
        self.lab_id.setObjectName("labelId")
        self.lab_id.setGeometry(QRect(35, 82, 100, 25))
        style += self.__styleWidget.styleLabel("labelId", "#351C75", "green", 13, "bold")

        self.tex_id = QLineEdit(self)
        self.tex_id.setGeometry(QRect(30, 105, 230, 25))
        self.tex_id.setObjectName("texId")
        self.tex_id.setReadOnly(True)
        style += self.__styleWidget.styleLine("texId",13)

        self.lab_guy = QLabel(self)
        self.lab_guy.setText("Tipo:")
        self.lab_guy.setGeometry(275, 82, 35, 25)
        self.lab_guy.setObjectName("labelGuy")
        style += self.__styleWidget.styleLabel("labelGuy", "white", "#351C75",  13, "bold")

        self.tex_guy = QLineEdit(self)
        self.tex_guy.setGeometry(QRect(270, 105, 140, 25))
        self.tex_guy.setObjectName("texGuy")
        self.tex_guy.setReadOnly(True)
        self.tex_guy.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texGuy",  13)

        self.lab_state = QLabel(self)
        self.lab_state.setText("Estado:")
        self.lab_state.setGeometry(425, 82, 50, 25)
        self.lab_state.setObjectName("labelState")
        style += self.__styleWidget.styleLabel("labelState", "white", "#351C75",  13, "bold")

        self.tex_state = QLineEdit(self)
        self.tex_state.setGeometry(QRect(420, 105, 170, 25))
        self.tex_state.setObjectName("texState")
        self.tex_state.setReadOnly(True)
        self.tex_state.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texState",  13)

        self.lab_name = QLabel(self)
        self.lab_name.setText("Nombre:")
        self.lab_name.setObjectName("labelUser")
        self.lab_name.setGeometry(QRect(35, 145, 60, 25))
        style += self.__styleWidget.styleLabel("labelUser", "#351C75", "green", 13, "bold")

        self.tex_name = QLineEdit(self)
        self.tex_name.setGeometry(QRect(30, 166, 330, 25))
        self.tex_name.setObjectName("texName")
        self.tex_name.setReadOnly(True)
        style += self.__styleWidget.styleLine("texName",13)

        self.lab_date = QLabel(self)
        self.lab_date.setText("Fecha:")
        self.lab_date.setObjectName("labelDate")
        self.lab_date.setGeometry(QRect(378, 145, 45, 25))
        style += self.__styleWidget.styleLabel("labelDate", "white", "#351C75", 13, "bold")

        self.tex_date = QLineEdit(self)
        self.tex_date.setGeometry(QRect(373, 166, 117, 25))
        self.tex_date.setObjectName("texDate")
        self.tex_date.setReadOnly(True)
        self.tex_date.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texDate", 13)

        self.lab_hour = QLabel(self)
        self.lab_hour.setText("Hora:")
        self.lab_hour.setObjectName("labelHour")
        self.lab_hour.setGeometry(QRect(502, 145, 35, 25))
        style += self.__styleWidget.styleLabel("labelHour","white", "#351C75", 13, "bold")

        self.tex_hour = QLineEdit(self)
        self.tex_hour.setGeometry(QRect(497, 166, 92, 25))
        self.tex_hour.setObjectName("texHour")
        self.tex_hour.setReadOnly(True)
        self.tex_hour.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLine("texHour", 13)

        self.lab_address = QLabel(self)
        self.lab_address.setText("Dirección: ")
        self.lab_address.setObjectName("labelAddress")
        self.lab_address.setGeometry(QRect(35, 200, 90, 25))
        style += self.__styleWidget.styleLabel("labelAddress", "#351C75", "green", 13, "bold")

        self.tex_address = QLineEdit(self)
        self.tex_address.setGeometry(QRect(30, 221, 275, 25))
        self.tex_address.setObjectName("texAddress")
        self.tex_address.setReadOnly(True)
        style += self.__styleWidget.styleLine("texAddress", 13)

        self.lab_mail = QLabel(self)
        self.lab_mail.setText("Email:")
        self.lab_mail.setObjectName("labelMail")
        self.lab_mail.setGeometry(QRect(320, 200, 90, 25))
        style += self.__styleWidget.styleLabel("labelMail", "#351C75", "green", 13, "bold")

        self.tex_mail = QLineEdit(self)
        self.tex_mail.setGeometry(QRect(315, 221, 275, 25))
        self.tex_mail.setObjectName("texMail")
        self.tex_mail.setReadOnly(True)
        style += self.__styleWidget.styleLine("texMail", 13)

        self.lab_description = QLabel(self)
        self.lab_description.setText("Descripción")
        self.lab_description.setGeometry(QRect(35, 268, 75, 25))
        self.lab_description.setObjectName("labelDes")
        style += self.__styleWidget.styleLabel("labelDes", "#351C75", "green", 13, "bold")

        self.tex_area_description = QPlainTextEdit(self)
        self.tex_area_description.move(30, 290)
        self.tex_area_description.resize(560, 185)
        self.tex_area_description.setObjectName("texPlainDes")
        self.tex_area_description.setReadOnly(True)
        style += self.__styleWidget.styleTexPlain("texPlainDes", 12)

        self.but_reply = QPushButton(self)
        self.but_reply.setText("Responder")
        self.but_reply.setGeometry(QRect(215, 490, 90, 30))
        self.but_reply.setObjectName("save")
        style += self.__styleWidget.styleButton("save", "green", "white", 12, "bold", 7)

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(310, 490, 90, 30))
        self.but_cancel.setObjectName("cancel")
        style += self.__styleWidget.styleButton("cancel", "red", "white",  12, "bold", 7)

        self.setStyleSheet(str(style))

    def __launch_Events(self):
        self.but_cancel.clicked.connect(self.__cancel)
        self.but_reply.clicked.connect(self.__reply)
        self.com_code.currentTextChanged.connect(self. __show_data)
    

    def __show_data(self):
        if self.com_code.currentText() != "":
            suggestion = self.__list_suggestion.search_by_code(self.com_code.currentText())
            user = self.__list_users.search_by_id(suggestion.get_id_user())
            self.__suggestion = suggestion

            self.tex_id.setText(user.get_id())
            self.tex_name.setText(user.get_name())
            self.tex_address.setText(user.get_address())
            self.tex_mail.setText(user.get_mail())

            self.tex_date.setText(suggestion.get_date())
            self.tex_guy.setText(suggestion.get_guy())
            self.tex_state.setText("Revisado" if suggestion.get_state() == True else "Pendiente")
            self.tex_area_description.setPlainText(suggestion.get_description())
            self.tex_hour.setText(suggestion.get_hour())

    def __reply(self):
        if self.__verify_code() == True:
            self.__window_reply.init_window()
            self.__window_reply.set_suggestion(self.__suggestion)
            self.__window_reply.setVisible(True)

    def __verify_code(self):
        if self.__suggestion.get_answer() != "":
            QMessageBox.warning(self,"Benavides EPS","Usted ya le respondió a este usuario \n\n Actualizando lista...",QMessageBox.Ok,)
            self.init_window()
            return False
        else:
            return True

    def __fill_up_combo(self):
        list_code = self.__list_suggestion.search_list_code()

        i = list_code.front()
        if list_code.size() > 0:
            self.but_reply.setEnabled(True)
            self.com_code.clear()
            while i != None:
                self.com_code.addItem(i.value) 
                i = i.next
        else:
            QMessageBox.information(self,"Benavides EPS","No hay sugestiones pendientes",QMessageBox.Ok,)
            self.setVisible(False)
            self.but_reply.setEnabled(False)

    def __cancel(self):
        self.setVisible(False)

    def init_window(self):
        self.tex_address.clear()
        self.tex_name.clear()
        self.tex_id.clear()
        self.tex_state.clear()
        self.tex_mail.clear()
        self.tex_guy.clear()
        self.tex_area_description.clear()
        self.tex_date.clear()
        self.tex_hour.clear()
        self.com_code.clear()
        self.but_reply.setEnabled(False)
        self.__fill_up_combo()
        
    

