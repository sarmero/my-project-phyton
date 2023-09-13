import datetime
from sqlite3 import Date
from PyQt5.QtCore import QDateTime, QRect, Qt
from PyQt5.QtWidgets import QComboBox, QDialog, QLabel, QLineEdit, QMessageBox, QPushButton,QCalendarWidget,QPlainTextEdit


class RegisterResponseView (QDialog):
    def __init__(self, vector_claim_suggestions, vector_user):
        super().__init__()
        self.__vector_claim_suggestions = vector_claim_suggestions
        self.__vector_user = vector_user
        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Registrar respuesta")
        self.setFixedSize(744, 596)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        # botones de la ventana
        self.but_search = QPushButton(self)
        self.but_save = QPushButton(self)
        self.but_cancel = QPushButton(self)
        # botones de la ventana
        self.but_search.setText("Buscar ")
        self.but_search.setGeometry(QRect(251, 54, 66, 25))
        self.but_save.setText("Guardar ")
        self.but_save.setGeometry(QRect(221, 548, 139, 25))
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(390, 548, 139, 25))
        # Crear una etiqueta y asociar a la ventana
        self.lab_code = QLabel(self)
        self.lab_información_claim = QLabel(self)
        self.lab_tipo_comentario = QLabel(self)
        self.lab_date_register = QLabel(self)
        self.lab_descry = QLabel(self)
        self.lab_register_respuesta = QLabel(self)
        self.lab_respuesta = QLabel(self)
        self.lab_email = QLabel(self)
        self.lab_cell = QLabel(self)
        self.lab_estado = QLabel(self)
        self.lab_date_system = QLabel(self)

        self.lab_code.setText("Código")
        self.lab_code.setGeometry(QRect(89, 57, 43, 25))
        self.lab_información_claim.setText("Información de la queja o sugerencia")
        self.lab_información_claim.setStyleSheet("font-size: 24px")
        self.lab_información_claim.setGeometry(QRect(169, 97, 405, 28))
        self.lab_tipo_comentario.setText("Tipo comentario")
        self.lab_tipo_comentario.setGeometry(QRect(57, 146, 98, 25))
        self.lab_date_register.setText("Fecha de registro:")
        self.lab_date_register.setGeometry(QRect(410, 146, 108, 25))
        self.lab_descry.setText("Descripción")
        self.lab_descry.setGeometry(QRect(57, 177, 73, 21))
        self.lab_register_respuesta.setText("Registrar respuesta")
        self.lab_register_respuesta.setStyleSheet("font-size: 24px")
        self.lab_register_respuesta.setGeometry(QRect(264, 313, 216, 28))
        self.lab_respuesta.setText("Respuesta")
        self.lab_respuesta.setGeometry(QRect(57, 341, 67, 25))
        self.lab_email.setText("Email")
        self.lab_email.setGeometry(QRect(75, 456, 36, 25))
        self.lab_cell.setText("Fijo")
        self.lab_cell.setGeometry(QRect(559, 456, 108, 25))
        self.lab_estado.setText("Estado")
        self.lab_estado.setGeometry(QRect(77, 496, 59, 25))
        self.lab_date_system.setText("Fecha del sistema")
        self.lab_date_system.setGeometry(QRect(410, 498, 108, 25))

        # cuadro de texto de la ventana
        self.tex_code = QLineEdit(self)
        self.tex_descry = QPlainTextEdit(self)
        self.tex_respuesta = QPlainTextEdit(self)
        self.tex_email = QLineEdit(self)
        self.tex_cell = QLineEdit(self)
        self.tex_date_register =QLineEdit(self)
        self.tex_date_sis = QLineEdit(self)
        self.tex_tipo_come = QLineEdit(self)
        # Ubicar en la ventana
        self.tex_code.setGeometry(QRect(142, 54, 100, 27))
        self.tex_descry.setGeometry(QRect(57, 198, 630, 78))
        self.tex_respuesta.setGeometry(QRect(57, 362, 630, 78))
        self.tex_email.setGeometry(QRect(150, 453, 282, 25))
        self.tex_cell.setGeometry(QRect(587, 456, 100, 25))
        self.tex_date_register.setGeometry(QRect(532, 146, 155, 27))
        self.tex_date_sis.setGeometry(QRect(532, 494, 155, 27))
        self.tex_tipo_come.setGeometry(QRect(160, 143, 100, 27))

        # combo box
        self.com_estado = QComboBox(self)
        self.com_estado.setGeometry(QRect(150, 493, 100, 27))
        self.com_estado.addItems(["Pendiente","Revisada"])

    def __launch_events(self):
        self.but_search.clicked.connect(self.__show_by_code)
        self.but_cancel.clicked.connect(self.__cancel)
        self.but_save.clicked.connect(self.__save_response)

    def init_window(self):
        self.tex_date_register.setText("")
        self.tex_email.setText("")
        self.tex_cell.setText("")
        self.tex_date_sis.setText("")
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
                id_user = suggestions.id_user()

                self.tex_tipo_come.setText(type)
                self.tex_date_register.setText(date)
                self.tex_descry.setPlainText(description)

                user = self.__vector_user.search_by_id(id_user)

                mail = user.mail()
                fijo = user.cell()

                self.tex_email.setText(mail)
                self.tex_cell.setText(fijo)
                hora_actual = datetime.datetime.now()
                self.tex_date_sis.setText(str(hora_actual.day)+"/"+str(hora_actual.month)+"/"+str(hora_actual.year))

            else:
                QMessageBox.information(self,"Registrar respuesta","No existe sugestión con ese código",QMessageBox.Ok,)
        else:
            QMessageBox.information(self,"Registrar respuesta","Escriba un código",QMessageBox.Ok,)

    def __save_response(self):
        response = self.tex_respuesta.toPlainText()
        if response != "":
            code = self.tex_code.text()
            date_response = self.tex_date_sis.text()
            state = self.com_estado.currentText()
            self.__vector_claim_suggestions.register_response(code, response, date_response, state)
            QMessageBox.information(self,"Registrar respuesta","Respuesta guardada",QMessageBox.Ok,)
            self.setVisible(False)
        else:
            QMessageBox.information(self,"Registrar respuesta","Escriba una respuesta",QMessageBox.Ok,)


    def __cancel(self):
        self.setVisible(False)