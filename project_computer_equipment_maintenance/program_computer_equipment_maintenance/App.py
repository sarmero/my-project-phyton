import sys
from PyQt5.QtWidgets import QApplication

from view.MainWindowView import MainWindowView


class App:

    def main(self):
        app = QApplication(sys.argv)
        window = MainWindowView()
        # window.open_file()  # cargar los polígonos
        window.init_window()
        window.show()  # Mostrar ventana

        app.exec_()


app = App()
app.main()
