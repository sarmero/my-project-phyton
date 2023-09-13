import sys
from PyQt5.QtWidgets import QApplication

from view.MainWindowView import MainWindowView


class App:

    def main(self):
        app = QApplication(sys.argv)  # iniciar el sistema gráfico
        window = MainWindowView()  # crear objecto ventana
        #window.open_file()  # cargar los polígonos
        window.init_window()
        window.show()  # mostrar ventana
        app.exec_()  # saliendo del sistema gráfico

app = App()

app.main()
