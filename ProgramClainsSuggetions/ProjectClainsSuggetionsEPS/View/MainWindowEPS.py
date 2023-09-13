from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QAction, QComboBox, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QStyle, QTableWidget, QTableWidgetItem
from View.CreditsView import CreditsView
from View.InfoResponseView import InfoResponseView
from View.MainWindowClientView import MainWindowClientView

from View.RegisterResponseView import RegisterResponseView
from controller.ListClaimSuggestions import ListClaimSuggestions
from controller.ListUser import ListUser


class MainWindowEPS (QMainWindow):
    def __init__(self):
        super().__init__()  
        
        self.__vector_claim_suggestions = ListClaimSuggestions()
        self.__vector_user = ListUser()
        self.__window_register_response = RegisterResponseView(self.__vector_claim_suggestions, self.__vector_user)
        self.__window_main_client = MainWindowClientView(self.__vector_claim_suggestions, self.__vector_user)
        self.__window_info_response = InfoResponseView(self.__vector_claim_suggestions)
        self.__window_credits = CreditsView()


        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Buzón de comentarios")
        self.setFixedSize(1024, 768)

        bar_menu = self.menuBar()
        menu_file = bar_menu.addMenu("&Suggestion")
        menu_help = bar_menu.addMenu("&Ayuda")

        self.ite_init_user = QAction("&Iniciar como usuario", self)
        self.ite_register_response = QAction("&Register response", self)
        self.ite_list_info_response = QAction("&Información respuesta", self)
        self.ite_exit = QAction("&Salir", self)
        self.ite_show_credits = QAction("&Créditos", self)

        self.ite_init_user.setIcon(self.style().standardIcon(QStyle.SP_FileIcon))
        self.ite_register_response.setIcon(self.style().standardIcon(QStyle.SP_FileIcon))
        self.ite_list_info_response.setIcon(self.style().standardIcon(QStyle.SP_FileIcon))
        self.ite_exit.setIcon(self.style().standardIcon(QStyle.SP_FileDialogBack))
        self.ite_show_credits.setIcon(self.style().standardIcon(QStyle.SP_MessageBoxInformation))

        self.ite_init_user.setShortcut("CTRL+I")
        self.ite_exit.setShortcut("CTRL+Q")
        self.ite_show_credits.setShortcut("CTRL+H")

        menu_file.addAction(self.ite_init_user)
        menu_file.addSeparator()
        menu_file.addAction(self.ite_register_response)
        menu_file.addAction(self.ite_list_info_response)
        menu_file.addSeparator()
        menu_file.addAction(self.ite_exit)
        menu_help.addAction(self.ite_show_credits)

        self.lab_state = QLabel(self)
        self.lab_code = QLabel(self)
        self.lab_id = QLabel(self)

        self.lab_state.setText("Estado: ")
        self.lab_state.setGeometry(QRect(683, 128, 59, 25))
        self.lab_code.setText("Buscar por código:")
        self.lab_code.setGeometry(QRect(378, 128, 108, 25))
        self.lab_id.setText("Buscar identificación:")
        self.lab_id.setGeometry(QRect(35, 128, 151, 25))

        self.tex_code = QLineEdit(self)
        self.tex_id = QLineEdit(self)
        self.tex_code.setGeometry(QRect(486, 128, 79, 25))
        self.tex_id.setGeometry(QRect(187, 128, 79, 25))

        self.but_register = QPushButton(self)
        self.but_search_code = QPushButton(self)
        self.but_search_id = QPushButton(self)
        self.but_search_state = QPushButton(self)

        self.but_register.setText("Registrar Respuesta ")
        self.but_register.setGeometry(QRect(30, 50, 146, 30))
        self.but_search_code.setText("buscar")
        self.but_search_code.setGeometry(QRect(571, 128, 80, 25))
        self.but_search_id.setText("buscar")
        self.but_search_id.setGeometry(QRect(266, 128, 80, 25))
        self.but_search_state.setText("buscar")
        self.but_search_state.setGeometry(QRect(836, 128, 80, 25))

        self.com_state = QComboBox(self)
        self.com_state.setGeometry(QRect(731, 128, 100, 25))
        self.com_state.addItems(["Pendiente","Revisada","Todo"])
        

        # self.dat_state = QData(self)

        self.tab_eps = QTableWidget(self)
        self.tab_eps.setGeometry(QRect(30, 203, 970, 558))
        # colocar la cantidad de filas y columnas
        self.tab_eps.setColumnCount(6)
        self.tab_eps.setRowCount(0)
        self.tab_eps.setColumnWidth(0, 100)  # Columna 1
        self.tab_eps.setColumnWidth(1, 100)  # Columna 2
        self.tab_eps.setColumnWidth(2, 100)  # Columna 3
        self.tab_eps.setColumnWidth(3, 70)  # Columna 4
        self.tab_eps.setColumnWidth(4, 500)  # Columna 5
        self.tab_eps.setColumnWidth(5, 100)  # Columna 6

        """
        la lista debemos modificar los nombres al ingresar eventos
        """
        ite_code = QTableWidgetItem("Tipo")
        self.tab_eps.setHorizontalHeaderItem(0, ite_code)  # Columna 1

        ite_quantity_points = QTableWidgetItem("código")
        self.tab_eps.setHorizontalHeaderItem(1, ite_quantity_points)  # Columna 2

        ite_perimeter = QTableWidgetItem("fecha")
        self.tab_eps.setHorizontalHeaderItem(2, ite_perimeter)  # Columna 3

        ite_code = QTableWidgetItem("hora")
        self.tab_eps.setHorizontalHeaderItem(3, ite_code)  # Columna 4

        ite_quantity_points = QTableWidgetItem("descripción")
        self.tab_eps.setHorizontalHeaderItem(4, ite_quantity_points)  # Columna 5

        ite_perimeter = QTableWidgetItem("estado")
        self.tab_eps.setHorizontalHeaderItem(5, ite_perimeter)  # Columna 6

    def __launch_events(self):
        self.ite_register_response.triggered.connect(self.__register_response)
        self.ite_list_info_response.triggered.connect(self.__info_response)
        self.ite_init_user.triggered.connect(self.__inti_user)
        self.ite_show_credits.triggered.connect(self.__credit)
        self.ite_exit.triggered.connect(self.exit)
        self.but_search_code.clicked.connect(self.__show_by_code)
        self.but_search_id.clicked.connect(self.__show_by_id)
        self.but_search_state.clicked.connect(self.__show_by_state)
        self.but_register.clicked.connect(self.__register_response)

    def __info_response(self):
        self.__window_info_response.init_window()
        self.__window_info_response.setVisible(True)

    def exit(self):
        self.close()

    def __credit(self):
       self.__window_credits.setVisible(True)

    def __inti_user(self):
        self.__window_main_client.setVisible(True)

    def __show_by_code(self):
        self.tab_eps.setRowCount(0)
        if self.tex_code.text() != "":
            code = self.tex_code.text()
            suggestions = self.__vector_claim_suggestions.search_by_code(code)

            if suggestions is not None:

                type = suggestions.type()
                date = suggestions.date()
                hour = suggestions.hour()
                description = suggestions.description()
                state = suggestions.state()

                ite_type = QTableWidgetItem(str(type))
                ite_code = QTableWidgetItem(str(code))
                ite_date = QTableWidgetItem(str(date))
                ite_hour = QTableWidgetItem(str(hour))
                ite_description = QTableWidgetItem(str(description))
                ite_state = QTableWidgetItem(str(state))

                self.tab_eps.insertRow(self.tab_eps.rowCount())
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 0, ite_type)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 1, ite_code)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 2, ite_date)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 3, ite_hour)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 4, ite_description)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 5, ite_state)
            else:
                QMessageBox.information(self,"Buzón de comentarios","No existe sugestión con ese código",QMessageBox.Ok,)
        else:
            QMessageBox.information(self,"Buzón de comentarios","Escriba un código",QMessageBox.Ok,)

    def __show_by_id(self):
        self.tab_eps.setRowCount(0)
        if self.tex_id.text() != "":
            id = self.tex_id.text()
            suggestions = self.__vector_claim_suggestions.search_by_id(id)

            if suggestions is not None:
                type = suggestions.type()
                code = suggestions.code()
                date = suggestions.date()
                hour = suggestions.hour()
                description = suggestions.description()
                state = suggestions.state()

                ite_type = QTableWidgetItem(str(type))
                ite_code = QTableWidgetItem(str(code))
                ite_date = QTableWidgetItem(str(date))
                ite_hour = QTableWidgetItem(str(hour))
                ite_description = QTableWidgetItem(str(description))
                ite_state = QTableWidgetItem(str(state))

                self.tab_eps.insertRow(self.tab_eps.rowCount())
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 0, ite_type)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 1, ite_code)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 2, ite_date)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 3, ite_hour)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 4, ite_description)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 5, ite_state)
            else:
                QMessageBox.information(self,"Buzón de comentarios","No existe sugestión con ese código",QMessageBox.Ok,)
        else:
            QMessageBox.information(self,"Buzón de comentarios","Escriba un código",QMessageBox.Ok,)

    def __show_by_state(self):
        self.tab_eps.setRowCount(0)

        state = self.com_state.currentText()
        list_state = self.__vector_claim_suggestions.search_by_state(state)

        if list_state.size() > 0:
            i = list_state.front()
            while i != None:
                type = i.value.type()
                code = i.value.code()
                date = i.value.date()
                hour = i.value.hour()
                description = i.value.description()
                state = i.value.state()

                ite_type = QTableWidgetItem(str(type))
                ite_code = QTableWidgetItem(str(code))
                ite_date = QTableWidgetItem(str(date))
                ite_hour = QTableWidgetItem(str(hour))
                ite_description = QTableWidgetItem(str(description))
                ite_state = QTableWidgetItem(str(state))

                self.tab_eps.insertRow(self.tab_eps.rowCount())
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 0, ite_type)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 1, ite_code)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 2, ite_date)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 3, ite_hour)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 4, ite_description)
                self.tab_eps.setItem(self.tab_eps.rowCount() - 1, 5, ite_state)

                i = i.next
        else:
            QMessageBox.information(self,"Buzón de comentarios","No existe sugestión con ese tipo",QMessageBox.Ok,)

    def __register_response(self):
        self.__window_register_response.init_window()
        self.__window_register_response.setVisible(True)

    def __save_file(self):
        self.__vector_claim_suggestions.save_file_claim_suggestions()
        self.__vector_user.save_file_claim_suggestions()

    def open_file(self):
        self.__vector_claim_suggestions.load_file_claim_suggestions()
        self.__vector_user.load_file_claim_suggestions()

    def closeEvent(self, event):
        response = QMessageBox.question(self,"Gestor EPS","¿Esta seguro que desea salir?",QMessageBox.Yes,QMessageBox.No,)

        if response == 16384:
            event.accept()
            self.__save_file()
        else:
            event.ignore()