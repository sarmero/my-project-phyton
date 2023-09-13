from datetime import datetime
from sqlite3 import Date
from PyQt5.QtCore import QDateTime, QRect, Qt
from PyQt5.QtWidgets import QComboBox, QDialog, QLabel, QLineEdit, QMessageBox, QPushButton,QCalendarWidget,QPlainTextEdit


class InfoResponseView (QDialog):
    def __init__(self, vector_claim_suggestions):
        super().__init__()
        self.__vector_claim_suggestions = vector_claim_suggestions

        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("información respuesta")
        self.setFixedSize(718, 574)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        # botones de la ventana
        self.but_search = QPushButton(self)
        self.but_acepte = QPushButton(self)
        self.but_update = QPushButton(self)
        # botones de la ventana
        self.but_search.setText("Buscar ")
        self.but_search.setGeometry(QRect(202, 87, 66, 25))
        self.but_acepte.setText("Aceptar")
        self.but_acepte.setGeometry(QRect(217, 528, 139, 30))
        self.but_update.setText("actualizar")
        self.but_update.setGeometry(QRect(385, 528, 139, 30))
        # Crear una etiqueta y asociar a la ventana
        self.lab_code = QLabel(self)
        self.lab_información_claim = QLabel(self)
        self.lab_tipo_comentario = QLabel(self)
        self.lab_date_register = QLabel(self)
        self.lab_descry = QLabel(self)
        self.lab_register_respuesta = QLabel(self)
        self.lab_respuesta = QLabel(self)
        self.lab_estado = QLabel(self)
        self.lab_date_system = QLabel(self)

        self.lab_code.setText("Código")
        self.lab_code.setGeometry(QRect(44, 89, 43, 25))
        self.lab_información_claim.setText("Información de la queja o sugerencia")
        self.lab_información_claim.setStyleSheet("font-size: 24px")
        self.lab_información_claim.setGeometry(QRect(156, 42, 405, 28))
        self.lab_tipo_comentario.setText("Tipo comentario")
        self.lab_tipo_comentario.setGeometry(QRect(379, 128, 98, 25))
        self.lab_date_register.setText("Fecha de registro:")
        self.lab_date_register.setGeometry(QRect(377, 90, 108, 25))
        self.lab_descry.setText("Descripción")
        self.lab_descry.setGeometry(QRect(44, 136, 73, 21))
        self.lab_register_respuesta.setText("Información respuesta")
        self.lab_register_respuesta.setStyleSheet("font-size: 24px")
        self.lab_register_respuesta.setGeometry(QRect(227, 313, 304, 28))
        self.lab_respuesta.setText("Respuesta")
        self.lab_respuesta.setGeometry(QRect(40, 405, 67, 25))
        self.lab_date_system.setText("Fecha del sistema")
        self.lab_date_system.setGeometry(QRect(377, 352, 108, 25))
        self.lab_estado.setText("Estado")
        self.lab_estado.setGeometry(QRect(44, 344, 59, 25))

        # cuadro de texto de la ventana
        self.tex_code = QLineEdit(self)
        self.tex_descry = QPlainTextEdit(self)
        self.tex_respuesta = QPlainTextEdit(self)
        self.tex_date_register =QLineEdit(self)
        self.tex_date_sis = QLineEdit(self)
        self.tex_tipo_come = QLineEdit(self)
        self.tex_estado = QLineEdit(self)
        # Ubicar en la ventana
        self.tex_code.setGeometry(QRect(93, 87, 100, 27))
        self.tex_descry.setGeometry(QRect(44, 157, 630, 140))
        self.tex_respuesta.setGeometry(QRect(44, 426, 630, 78))
        self.tex_date_register.setGeometry(QRect(499, 87, 155, 27))
        self.tex_date_sis.setGeometry(QRect(499, 348, 155, 27))
        self.tex_tipo_come.setGeometry(QRect(499, 125, 100, 27))
        self.tex_estado.setGeometry(QRect(117, 341, 100, 27))

    def __launch_events(self):
        self.but_search.clicked.connect(self.__show_by_code)
        self.but_update.clicked.connect(self.__update_register)
        self.but_acepte.clicked.connect(self.__acepte)

    def init_window(self):
        self.tex_date_register.setText("")
        self.tex_date_sis.setText("")
        self.tex_estado.setText("")
        self.tex_tipo_come.setText("")
        self.tex_descry.clear()
        self.tex_respuesta.clear()

    def __show_by_code(self):
        self.tex_descry.clear()
        self.tex_respuesta.clear()

        if self.tex_code.text() != "":
            code = self.tex_code.text()
            suggestions = self.__vector_claim_suggestions.search_by_code(code)

            if suggestions is not None:
                type = suggestions.type()
                date = suggestions.date()
                description = suggestions.description()
                response = suggestions.response()
                state = suggestions.state()
                date_response = suggestions.date_response()

                self.tex_tipo_come.setText(type)
                self.tex_date_register.setText(date)
                self.tex_descry.setPlainText(description)
                self.tex_respuesta.setPlainText(response)
                self.tex_estado.setText(state)
                self.tex_date_sis.setText(date_response)

            else:
                QMessageBox.information(self,"Registrar respuesta","No existe sugestión con ese código",QMessageBox.Ok,)
        else:
            QMessageBox.information(self,"Registrar respuesta","Escriba un código",QMessageBox.Ok,)

    def __acepte(self):
        self.setVisible(False)

    def __update_register(self):
        self.__show_by_code()