import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from view.Ui_MainWindowView import Ui_MainWindow


class App:

    def main(self):
        app = QApplication(sys.argv)
        window = QMainWindow()
        main_window = Ui_MainWindow()
        main_window.setupUi(window)
        window.show()  # Mostrar ventana

        app.exec_()


app = App()
app.main()
