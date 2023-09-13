import datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRect, QSize, QTime, QTimer, Qt, pyqtSignal
from PyQt5.QtGui import QColor, QIcon, QPixmap
from PyQt5.QtWidgets import *
from component.QlabelClicked import QLabelClickable
from component.StyleWidget import StyleWidget
from controller.ListSuggestion import ListSuggestion
from controller.ListUser import ListUser
from view.MainWindowAdmin import MainWindowAdmin
from view.MainWindowUser import MainWindowUser
from view.CreditsView import CreditsView




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__list_suggestions = ListSuggestion()
        self.__list_User = ListUser()

        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(60000)

        self.window_suggestion = MainWindowAdmin(self.__list_suggestions, self.__list_User)
        self.window_user = MainWindowUser(self.__list_suggestions, self.__list_User)
        self.window_credits = CreditsView()
        

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Benavides EPS")
        self.setFixedSize(760, 515)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setMinimumSize(QSize(760, 515))

        self.__styleWidget = StyleWidget("Comic Sans MS")
        style = self.__styleWidget.styleMainWindow("green")

        canvas = QPixmap("images/fondoMenu.png")
        self.lab_background = QLabel(self)
        self.lab_background.setGeometry(QRect(0, 0, 760, 515))
        self.lab_background.setPixmap(canvas)

        # obtener barra de menú
        bar_menu = self.menuBar()
        style += self.__styleWidget.styleBar("green","white")
        # Adiciona opción al menú "&" sirve para dar acceso rápido
        menu_file = bar_menu.addMenu("&EPS")
        menu_help = bar_menu.addMenu("&Ayuda")

        # Crear Item de un menú
        self.ite_init_admin = QAction("&Administración", self)
        self.ite_init_user = QAction("&Usuarios", self)
        self.ite_exit = QAction("&Salir", self)
        self.ite_show_credits = QAction("&Créditos", self)
        

        # Agregar Ícono al Item del menú
        self.ite_init_admin.setIcon(
            self.style().standardIcon(QStyle.SP_FileIcon)
        )
        self.ite_init_user.setIcon(
            self.style().standardIcon(QStyle.SP_FileDialogListView)
        )

        self.ite_exit.setIcon(self.style().standardIcon(QStyle.SP_FileDialogBack))
        self.ite_show_credits.setIcon(
            self.style().standardIcon(QStyle.SP_MessageBoxInformation)
        )

        # agregar un short cut (acceso rápido)
        self.ite_init_admin.setShortcut("CTRL+R")
        self.ite_init_user.setShortcut("CTRL+L")
        self.ite_exit.setShortcut("CTRL+E")
        self.ite_show_credits.setShortcut("CTRL+S")
        style += self.__styleWidget.styleMenu("","green")

        # agregar item al menú
        menu_file.addAction(self.ite_init_admin)
        menu_file.addAction(self.ite_init_user)
        menu_file.addSeparator()
        menu_file.addAction(self.ite_exit)
        menu_help.addAction(self.ite_show_credits)

        canvas = QPixmap("images/admin.png")
        self.lab_admin =  QLabelClickable(self)
        self.lab_admin.setGeometry(QRect(204, 88, 130, 130))
        self.lab_admin.setPixmap(canvas)
        self.lab_admin.setObjectName("admin")
        style += self.__styleWidget.styleLabelBorderHover("admin","green",16)

        canvas = QPixmap("images/user.png")
        self.lab_user = QLabelClickable(self)
        self.lab_user.setGeometry(QRect(426, 88, 130, 130))
        self.lab_user.setPixmap(canvas)
        self.lab_user.setObjectName("user")
        style += self.__styleWidget.styleLabelBorderHover("user","green",16)

        canvas = QPixmap("images/exit.png")
        self.lab_exit = QLabelClickable(self)
        self.lab_exit.setGeometry(QRect(204, 259, 130, 130))
        self.lab_exit.setPixmap(canvas)
        self.lab_exit.setObjectName("exit")
        self.lab_exit.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        style += self.__styleWidget.styleLabelBorderHover("exit","green",16)

        canvas = QPixmap("images/credit.png")
        self.lab_credit = QLabelClickable(self)
        self.lab_credit.setGeometry(QRect(426, 259, 130, 130))
        self.lab_credit.setPixmap(canvas)
        self.lab_credit.setObjectName("credit")
        self.lab_credit.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        style += self.__styleWidget.styleLabelBorderHover("credit","green",16)

        self.lab_admin1 = QLabel(self)
        self.lab_admin1.setText("Administración")
        self.lab_admin1.setGeometry(QRect(211, 218, 128, 25))
        self.lab_admin1.setObjectName("admin1")
        style += self.__styleWidget.styleLabel("admin1","green","lightgreen",17,"bold")

        self.lab_user1 = QLabel(self)
        self.lab_user1.setText("Usuarios")
        self.lab_user1.setGeometry(QRect(464, 218, 70, 25))
        self.lab_user1.setObjectName("user1")
        style += self.__styleWidget.styleLabel("user1","green","lightgreen",17,"bold")

        self.lab_exit1 = QLabel(self)
        self.lab_exit1.setText("Salir")
        self.lab_exit1.setGeometry(QRect(245, 390, 49, 25))
        self.lab_exit1.setObjectName("exit1")
        style += self.__styleWidget.styleLabel("exit1","green","lightgreen",17,"bold")

        self.lab_credit1 = QLabel(self)
        self.lab_credit1.setText("Créditos")
        self.lab_credit1.setGeometry(QRect(466, 390, 76, 25))
        self.lab_credit1.setObjectName("credit1")
        style += self.__styleWidget.styleLabel("credit1","green","lightgreen",17,"bold")

        self.lab_hour = QLabel(self)
        self.lab_hour.setText("10:50")
        self.lab_hour.setGeometry(QRect(346, 20, 70, 36))
        self.lab_hour.setObjectName("hour")
        self.lab_hour.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLabel("hour","green","lightgreen",24,"bold")

        self.lab_date = QLabel(self)
        self.lab_date.setText(datetime.datetime.now().strftime('%A, de %d %B de %Y'))
        self.lab_date.setGeometry(QRect(229, 51, 310, 25))
        self.lab_date.setObjectName("date")
        self.lab_date.setAlignment(Qt.AlignHCenter)
        style += self.__styleWidget.styleLabel("date","green","lightgreen",15,"bold")

        self.setStyleSheet(str(style))


    def displayTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm')
        self.lab_hour.setText(displayText)

        if displayText == "00:00":
            self.lab_date.setText(datetime.datetime.now().strftime('%A, de %d %B de %Y'))
        

     
    def __launch_Events(self):
        # Conectar el método a el evento clic de un item del menú
        self.ite_init_admin.triggered.connect(self.__init_admin)
        self.ite_init_user.triggered.connect(self.__init_user)
        self.ite_exit.triggered.connect(self.__exit)
        self.ite_show_credits.triggered.connect(self.__credits)
        self.lab_admin.clicked.connect(self.__init_admin)
        self.lab_user.clicked.connect(self.__init_user)
        self.lab_exit.clicked.connect(self.__exit)
        self.lab_credit.clicked.connect(self.__credits)

    def __init_admin(self):
        self.window_suggestion.setVisible(True)

    def __init_user(self):
        self.window_user.setVisible(True)

    def __credits(self):
        self.window_credits.setVisible(True)

    def __exit(self):
        self.close()

    def __save_file(self):
        self.__list_suggestions.save_list()
        self.__list_User.save_list()
    
    def open_file(self):
        self.__list_suggestions.load_list()
        self.__list_User.load_list()

    def closeEvent(self, event):
        answer = QMessageBox.question(
            self, " Salir ", " Seguro Desea Salir ", QMessageBox.Yes, QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.__save_file()
            event.accept()
        else:
            event.ignore()

