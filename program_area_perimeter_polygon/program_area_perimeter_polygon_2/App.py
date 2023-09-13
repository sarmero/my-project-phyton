import sys

from PyQt5.QtWidgets import QApplication

from view.ViewMainWindow1 import MainWindow


class App:

    def main(self):
        app = QApplication(sys.argv)
        window = MainWindow()
        window.init_window()
        window.show()

        app.exec_()


app = App()
app.main()
