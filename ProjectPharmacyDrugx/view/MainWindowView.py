from PyQt5.QtWidgets import QMainWindow
from controller.ListPharmacy import ListPharmacy 
from view.CreditsView import CreditsView
from view.RegisterBuysView import RegisterBuysView
from view.RegisterMedicineView import RegisterMedicineView
from view.RegisterSaleView import RegisterSaleView
from view.ReportMedicineView import ReportMedicineView



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__vector_pharmacy = ListPharmacy()
        self.__window_register_medicine = RegisterMedicineView(self.__vector_pharmacy)
        self.__window_register_buys = RegisterBuysView(self.__vector_pharmacy)
        self.__window_register_sale = RegisterSaleView(self.__vector_pharmacy)
        self.__window_report_medicine = ReportMedicineView(self.__vector_pharmacy)
        self.__window_credits = CreditsView()
        

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        pass

    def __launch_Events(self):
        pass

    def __register_medicine(self):
        self.__window_register_medicine.initWindow()
        self.__window_register_medicine.setVisible(True)

    def __register_buys(self):
        self.__window_register_buys.initWindow()
        self.__window_register_buys.setVisible(True)

    def __register_sale(self):
        self.__window_register_sale.initWindow()
        self.__window_register_sale.setVisible(True)

    def __report_medicine(self):
        self.__window_report_medicine.initWindow()
        self.__window_report_medicine.setVisible(True)

    def __show_medicine(self):
        pass

    def __show_credits(self):
        self.__window_credits.setVisible(True)

    def __exit(self):
        pass

    def closeEvent(self, event):
        event.accept()
