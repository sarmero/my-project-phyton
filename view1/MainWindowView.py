from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import *
from component.StyleWidget import StyleWidget

from controller.ListSuggestion import ListSuggestion
from controller.ListUser import ListUser
from view.CreditsView import CreditsView
from view.ListSuggestionView import ListPccsView
from view.RegisterSuggestionView import RegisterSuggestionView
from view.RegisterUserView import RegisterUserView
from view.ReplyView import ReplyView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__vector_pccs = ListSuggestion()
        self.__vector_user = ListUser()
        self.__window_Register_pccs = RegisterSuggestionView(self.__vector_pccs)
        self.__window_list_pccs = ListPccsView(self.__vector_pccs)
        self.__window_register_user = RegisterUserView(self.__vector_user)
        self.__window_credits = CreditsView()
        self.__styleWidget = StyleWidget()
        self.__window_reply = ReplyView(self.__vector_pccs)

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Gestor de EPS")
        self.resize(500, 420)
        self.setWindowIcon(QIcon("icon.png"))
        self.generalLayout = QHBoxLayout()
        self.gridLayout = QGridLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self.setMinimumSize(QSize(500, 420))
        style = self.__styleWidget.styleMainWindow("#13293d")
        # obtener barra de menú
        bar_menu = self.menuBar()
        style += self.__styleWidget.styleBar("orange")
        # Adiciona opción al menú "&" sirve para dar acceso rápido
        menu_file = bar_menu.addMenu("&Petición")
        menu_help = bar_menu.addMenu("&Ayuda")

        # Crear Item de un menú
        self.ite_register_petition = QAction("&Registrar petición", self)
        self.ite_list_petition = QAction("&Lista de petición", self)
        self.ite_register_user = QAction("&Registrar usuario", self)
        self.ite_exit = QAction("&Salir", self)
        self.ite_show_credits = QAction("&Créditos", self)

        # Agregar Ícono al Item del menú
        self.ite_register_petition.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon)
        )
        self.ite_list_petition.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogListView)
        )
        self.ite_register_user.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogDetailedView)
        )
        self.ite_exit.setIcon(self.style().standardIcon(QStyle.SP_FileDialogBack))
        self.ite_show_credits.setIcon(
            self.style().standardIcon(QStyle.SP_MessageBoxInformation)
        )

        # agregar un short cut (acceso rápido)
        self.ite_register_petition.setShortcut("CTRL+R")
        self.ite_list_petition.setShortcut("CTRL+L")
        self.ite_exit.setShortcut("CTRL+E")
        self.ite_show_credits.setShortcut("CTRL+S")

        # agregar item al menú
        menu_file.addAction(self.ite_register_petition)
        menu_file.addAction(self.ite_list_petition)
        menu_file.addSeparator()
        menu_file.addAction(self.ite_register_user)
        menu_file.addSeparator()
        menu_file.addAction(self.ite_exit)
        menu_help.addAction(self.ite_show_credits)

        self.lab_code = QLabel(self)
        self.lab_code.setText("Código: ")
        self.lab_code.setObjectName("labelCode")
        self.lab_code.setGeometry(QRect(100, 35, 45, 25))
        style += self.__styleWidget.styleLabel("labelCode", "orange", "blue", "Arial", 12, "bold")

        self.tex_code = QLineEdit(self)
        self.tex_code.setGeometry(QRect(155, 35, 150, 25))
        self.tex_code.setObjectName("texCode")
        style += self.__styleWidget.styleLine("texCode", "Arial", 12)

        self.but_search = QPushButton(self)
        self.but_search.setText("Buscar")
        self.but_search.setGeometry(QRect(310, 35, 75, 25))
        self.but_search.setObjectName("buttonSearch")
        style += self.__styleWidget.styleButton("buttonSearch", "#4e91Cd", "white", "Arial", 13, "bold", 12)

        self.lab_code2 = QLabel(self)
        self.lab_code2.setText("Código: ")
        self.lab_code2.setObjectName("labelCode2")
        self.lab_code2.setGeometry(QRect(25, 65, 45, 25))
        style += self.__styleWidget.styleLabel("labelCode2", "#4e91Cd", "white", "Arial", 13, "bold")

        self.lab_code_edit = QLabel(self)
        self.lab_code_edit.setText("210478")
        self.lab_code_edit.setObjectName("labelCode3")
        self.lab_code_edit.setGeometry(QRect(75, 65, 50, 25))
        style += self.__styleWidget.styleLabel(
            "labelCode3", "orange", "White", "Arial", 13, ""
        )

        self.lab_guy = QLabel(self)
        self.lab_guy.setText("Tipo: ")
        self.lab_guy.setObjectName("labelGuy")
        self.lab_guy.setGeometry(QRect(125, 65, 30, 25))
        style += self.__styleWidget.styleLabel(
            "labelGuy", "#4e91Cd", "white", "Arial", 13, "bold"
        )

        self.lab_guy_edit = QLabel(self)
        self.lab_guy_edit.setText("Sugerencia")
        self.lab_guy_edit.setObjectName("labelGuy2")
        self.lab_guy_edit.setGeometry(QRect(160, 65, 70, 25))
        style += self.__styleWidget.styleLabel(
            "labelGuy2", "orange", "White", "Arial", 13, ""
        )

        self.lab_state = QLabel(self)
        self.lab_state.setText("Estado: ")
        self.lab_state.setObjectName("labelState")
        self.lab_state.setGeometry(QRect(240, 65, 45, 25))
        style += self.__styleWidget.styleLabel(
            "labelState", "#4e91Cd", "white", "Arial", 13, "bold"
        )

        self.lab_state_edit = QLabel(self)
        self.lab_state_edit.setText("Pendiente")
        self.lab_state_edit.setObjectName("labelState2")
        self.lab_state_edit.setGeometry(QRect(290, 65, 70, 25))
        style += self.__styleWidget.styleLabel(
            "labelState2", "orange", "White", "Arial", 13, ""
        )

        self.lab_date = QLabel(self)
        self.lab_date.setText("Fecha: ")
        self.lab_date.setObjectName("labelDate")
        self.lab_date.setGeometry(QRect(360, 65, 40, 25))
        style += self.__styleWidget.styleLabel(
            "labelDate", "#4e91Cd", "white", "Arial", 13, "bold"
        )

        self.lab_date_edit = QLabel(self)
        self.lab_date_edit.setText("06/01/2023")
        self.lab_date_edit.setObjectName("labelDate2")
        self.lab_date_edit.setGeometry(QRect(400, 65, 70, 25))
        style += self.__styleWidget.styleLabel(
            "labelDate2", "orange", "White", "Arial", 13, ""
        )

        self.lab_id = QLabel(self)
        self.lab_id.setText("Identificación: ")
        self.lab_id.setObjectName("labelId")
        self.lab_id.setGeometry(QRect(65, 90, 80, 25))
        style += self.__styleWidget.styleLabel(
            "labelId", "#4e91Cd", "white", "Arial", 13, "bold"
        )

        self.lab_id_edit = QLabel(self)
        self.lab_id_edit.setText("1087205878")
        self.lab_id_edit.setObjectName("labelId2")
        self.lab_id_edit.setGeometry(QRect(150, 90, 90, 25))
        style += self.__styleWidget.styleLabel(
            "labelId2", "orange", "White", "Arial", 13, ""
        )

        self.lab_user = QLabel(self)
        self.lab_user.setText("Usuario: ")
        self.lab_user.setObjectName("labelUser")
        self.lab_user.setGeometry(QRect(230, 90, 50, 25))
        style += self.__styleWidget.styleLabel(
            "labelUser", "#4e91Cd", "white", "Arial", 13, "bold"
        )

        self.lab_user_edit = QLabel(self)
        self.lab_user_edit.setText("Juan Andres Perez Hurtado")
        self.lab_user_edit.setObjectName("labelUser2")
        self.lab_user_edit.setGeometry(QRect(285, 90, 200, 25))
        style += self.__styleWidget.styleLabel(
            "labelUser2", "orange", "White", "Arial", 13, ""
        )

        self.lab_description = QLabel(self)
        self.lab_description.setText("Descripción")
        self.lab_description.setGeometry(QRect(25, 120, 90, 25))
        self.lab_description.setObjectName("labelDescription")
        style += self.__styleWidget.styleLabel(
            "labelDescription", "orange", "blue", "Arial", 13, "bold"
        )

        self.tex_area_description = QPlainTextEdit(self)
        self.tex_area_description.move(25, 145)
        self.tex_area_description.resize(450, 225)

        self.but_reply = QPushButton(self)
        self.but_reply.setText("Responder")
        self.but_reply.setGeometry(QRect(190, 380, 120, 30))
        self.but_reply.setObjectName("buttonReply")
        style += self.__styleWidget.styleButton(
            "buttonReply", "orange", "#13293d", "Arial", 12, "bold", 15
        )

        self.setStyleSheet(str(style))

    def __launch_Events(self):
        # Conectar el método a el evento clic de un item del menú

        self.ite_register_petition.triggered.connect(self.__register_petition)
        self.ite_list_petition.triggered.connect(self.__List__petition)
        self.ite_register_user.triggered.connect(self.__register_user)
        self.ite_exit.triggered.connect(self.__exit)
        self.ite_show_credits.triggered.connect(self.__credits)
        self.but_reply.clicked.connect(self.__reply_pccs)

    def __reply_pccs(self):
        self.__window_reply.setVisible(True)

    def __register_petition(self):
        self.__window_Register_pccs.setVisible(True)

    def __List__petition(self):
        self.__window_list_pccs.setVisible(True)

    def __register_user(self):
        self.__window_register_user.initWindow()
        self.__window_register_user.setVisible(True)

    def __credits(self):
        self.__window_credits.setVisible(True)

    def __exit(self):
        pass

    def open_file(self):
        self.__vector_pccs.load_list()
    
    def save_file(self):
        self.__vector_pccs.save_list()

    def closeEvent(self, event):
        self.save_file()
        event.accept()
