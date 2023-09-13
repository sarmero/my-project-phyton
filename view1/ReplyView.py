from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QDialog, QLabel, QPlainTextEdit, QPushButton
from component.StyleWidget import StyleWidget
from controller.ListSuggestion import ListSuggestion
from controller.ListUser import ListUser


class ReplyView(QDialog):
    __list_pccs = ListSuggestion()
    __list_user = ListUser()

    def __init__(self, list_pccs, list_user):
        super().__init__()
        self.__list_pccs = list_pccs
        self.__list_user = list_user
        self.__styleWidget = StyleWidget()

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Respuesta")
        self.resize(500, 300)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("#13293d")

        self.lab_code = QLabel(self)
        self.lab_code.setText("Código: ")
        self.lab_code.setObjectName("labelCode")
        self.lab_code.setGeometry(QRect(25, 10, 45, 25))
        style += self.__styleWidget.styleLabel(
            "labelCode", "#4e91Cd", "white", "Arial", 13, "bold"
        )

        self.lab_code_edit = QLabel(self)
        self.lab_code_edit.setText("210478")
        self.lab_code_edit.setObjectName("labelCode3")
        self.lab_code_edit.setGeometry(QRect(75, 10, 50, 25))
        style += self.__styleWidget.styleLabel(
            "labelCode3", "orange", "White", "Arial", 13, ""
        )

        self.lab_guy = QLabel(self)
        self.lab_guy.setText("Tipo: ")
        self.lab_guy.setObjectName("labelGuy")
        self.lab_guy.setGeometry(QRect(135, 10, 30, 25))
        style += self.__styleWidget.styleLabel(
            "labelGuy", "#4e91Cd", "white", "Arial", 13, "bold"
        )

        self.lab_guy_edit = QLabel(self)
        self.lab_guy_edit.setText("Sugerencia")
        self.lab_guy_edit.setObjectName("labelGuy2")
        self.lab_guy_edit.setGeometry(QRect(170, 10, 70, 25))
        style += self.__styleWidget.styleLabel(
            "labelGuy2", "orange", "White", "Arial", 13, ""
        )

        self.lab_user = QLabel(self)
        self.lab_user.setText("Usuario: ")
        self.lab_user.setObjectName("labelUser")
        self.lab_user.setGeometry(QRect(255, 10, 50, 25))
        style += self.__styleWidget.styleLabel(
            "labelUser", "#4e91Cd", "white", "Arial", 13, "bold"
        )

        self.lab_user_edit = QLabel(self)
        self.lab_user_edit.setText("Juan Andres Perez Hurtado")
        self.lab_user_edit.setObjectName("labelUser2")
        self.lab_user_edit.setGeometry(QRect(310, 10, 200, 25))
        style += self.__styleWidget.styleLabel(
            "labelUser2", "orange", "White", "Arial", 13, ""
        )

        self.tex_area_answer = QPlainTextEdit(self)
        self.tex_area_answer.move(25, 40)
        self.tex_area_answer.resize(450, 210)

        self.but_send = QPushButton(self)
        self.but_send.setText("Enviar")
        self.but_send.setGeometry(QRect(170, 260, 75, 25))
        self.but_send.setObjectName("send")
        style += self.__styleWidget.styleButton(
            "send", "orange", "#13293d", "Arial", 12, "bold", 12
        )
        # hBoxLayout.addWidget(self.but_save)

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(255, 260, 75, 25))
        self.but_cancel.setObjectName("cancel")
        style += self.__styleWidget.styleButton(
            "cancel", "red", "white", "Arial", 12, "bold", 12
        )
        # hBoxLayout.addWidget(self.but_cancel)

        self.setStyleSheet(str(style))

    def __launch_Events(self):
        pass
