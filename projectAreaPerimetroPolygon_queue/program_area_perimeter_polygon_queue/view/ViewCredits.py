from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QDialog, QPushButton


class ViewCredits(QDialog):

    def __init__(self):
        super().__init__()
        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Créditos")
        self.setFixedSize(550, 300)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.lab_logo = QLabel(self)
        self.lab_logo.setGeometry(QRect(20, 20, 250, 250))
        canvas = QPixmap("images/logo.jpg")
        self.lab_logo.setPixmap(canvas)

        self.lab_message = QLabel(self)
        self.lab_message.setText("")
        self.lab_message.setGeometry(QRect(290, 20, 240, 220))

        self.but_ok = QPushButton(self)
        self.but_ok.setText("Aceptar")
        self.but_ok.setGeometry(QRect(360, 240, 100, 30))

    def __launch_Events(self):
        self.but_ok.clicked.connect(self.__ok)

    def __ok(self):
        self.setVisible(False)
