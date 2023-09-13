from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton


class CreditView(QDialog):

    def __init__(self):
        super().__init__()  # Constructor de la clase padre
        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Créditos")
        self.setFixedSize(550, 300)
        # Activar una ventana modal(no funciona la principal hasta que termine la secundaria)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        # Quita el botón de ayuda de la ventana
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Crear una etiqueta y asociarla a la ventana
        self.lab_logo = QLabel(self)
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_logo.setGeometry(QRect(20, 20, 250, 250))
        # Crea una imagen
        canvas = QPixmap("image/logo.jpeg")
        #
        self.lab_logo.setPixmap(canvas)

        # Crear una etiqueta y asociarla a la ventana
        self.lab_message = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_message.setText(
            "Gestor de polígonos\n" + "Hecho por: Mauricio Racines\n" + "Udenar - 2023")
        # Ubicar en la ventana (x,y,ancho,largo)
        self.lab_message.setGeometry(QRect(290, 20, 240, 220))

        # Crear un botón y asociarlo a la ventana
        self.but_ok = QPushButton(self)
        # Colocar el texto al botón
        self.but_ok.setText("Aceptar")
        # Ubicar en la ventana(x,y,ancho,largo)
        self.but_ok.setGeometry(QRect(360, 240, 100, 30))

    def __launch_events(self):
        self.but_ok.clicked.connect(self.__ok)  # Evento para botón ok
        pass

    def init_window(self):
        pass

    def __ok(self):  # Oculta la ventana
        self.setVisible(False)
