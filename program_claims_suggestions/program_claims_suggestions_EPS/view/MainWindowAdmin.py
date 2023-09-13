from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QColor, QIcon, QPixmap
from PyQt5.QtWidgets import *
from component.QlabelClicked import QLabelClickable
from component.StyleWidget import StyleWidget
from controller.ListSuggestion import ListSuggestion
from controller.ListUser import ListUser
from view.CreditsView import CreditsView
from view.DetailView import DetailView
from view.ListSuggestionView import ListSuggestionView
from view.ListUserView import ListUserView
from view.ReplySuggestionView import ReplySuggestionView




class MainWindowAdmin(QDialog):

    def __init__(self, list_suggestions, list_User):
        super().__init__()
        self.__list_suggestions = list_suggestions
        self.__list_User = list_User

        self.__window_list_suggestion = ListSuggestionView(self.__list_suggestions, self.__list_User)
        self.__window_list_user = ListUserView( self.__list_User)
        self.__window_register_answer = ReplySuggestionView(list_suggestions, list_User)
        self.__window_detail = DetailView(self.__list_suggestions, self.__list_User)
        

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Administración")
        self.resize(760, 515)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setMinimumSize(QSize(760, 515))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.__styleWidget = StyleWidget("Comic Sans MS")
        style = self.__styleWidget.styleMainWindow("green")

        canvas = QPixmap("images/fondoMenu.png")
        self.lab_background = QLabel(self)
        self.lab_background.setGeometry(QRect(0, 0, 760, 515))
        self.lab_background.setPixmap(canvas)

        # obtener barra de menú
        bar_menu = QMenuBar(self)
        style += self.__styleWidget.styleBar("green","white")
        # Adiciona opción al menú "&" sirve para dar acceso rápido
        menu_file = bar_menu.addMenu("&sugestión")

        # Crear Item de un menú
        self.ite_reply_suggestion = QAction("&Responder sugestión", self)
        self.ite_search_sugerencia = QAction("&Detalle sugestión", self)
        self.ite_list_sugerencia = QAction("&Listado de sugestión", self)
        self.ite_list_user = QAction("&listado de usuario", self)

        # Agregar Ícono al Item del menú
        self.ite_reply_suggestion.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon)
        )
        self.ite_search_sugerencia.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogListView)
        )

        self.ite_list_sugerencia.setIcon(self.style().standardIcon(QStyle.SP_FileDialogBack))
        self.ite_list_user.setIcon(
            self.style().standardIcon(QStyle.SP_MessageBoxInformation)
        )

        # agregar un short cut (acceso rápido)
        self.ite_reply_suggestion.setShortcut("CTRL+R")
        self.ite_search_sugerencia.setShortcut("CTRL+L")
        self.ite_list_sugerencia.setShortcut("CTRL+E")
        self.ite_list_user.setShortcut("CTRL+S")

        # agregar item al menú
        menu_file.addAction(self.ite_reply_suggestion)
        menu_file.addAction(self.ite_search_sugerencia)
        menu_file.addSeparator()
        menu_file.addAction(self.ite_list_sugerencia)
        menu_file.addAction(self.ite_list_user)

        canvas = QPixmap("images/back.png")
        self.lab_back = QLabelClickable(self)
        self.lab_back.setGeometry(QRect(39, 25, 32, 32))
        self.lab_back.setPixmap(canvas)
        self.lab_back.setObjectName("back")
        # style += self.__styleWidget.styleLabelBorderHover("back","green",16)

        canvas = QPixmap("images/reply.png")
        self.lab_reply = QLabelClickable(self)
        self.lab_reply.setGeometry(QRect(204, 88, 130, 130))
        self.lab_reply.setPixmap(canvas)
        self.lab_reply.setObjectName("reply")
        style += self.__styleWidget.styleLabelBorderHover("reply","green",16)

        canvas = QPixmap("images/detail.png")
        self.lab_detail = QLabelClickable(self)
        self.lab_detail.setGeometry(QRect(426, 88, 130, 130))
        self.lab_detail.setPixmap(canvas)
        self.lab_detail.setObjectName("detail")
        style += self.__styleWidget.styleLabelBorderHover("detail","green",16)

        canvas = QPixmap("images/list.png")
        self.lab_list_sugerencia = QLabelClickable(self)
        self.lab_list_sugerencia.setGeometry(QRect(204, 259, 130, 130))
        self.lab_list_sugerencia.setPixmap(canvas)
        self.lab_list_sugerencia.setObjectName("list_sug")
        style += self.__styleWidget.styleLabelBorderHover("list_sug","green",16)

        canvas = QPixmap("images/list_user.png")
        self.lab_list_user = QLabelClickable(self)
        self.lab_list_user.setGeometry(QRect(426, 259, 130, 130))
        self.lab_list_user.setPixmap(canvas)
        self.lab_list_user.setObjectName("user")
        style += self.__styleWidget.styleLabelBorderHover("user","green",16)

        self.lab_reply1 = QLabel(self)
        self.lab_reply1.setText("Responder sugestión")
        self.lab_reply1.setGeometry(QRect(174, 218, 185, 25))
        self.lab_reply1.setObjectName("reply1")
        style += self.__styleWidget.styleLabel("reply1","green","lightgreen",17,"bold")

        self.lab_detail1 = QLabel(self)
        self.lab_detail1.setText("Detalle sugestión")
        self.lab_detail1.setGeometry(QRect(411, 218, 170, 25))
        self.lab_detail1.setObjectName("detail1")
        style += self.__styleWidget.styleLabel("detail1","green","lightgreen",17,"bold")

        self.lab_list_sug = QLabel(self)
        self.lab_list_sug.setText("Listado de sugestión")
        self.lab_list_sug.setGeometry(QRect(178, 390, 177, 25))
        self.lab_list_sug.setObjectName("list_sug1")
        style += self.__styleWidget.styleLabel("list_sug1","green","lightgreen",17,"bold")

        self.lab_list_use = QLabel(self)
        self.lab_list_use.setText("Listado usuario")
        self.lab_list_use.setGeometry(QRect(435, 390, 138, 25))
        self.lab_list_use.setObjectName("list_use1")
        style += self.__styleWidget.styleLabel("list_use1","green","lightgreen",17,"bold")

        self.lab_portal = QLabel(self)
        self.lab_portal.setText("Portal de sugestión")
        self.lab_portal.setGeometry(QRect(235, 25, 300, 42))
        self.lab_portal.setObjectName("portal")
        self.lab_portal.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLabel("portal","green","lightgreen",28,"bold")

        self.setStyleSheet(str(style))


    def __launch_Events(self):
        self.ite_reply_suggestion.triggered.connect(self.__register_answer)
        self.ite_search_sugerencia.triggered.connect(self.__detail_suggestion)
        self.ite_list_sugerencia.triggered.connect(self.__show_list_suggestion)
        self.ite_list_user.triggered.connect(self.__show_list_users)
        self.lab_list_sugerencia.clicked.connect(self.__show_list_suggestion)
        self.lab_detail.clicked.connect(self.__detail_suggestion)
        self.lab_list_user.clicked.connect(self.__show_list_users)
        self.lab_reply.clicked.connect(self.__register_answer)
        self.lab_back.clicked.connect(self.__back)

    def __register_answer(self):
        self.__window_register_answer.setVisible(True)
        self.__window_register_answer.init_window()

    def __detail_suggestion(self):
        self.__window_detail.init_window()
        self.__window_detail.setVisible(True)

    def __show_list_suggestion(self):
        self.__window_list_suggestion.init_window()
        self.__window_list_suggestion.setVisible(True)

    def __show_list_users(self):
        self.__window_list_user.init_window()
        self.__window_list_user.setVisible(True)
    
    def __back(self):
        self.setVisible(False)
