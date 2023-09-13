from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QDialog, QPushButton

from component.StyleWidget import StyleWidget


class CreditsView(QDialog):
    def __init__(self):
        super().__init__()
        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Créditos")
        self.setFixedSize(500, 400)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.__styleWidget = StyleWidget("Comic Sans MS")
        style = self.__styleWidget.styleDialog("#159438")

        self.lab_logo = QLabel(self)
        self.lab_logo.setGeometry(QRect(0, 0, 200, 400))
        canvas = QPixmap("images/credits_.jpg")
        self.lab_logo.setPixmap(canvas)

        self.lab_logo = QLabel(self)
        self.lab_logo.setGeometry(QRect(142, 152, 111, 117))
        canvas = QPixmap("images/UniNar.png")
        self.lab_logo.setPixmap(canvas)

        self.lab_title = QLabel(self)
        self.lab_title.setText("Gestor de sugerencias")
        self.lab_title.setObjectName("labelSugerencia")
        self.lab_title.setGeometry(QRect(216, 42, 280, 38))
        style += self.__styleWidget.styleLabel("labelSugerencia", "white", "lightgreen", 24, "bold")

        self.lab_name_eps = QLabel(self)
        self.lab_name_eps.setText("EPS Benavides")
        self.lab_name_eps.setObjectName("labelA")
        self.lab_name_eps.setGeometry(QRect(300, 78, 105, 25))
        style += self.__styleWidget.styleLabel("labelA", "white", "lightgreen", 14, "bold")

        self.lab = QLabel(self)
        self.lab.setText("Hecho por:")
        self.lab.setObjectName("labelL")
        self.lab.setGeometry(QRect(320, 159, 70, 25))
        style += self.__styleWidget.styleLabel("labelL", "white", "lightgreen", 13, "bold")

        self.lab_name1 = QLabel(self)
        self.lab_name1.setText("Pablo Andres Benavides")
        self.lab_name1.setObjectName("labelB")
        self.lab_name1.setGeometry(QRect(280, 190, 150, 25))
        style += self.__styleWidget.styleLabel("labelB", "white", "lightgreen", 13, "bold")

        self.lab_name2 = QLabel(self)
        self.lab_name2.setText("Sebastian Armero")
        self.lab_name2.setObjectName("labelC")
        self.lab_name2.setGeometry(QRect(298, 212, 120, 25))
        style += self.__styleWidget.styleLabel("labelC", "white", "lightgreen", 13, "bold")

        self.lab_un = QLabel(self)
        self.lab_un.setText("Universidad de Nariño")
        self.lab_un.setObjectName("labelD")
        self.lab_un.setGeometry(QRect(262, 285, 190, 28))
        style += self.__styleWidget.styleLabel("labelD", "white", "lightgreen", 16, "bold")

        self.lab_date = QLabel(self)
        self.lab_date.setText("2023")
        self.lab_date.setObjectName("labelS")
        self.lab_date.setGeometry(QRect(335, 311, 40, 25))
        style += self.__styleWidget.styleLabel("labelS", "white", "lightgreen", 14, "bold")

        self.but_ok = QPushButton(self)
        self.but_ok.setText("Aceptar")
        self.but_ok.setGeometry(QRect(313, 360, 80, 30))
        self.but_ok.setObjectName("ok")
        style += self.__styleWidget.styleButton("ok", "white", "green",  12, "bold", 7)

        self.setStyleSheet(str(style))

    def __launch_Events(self):
        self.but_ok.clicked.connect(self.__ok)

    def __ok(self):
        self.setVisible(False)
