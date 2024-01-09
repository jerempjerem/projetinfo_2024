# pyside2-uic ui/logindialog.ui -o ui_logindialog.py
# pyside2-uic ui/mainwindow.ui -o ui_mainwindow.py
# pyrcc5 ressources.qrc -o ressources_rc.py

#MVC

import sys
import globals
from functions import LoginController, MainController
import locale
from datetime import datetime
import tempfile
import json
import os

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
        
        self.planningcalendar : list[QLabel] = [self.ui.planninglundi, self.ui.planningmardi, self.ui.planningmercredi, self.ui.planningjeudi, self.ui.planningvendredi, self.ui.planningsamedi, self.ui.planningdimanche]


        loadJsonStyle(self, self.ui, jsonFiles={"styles/style.json"})
        ########################################################################

        ########################################################################      
        
        ## Navigations des pages
        self.ui.planningBtn.clicked.connect(lambda: self.ui.stackedplanning.setCurrentIndex(0))
        self.ui.timelineBtn.clicked.connect(lambda: self.ui.stackedplanning.setCurrentIndex(1))
        self.ui.editBtn.clicked.connect(lambda: self.ui.stackedplanning.setCurrentIndex(2))
        self.ui.decoBtn.clicked.connect(lambda: self.controller.disconnect())
        
        ## Page Planning
        self.ui.tableplanning.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableplanning.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableplanning.setSelectionMode(QTableWidget.NoSelection)# Désactiver la sélection des cellules
        self.ui.tableplanning.setEditTriggers(QTableWidget.NoEditTriggers) # Désactiver l'édition des cellules
        self.ui.tableplanning.setFocusPolicy(Qt.NoFocus)  # Desactive les effets sur les cellules lors d'un clic
        
        self.ui.planningNextWeekBtn.clicked.connect(lambda: self.controller.update_calendar(self.ui.planningsemaine, globals.PLANNING_TABS['Planning'][0], self.planningcalendar, self.ui.tableplanning, 'Planning', next_week=True))
        self.ui.planningPrevWeekBtn.clicked.connect(lambda: self.controller.update_calendar(self.ui.planningsemaine, globals.PLANNING_TABS['Planning'][0], self.planningcalendar, self.ui.tableplanning, 'Planning', previous_week=True))
        # self.ui.planningPickerWeekBtn.clicked.connect()
        
        ## Initialisation des valeurs par default
        self.ui.name.setText(globals.PRENOM_UTILISATEUR)
        
        current_date = datetime.now().strftime("%d/%m/%Y")
        self.controller.update_calendar(self.ui.planningsemaine, current_date, self.planningcalendar, self.ui.tableplanning, 'Planning')        

########################################################################
## EXECUTE APP
########################################################################
app = QApplication(sys.argv)


# Vérifier si le fichier temporaire existe
if os.path.exists(globals.PATH_TEMP_FILE):
    with open(globals.PATH_TEMP_FILE, 'r') as existing_file:
        content = json.load(existing_file)
        globals.PRENOM_UTILISATEUR = content['Prenom']  # Utilisez get pour éviter une KeyError
        globals.USERNAME_UTILISATEUR = content['Username']  # Utilisez get pour éviter une KeyError

else:
    login = LoginDialog()
    if login.exec_() == QDialog.Accepted:

        data = {"Prenom": globals.PRENOM_UTILISATEUR, "Username": globals.USERNAME_UTILISATEUR}
        with open(globals.PATH_TEMP_FILE, 'w') as new_file:
            json.dump(data, new_file, indent=2)

# Lancer l'application
mainwindow = MainWindow()
mainwindow.show()
sys.exit(app.exec_())


########################################################################
## END===>
########################################################################  