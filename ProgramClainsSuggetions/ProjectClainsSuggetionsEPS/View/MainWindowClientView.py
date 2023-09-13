from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton
from View.RegisterClaimSuggestionsView import RegisterClaimSuggestionsView
from View.RegisterResponseView import RegisterResponseView
from View.RegisterUserView import RegisterUserView
from controller.ListClaimSuggestions import ListClaimSuggestions


class MainWindowClientView(QDialog):
    
    def __init__(self, vector_claim_suggestions, vector_user):
        super().__init__()# Constructor de la clase
        # Se separa memoria para arreglo de polígonos (UNA SOLA VEZ EN EL PROGRAMA)
        self.__vector_claim_suggestions = vector_claim_suggestions
        self.__vector_user = vector_user

        self.__window_register_user = RegisterUserView(self.__vector_user)
        self.__window_register_claim_suggestions = RegisterClaimSuggestionsView(self.__vector_claim_suggestions, self.__vector_user)
        
        # self.__Credits = CreditsView()

        self.__launch_widgets()
        self.__launch_events()

    def __launch_widgets(self):
        self.setWindowTitle("Bienvenidos a EPS los Angeles")
        self.setFixedSize(1024, 768)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        

        self.but_register_user = QPushButton(self)
        self.but_register_claim = QPushButton(self)

        self.but_register_user.setText("Registrar Usuario ")
        self.but_register_user.setGeometry(QRect(122, 40, 159, 52))
        self.but_register_claim.setText("Buzón quejas o sugerencia  ")
        self.but_register_claim.setGeometry(QRect(330, 40, 236, 52))

        self.lab_logo = QLabel(self)
        self.lab_logo.setGeometry(QRect(50, 80, 1024, 658))
        canvas = QPixmap("images/fondo.jpg")
        self.lab_logo.setPixmap(canvas)

    def __launch_events(self):
        self.but_register_user.clicked.connect(self.__register_user)
        self.but_register_claim.clicked.connect(self.__register_claim)

    def __register_user(self):
        self.__window_register_user.init_window()
        self.__window_register_user.setVisible(True)

    def __register_claim(self):
        self.__window_register_claim_suggestions.init_window()
        self.__window_register_claim_suggestions.setVisible(True)
