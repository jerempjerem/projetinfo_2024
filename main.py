# pyside2-uic ui/logindialog.ui -o ui_logindialog.py
# pyside2-uic ui/mainwindow.ui -o ui_mainwindow.py
# pyrcc5 ressources.qrc -o ressources_rc.py

#MVC

import sys
import globals
from functions import LoginController, MainController
import locale
from datetime import datetime

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget
########################################################################
# IMPORT GUI FILE
from ui_logindialog import *
from ui_mainwindow import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
########################################################################

# Configurer la locale en français
locale.setlocale(locale.LC_TIME, 'fr_FR')

########################################################################
## LOGIN WINDOW CLASS
########################################################################
class LoginDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        
        self.controller = LoginController(self)

        loadJsonStyle(self, self.ui, jsonFiles={"styles/style.json"})
        ########################################################################

        ########################################################################       
        self.ui.loginbtn.clicked.connect(lambda: self.controller.login())
        self.ui.closebtn.clicked.connect(lambda: sys.exit(app.exec_()))
        
        
########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.controller = MainController(self)

        loadJsonStyle(self, self.ui, jsonFiles={"styles/style.json"})
        ########################################################################

        ########################################################################      
        
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        ## Navigations des pages
        self.ui.planningBtn.clicked.connect(lambda: self.ui.stackedplanning.setCurrentIndex(0))
        self.ui.timelineBtn.clicked.connect(lambda: self.ui.stackedplanning.setCurrentIndex(1))
        self.ui.editBtn.clicked.connect(lambda: self.ui.stackedplanning.setCurrentIndex(2))
        
        # Page Planning
        self.ui.planningNextWeekBtn.clicked.connect(lambda: self.controller.updates_planning_week(self.ui.planningsemaine, globals.planning_week[0], next_week=True))
        self.ui.planningPrevWeekBtn.clicked.connect(lambda: self.controller.updates_planning_week(self.ui.planningsemaine, globals.planning_week[0], previous_week=True))
        # self.ui.planningPickerWeekBtn.clicked.connect()
        
        
        
        ## Initialisation des valeurs par default
        self.ui.name.setText(globals.PRENOM_UTILISATEUR)
        
        current_date = datetime.now().strftime("%d/%m/%Y")
        self.controller.updates_planning_week(self.ui.planningsemaine, current_date)
        
        # Création de l'item personnalisé
        custom_widget = self.controller._test()

        # Création de l'item de tableau personnalisé
        item = QTableWidgetItem()
        # item.setBackground(QColor("red"))

        # Définition du widget comme élément de la cellule
        self.ui.tableWidget.setSpan(1, 1, 5, 1)
        self.ui.tableWidget.setCellWidget(1, 1, custom_widget)
        self.ui.tableWidget.setItem(1, 1, item)
        

########################################################################
## EXECUTE APP
########################################################################
app = QApplication(sys.argv)
login = LoginDialog()

# if login.exec_() == QDialog.Accepted:
        
#         mainwindow = MainWindow()
#         mainwindow.show()
#         sys.exit(app.exec_())


globals.PRENOM_UTILISATEUR = "Jérémie"
mainwindow = MainWindow()
mainwindow.show()

sys.exit(app.exec_())

########################################################################
## END===>
########################################################################  