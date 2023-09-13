import sys
from PySide6.QtWidgets import QApplication
from view.MainWindow import MainWindow


class App:

    def main(self):
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()

        app.exec_()


app = App()
app.main()
