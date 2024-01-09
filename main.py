# pyside2-uic ui/logindialog.ui -o ui_logindialog.py
# pyside2-uic ui/mainwindow.ui -o ui_mainwindow.py
# pyrcc5 ressources.qrc -o ressources_rc.py

#MVC

import sys
import globals
import functions
import locale
from datetime import datetime

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget
from database import Database
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

db = Database()

########################################################################
## LOGIN WINDOW CLASS
########################################################################
class LoginDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles={"styles/style.json"})
        ########################################################################

        ########################################################################       
        self.ui.loginbtn.clicked.connect(self.login)
        self.ui.closebtn.clicked.connect(self.exit)
        
    def exit(self):
        sys.exit(app.exec_())
        
    def login(self):
       
        query = f"SELECT Username, Mdp, Prenom FROM EMPLOYES WHERE Username='{self.ui.username.text()}'"
        result = db.fetch(query)
        
        if result:
            password = result[0][1]
            globals.PRENOM_UTILISATEUR = result[0][2]
            
            if password == self.ui.password.text():
                self.accept()
            else:
                self.ui.password.clear()
                self.ui.error_password.setText("Mot de passe invalide")
        else:
            self.clear_username_password()
            self.ui.error_password.setText("Nom d'utilisateur invalide")
                
    def clear_username_password(self):
        self.ui.username.clear()
        self.ui.password.clear()
        
        
########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles={"styles/style.json"})
        ########################################################################

        ########################################################################      
        
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        ## Navigations des pages
        self.ui.planningBtn.clicked.connect(self._go_to_planning_page)
        self.ui.timelineBtn.clicked.connect(self._go_to_timeline_page)
        self.ui.editBtn.clicked.connect(self._go_to_edit_page)
        
        # Page Planning
        self.ui.planningNextWeekBtn.clicked.connect(lambda: self._updates_planning_week(self.ui.planningsemaine, functions.planning_week[0], next_week=True))
        self.ui.planningPrevWeekBtn.clicked.connect(lambda: self._updates_planning_week(self.ui.planningsemaine, functions.planning_week[0], previous_week=True))
        # self.ui.planningPickerWeekBtn.clicked.connect()
        
        
        
        ## Initialisation des valeurs par default
        self.ui.name.setText(globals.PRENOM_UTILISATEUR)
        
        current_date = datetime.now().strftime("%d/%m/%Y")
        self._updates_planning_week(self.ui.planningsemaine, current_date)
    
    
    def _updates_planning_week(self, plage_label: QLabel, date: str, previous_week : bool = False, next_week : bool = False):
        
        functions.planning_week = functions.get_weekdates(date, previous_week=previous_week, next_week=next_week)
        planning_plage = functions.get_plage_dates(functions.planning_week)
        plage_label.setText(planning_plage)
    
    def _go_to_planning_page(self):
        self.ui.stackedplanning.setCurrentIndex(0)

    def _go_to_timeline_page(self):
        self.ui.stackedplanning.setCurrentIndex(1) 
    
    def _go_to_edit_page(self):
        self.ui.stackedplanning.setCurrentIndex(2) 

        


########################################################################
## EXECUTE APP
########################################################################
app = QApplication(sys.argv)
login = LoginDialog()

if login.exec_() == QDialog.Accepted:
        
        mainwindow = MainWindow()
        mainwindow.show()
        sys.exit(app.exec_())


globals.PRENOM_UTILISATEUR = "Jérémie"
mainwindow = MainWindow()
mainwindow.show()

# sys.exit(app.exec_())

########################################################################
## END===>
########################################################################  