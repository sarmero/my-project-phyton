import sys
from PyQt5.QtWidgets import QApplication
from view.ViewMainWindow import MainWindow


class App:

    def main(self):
        app = QApplication(sys.argv)
        window = MainWindow()
        #window.open_file()
        window.init_window()
        window.show()

        app.exec_()


app = App()
app.main()
