import datetime
from PyQt5.QtCore import QDateTime, QRect, Qt
from PyQt5.QtWidgets import QCalendarWidget, QComboBox, QDateTimeEdit, QDialog, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QPushButton

from classes.ClaimSuggestions import ClaimSuggestions


class RegisterClaimSuggestionsView(QDialog):
    def __init__(self, vector_claim_suggestions, vector_user):
        super().__init__()
        self.__vector__claim_suggestions = vector_claim_suggestions
        self.__vector_user = vector_user
        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Registrar queja o sugerencia")
        self.setFixedSize(770, 578)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        # botones de la ventana
        self.but_search = QPushButton(self)
        self.but_cancel = QPushButton(self)
        self.but_save = QPushButton(self)

        self.but_search.setText("Buscar ")
        self.but_search.setGeometry(QRect(338, 92, 66, 27))
        self.but_cancel.setText("Cancelar ")
        self.but_cancel.setGeometry(QRect(217, 528, 130, 27))
        self.but_save.setText("Guardar")
        self.but_save.setGeometry(QRect(385, 528, 130, 27))
        # cuadro de texto de la ventana
        self.tex_N_ide = QLineEdit(self)
        self.tex_name = QLineEdit(self)
        self.tex_email = QLineEdit(self)
        self.tex_cell = QLineEdit(self)
        self.tex_code = QLineEdit(self)
        self.tex_descry = QPlainTextEdit(self)
        self.tex_date_sis = QLineEdit(self)
        self.tex_date_user = QLineEdit(self)
        # Ubicar en la ventana
        self.tex_N_ide.setGeometry(QRect(203, 92, 100, 27))
        self.tex_name.setGeometry(QRect(203, 141, 100, 27))
        self.tex_email.setGeometry(QRect(203, 182, 100, 27))
        self.tex_cell.setGeometry(QRect(514, 182, 100, 27))
        self.tex_code.setGeometry(QRect(162, 269, 100, 27))
        self.tex_descry.setGeometry(QRect(71, 340, 630, 140))
        self.tex_date_sis.setGeometry(QRect(526, 269, 187, 27))
        self.tex_date_user.setGeometry(QRect(514, 142, 187, 27))
        # Crear una etiqueta y asociar a la ventana
        self.lab_N_ide = QLabel(self)
        self.lab_name = QLabel(self)
        self.lab_email = QLabel(self)
        self.lab_cell = QLabel(self)
        self.lab_date = QLabel(self)
        self.lab_información = QLabel(self)
        self.lab_date2 = QLabel(self)
        self.lab_code = QLabel(self)
        self.lab_descripción = QLabel(self)
        self.lab_tipo_come = QLabel(self)
        self.lab_información_que = QLabel(self)
        # Colocar el texto a la etiqueta
        self.lab_N_ide.setText("N° Identificación:")
        self.lab_name.setText("Nombre:")
        self.lab_email.setText("Email:")
        self.lab_cell.setText("Celular:")
        self.lab_date.setText("Fecha de nacimiento:")
        self.lab_información.setText("Información del usuario:")
        self.lab_información.setStyleSheet("font-size: 24px")
        self.lab_date2.setText("Fecha del sistema:")
        self.lab_code.setText("Código:")
        self.lab_descripción.setText("Descripción:")
        self.lab_tipo_come.setText("Tipo comentario:")
        self.lab_información_que.setText("Información de la queja o sugerencia:")
        self.lab_información_que.setStyleSheet("font-size: 24px")

        self.lab_N_ide.setGeometry(QRect(69, 95, 101, 21))
        self.lab_name.setGeometry(QRect(69, 135, 48, 21))
        self.lab_email.setGeometry(QRect(69, 185, 33, 21))
        self.lab_cell.setGeometry(QRect(358, 185, 42, 21))
        self.lab_date.setGeometry(QRect(358, 135, 124, 21))
        self.lab_información.setGeometry(QRect(243, 42, 256, 28))
        self.lab_date2.setGeometry(QRect(404, 273, 79, 21))
        self.lab_code.setGeometry(QRect(71, 273, 43, 21))
        self.lab_descripción.setGeometry(QRect(70, 319, 79, 21))
        self.lab_tipo_come.setGeometry(QRect(406, 311, 98, 21))
        self.lab_información_que.setGeometry(QRect(183, 225, 405, 28))
        # combo box
        self.com_tipo_come = QComboBox(self)
        self.com_tipo_come.setGeometry(QRect(526, 308, 100, 27))
        self.com_tipo_come.addItems(["Petición", "Queja", "Reclamo","Sugerencia"])


    def __launch_events(self):
        self.but_save.clicked.connect(self.__save_suggestions)
        self.but_search.clicked.connect(self.__show_data_user)
        self.but_cancel.clicked.connect(self.__cancel)

    def __save_suggestions(self):
        id_user = self.tex_N_ide.text()
        code = self.tex_code.text()
        date = self.tex_date_sis.text()
        type = self.com_tipo_come.currentText()
        description = self.tex_descry.toPlainText()
        hora_actual = datetime.datetime.now()
        hour = str(hora_actual.hour)+":"+str(hora_actual.minute)
        state = "Pendiente"

        if id_user != "" and code != "" and description != "":
            exists = self.__vector__claim_suggestions.search_code(code)
            if exists is False:
                suggestion = ClaimSuggestions(code, date, hour, id_user, state, type, description)
                self.__vector__claim_suggestions.add_claim_suggestions(suggestion)
                QMessageBox.information(self,"Registrar sugestión","Sugestión agregada",QMessageBox.Ok,)
                self.setVisible(False)
            else:
                QMessageBox.information(self,"Registrar sugestión","el código ya existe",QMessageBox.Ok,)
        else:
            QMessageBox.information(self,"Registrar sugestión","Todas los item son obligatorios",QMessageBox.Ok,)

    def __show_data_user(self):
        id_user = self.tex_N_ide.text()
        if id_user != "":
            user = self.__vector_user.search_by_id(id_user)

            if user is not None:
                name = user.name()
                mail = user.mail()
                date_birth = user.date_birth()
                cell = user.cell()

                self.tex_name.setText(name)
                self.tex_email.setText(mail)
                self.tex_date_user.setText(date_birth)
                self.tex_cell.setText(cell)
                hora_actual = datetime.datetime.now()
                self.tex_date_sis.setText(str(hora_actual.day)+"/"+str(hora_actual.month)+"/"+str(hora_actual.year))

            else:
                QMessageBox.information(self,"Registrar suggestions","No se encontró usuario con el numero de identificación",QMessageBox.Ok,)
        else:
            QMessageBox.information(self,"Registrar suggestion","Ingrese una identificación",QMessageBox.Ok,)

    def __cancel(self):
        self.setVisible(False)


    def init_window(self):
        self.tex_name.setText("")
        self.tex_email.setText("")
        self.tex_date_user.setText("")
        self.tex_cell.setText("")
        self.tex_date_sis.setText("")
        self.tex_N_ide.setText("")
        self.tex_code.setText("")
        self.tex_date_sis.setText("")
        self.tex_descry.clear()