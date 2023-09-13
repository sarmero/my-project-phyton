
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel


class QLabelClickable(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, event):
        self.clicked.emit()