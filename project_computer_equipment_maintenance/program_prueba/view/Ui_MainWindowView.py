# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Archivos\Mis Datos\Udenar\SEXTO SEMESTRE\2022ED\projects\taller2\project_computer_equipment_maintenance\program_prueba\ui\MainWindowView.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.bar_menu = QtWidgets.QMenuBar(MainWindow)
        self.bar_menu.setObjectName("bar_menu")
        self.men_file = QtWidgets.QMenu(self.bar_menu)
        self.men_file.setObjectName("men_file")
        MainWindow.setMenuBar(self.bar_menu)
        self.ite_open = QtWidgets.QAction(MainWindow)
        self.ite_open.setObjectName("ite_open")
        self.ite_save = QtWidgets.QAction(MainWindow)
        self.ite_save.setObjectName("ite_save")
        self.men_file.addAction(self.ite_open)
        self.men_file.addAction(self.ite_save)
        self.bar_menu.addAction(self.men_file.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mantenimiento de equipos de cómputo"))
        self.men_file.setTitle(_translate("MainWindow", "Archivo"))
        self.ite_open.setText(_translate("MainWindow", "Abrir"))
        self.ite_save.setText(_translate("MainWindow", "Guardar"))