import sys
from PyQt5.QtWidgets import QApplication
from View.MainWindowEPS import MainWindowEPS



class App:

    def main(self):
        app = QApplication(sys.argv)  # iniciar sistema gráfico
        window_client = MainWindowEPS()  # crear objeto de la ventana
        window_client.open_file()
        # window_client.init_window()
        window_client.show()  # mostrar ventana

        # window_eps = MainWindowEPS()
        # window_eps.open_file()
        # window_eps.init_window()
        # window_eps.show()  # mostrar ventana

        app.exec_()  # saliendo del sistema


app = App()
app.main()
