from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import (
    QComboBox,
    QDialog,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
)
from component.StyleWidget import StyleWidget

from controller.ListSuggestion import ListSuggestion


class RegisterPccsView(QDialog):
    __list_pccs = ListSuggestion()

    def __init__(self, list_pccs):
        super().__init__()
        self.__list_pccs = list_pccs
        self.__styleWidget = StyleWidget()

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Gestor de polígono")
        self.setFixedSize(570, 400)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("#13293d")

        self.lab_id = QLabel(self)
        self.lab_id.setText("Identificación:")
        self.lab_id.setGeometry(40, 20, 87, 25)
        self.lab_id.setObjectName("labelId")
        style += self.__styleWidget.styleLabel("labelId", "orange", "#4e91cd", "Arial", 13, "bold")

        self.tex_id = QLineEdit(self)
        self.tex_id.setGeometry(QRect(132, 20, 150, 25))
        self.tex_id.setObjectName("texId")
        style += self.__styleWidget.styleLine("texId", "Arial", 12)

        self.but_validate = QPushButton(self)
        self.but_validate.setText("Validar")
        self.but_validate.setGeometry(QRect(287, 20, 65, 25))
        self.but_validate.setObjectName("buttonValidate")
        style += self.__styleWidget.styleButton("buttonValidate", "#4e91cd", "white", "Arial", 12, "bold", 12)

        self.lab_guy = QLabel(self)
        self.lab_guy.setText("Tipo: ")
        self.lab_guy.setGeometry(363, 20, 32, 25)
        self.lab_guy.setObjectName("labelGuy")
        style += self.__styleWidget.styleLabel("labelGuy", "orange", "#4e91cd", "Arial", 13, "bold")

        self.com_guy = QComboBox(self)
        self.com_guy.setGeometry(QRect(402, 20, 110, 25))
        self.com_guy.setObjectName("com")
        style += self.__styleWidget.styleLine("com", "Arial", 12)

        self.lab_code = QLabel(self)
        self.lab_code.setText("Código: 2108")
        self.lab_code.setGeometry(QRect(455, 50, 90, 25))
        self.lab_code.setObjectName("labelCode")
        style += self.__styleWidget.styleLabel("labelCode", "orange", "#4e91cd", "Arial", 13, "bold")

        self.lab_description = QLabel(self)
        self.lab_description.setText("Descripción")
        self.lab_description.setGeometry(QRect(25, 50, 75, 25))
        self.lab_description.setObjectName("labelDes")
        style += self.__styleWidget.styleLabel("labelDes", "orange", "#4e91cd", "Arial", 12, "")

        self.tex_area_description = QPlainTextEdit(self)
        self.tex_area_description.move(25, 75)
        self.tex_area_description.resize(520, 270)

        self.but_send = QPushButton(self)
        self.but_send.setText("Enviar")
        self.but_send.setGeometry(QRect(202, 360, 80, 30))
        self.but_send.setObjectName("buttonSend")
        style += self.__styleWidget.styleButton("buttonSend", "orange", "#13293d", "Arial", 12, "bold", 12)

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(287, 360, 80, 30))
        self.but_cancel.setObjectName("buttonCancel")
        style += self.__styleWidget.styleButton("buttonCancel", "red", "White", "Arial", 12, "bold", 12)

        self.setStyleSheet(str(style))

    def __launch_Events(self):
        self.but_validate.clicked.connect(self. __validate_user)


    def __validate_user(self):
        self.__list_pccs

