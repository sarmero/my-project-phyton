from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QColor, QIcon, QPixmap
from PyQt5.QtWidgets import *
from component.QlabelClicked import QLabelClickable
from component.StyleWidget import StyleWidget
from controller.ListSuggestion import ListSuggestion
from controller.ListUser import ListUser
from view.ProfileView import ProfileView
from view.RegisterSuggestionView import RegisterSuggestionView
from view.RegisterUserView import RegisterUserView
from view.AnswerView import AnswerView




class MainWindowUser(QDialog):
    def __init__(self,list_suggestions, list_User):
        super().__init__()
        self.__list_suggestions = list_suggestions
        self.__list_User = list_User

        self.window_register_suggestion = RegisterSuggestionView(self.__list_suggestions, self.__list_User)
        self.window_register_user = RegisterUserView( self.__list_User)
        self.window_answer = AnswerView(list_suggestions, list_User)
        self.Window_profile = ProfileView(self.__list_User)
        

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Usuarios")
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
        menu_file = QMenu("&Usuarios",self)
        bar_menu.addMenu(menu_file)

        # Crear Item de un menú
        self.ite_register_suggestion = QAction("&Administración", self)
        self.ite_register_users = QAction("&Usuarios", self)
        self.ite_response = QAction("&Respuesta", self)
        self.ite_profile = QAction("&Perfil", self)

        # Agregar Ícono al Item del menú
        self.ite_register_suggestion.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon)
        )
        self.ite_register_users.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogListView)
        )

        self.ite_response.setIcon(self.style().standardIcon(QStyle.SP_FileDialogBack))
        self.ite_profile.setIcon(
            self.style().standardIcon(QStyle.SP_MessageBoxInformation)
        )

        # agregar un short cut (acceso rápido)
        self.ite_register_suggestion.setShortcut("CTRL+R")
        self.ite_register_users.setShortcut("CTRL+L")
        self.ite_response.setShortcut("CTRL+E")
        self.ite_profile.setShortcut("CTRL+S")

        # agregar item al menú
        menu_file.addAction(self.ite_register_suggestion)
        menu_file.addAction(self.ite_register_users)
        menu_file.addAction(self.ite_response)
        menu_file.addAction(self.ite_profile)

        canvas = QPixmap("images/back.png")
        self.lab_back = QLabelClickable(self)
        self.lab_back.setGeometry(QRect(39, 25, 32, 32))
        self.lab_back.setPixmap(canvas)
        self.lab_back.setObjectName("back")
        # style += self.__styleWidget.styleLabelBorderHover("back","green",16)

        canvas = QPixmap("images/register_sug.png")
        self.lab_register_suggestions = QLabelClickable(self)
        self.lab_register_suggestions.setGeometry(QRect(204, 88, 130, 130))
        self.lab_register_suggestions.setPixmap(canvas)
        self.lab_register_suggestions.setObjectName("admin")
        style += self.__styleWidget.styleLabelBorderHover("admin","green",16)

        canvas = QPixmap("images/register_user.png")
        self.lab_register_user = QLabelClickable(self)
        self.lab_register_user.setGeometry(QRect(426, 88, 130, 130))
        self.lab_register_user.setPixmap(canvas)
        self.lab_register_user.setObjectName("suggestions")
        style += self.__styleWidget.styleLabelBorderHover("suggestions","green",16)

        canvas = QPixmap("images/answer.png")
        self.lab_answer = QLabelClickable(self)
        self.lab_answer.setGeometry(QRect(204, 259, 130, 130))
        self.lab_answer.setPixmap(canvas)
        self.lab_answer.setObjectName("response")
        style += self.__styleWidget.styleLabelBorderHover("response","green",16)

        canvas = QPixmap("images/profile.png")
        self.lab_profile = QLabelClickable(self)
        self.lab_profile.setGeometry(QRect(426, 259, 130, 130))
        self.lab_profile.setPixmap(canvas)
        self.lab_profile.setObjectName("profile")
        style += self.__styleWidget.styleLabelBorderHover("profile","green",16)

        self.lab_register_suggestions1 = QLabel(self)
        self.lab_register_suggestions1.setText("Realizar sugerencia")
        self.lab_register_suggestions1.setGeometry(QRect(183, 218, 172, 25))
        self.lab_register_suggestions1.setObjectName("admin1")
        style += self.__styleWidget.styleLabel("admin1","green","lightgreen",17,"bold")

        self.lab_register_user1 = QLabel(self)
        self.lab_register_user1.setText("Registrarse")
        self.lab_register_user1.setGeometry(QRect(443, 218, 140, 25))
        self.lab_register_user1.setObjectName("register_user1")
        style += self.__styleWidget.styleLabel("register_user1","green","lightgreen",17,"bold")

        self.lab_answer1 = QLabel(self)
        self.lab_answer1.setText("Respuesta")
        self.lab_answer1.setGeometry(QRect(227, 390, 83, 25))
        self.lab_answer1.setObjectName("response1")
        style += self.__styleWidget.styleLabel("response1","green","lightgreen",17,"bold")

        self.lab_profile1 = QLabel(self)
        self.lab_profile1.setText("Perfil")
        self.lab_profile1.setGeometry(QRect(470, 390, 50, 25))
        self.lab_profile1.setObjectName("profile1")
        style += self.__styleWidget.styleLabel("profile1","green","lightgreen",17,"bold")

        self.lab_portal = QLabel(self)
        self.lab_portal.setText("Portal de usuarios")
        self.lab_portal.setGeometry(QRect(261, 25, 250, 36))
        self.lab_portal.setObjectName("portal")
        self.lab_portal.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLabel("portal","green","lightgreen",28,"bold")

        text = "El propósito de NUEVA EPS es la protección integral de la salud de nuestros afiliados,"
        text +="\nrazón por la cual nos enfocamos nen gestionar sus riesgos, con un alto compromiso en"
        text +="\nprevenir, mantener o mejorar sus condiciones de bienestar y la de su grupo familiar."

        
        self.lab_message = QLabel(self)
        self.lab_message.setText(text)
        self.lab_message.setGeometry(QRect(104, 438, 543, 61))
        self.lab_message.setObjectName("message")
        self.lab_message.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLabel("message","black","green",12,"")

        self.setStyleSheet(str(style))


    def __launch_Events(self):
        # Conectar el método a el evento clic de un item del menú
        self.ite_register_suggestion.triggered.connect(self.__register_suggestion)
        self.ite_register_users.triggered.connect(self.__register_user)
        self.ite_response.triggered.connect(self.__answer)
        self.ite_profile.triggered.connect(self.__show_profile)
        self.lab_answer.clicked.connect(self.__answer)
        self.lab_register_suggestions.clicked.connect(self.__register_suggestion)
        self.lab_register_user.clicked.connect(self.__register_user)
        self.lab_profile.clicked.connect(self.__show_profile)
        self.lab_back.clicked.connect(self.__back)


    def __register_suggestion(self):
        self.window_register_suggestion.init_window()
        self.window_register_suggestion.setVisible(True)

    def __register_user(self):
        self.window_register_user.init_window()
        self.window_register_user.setVisible(True)

    def __show_profile(self):
        self.Window_profile.init_window()
        self.Window_profile.setVisible(True)

    def __answer(self):
        self.window_answer.init_window()
        self.window_answer.setVisible(True)

    def __back(self):
        self.setVisible(False)

