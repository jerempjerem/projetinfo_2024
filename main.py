# pyside2-uic ui/logindialog.ui -o ui_logindialog.py
# pyside2-uic ui/mainwindow.ui -o ui_mainwindow.py
# pyrcc5 ressources.qrc -o ressources_rc.py

#MVC

import sys
import globals
from functions import LoginController, MainController, save_user, read_user
import locale
from datetime import datetime
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

        loadJsonStyle(self, self.ui, jsonFiles={"styles/loginstyle.json"})
        ########################################################################

        ########################################################################       
        self.ui.loginbtn.clicked.connect(lambda: self.controller.login())
        self.ui.closebtn.clicked.connect(self.close)
        
        
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
        self.editcalendar : list[QLabel] = [self.ui.editlundi, self.ui.editmardi, self.ui.editmercredi, self.ui.editjeudi, self.ui.editvendredi, self.ui.editsamedi, self.ui.editdimanche]

        loadJsonStyle(self, self.ui, jsonFiles={"styles/mainstyle.json"})
        ########################################################################

        ########################################################################      
        
        ## Navigations des pages
        self.ui.planningBtn.clicked.connect(lambda: self.ui.stackedplanning.setCurrentIndex(0))
        self.ui.timelineBtn.clicked.connect(lambda: self.ui.stackedplanning.setCurrentIndex(1))
        self.ui.editBtn.clicked.connect(lambda: self.ui.stackedplanning.setCurrentIndex(2))
        self.ui.decoBtn.clicked.connect(self.disconnect)
        
        ## Page Planning
        self.init_table(self.ui.tableplanning)
        
        self.ui.planningNextWeekBtn.clicked.connect(lambda: self.controller.update_calendar(self.ui.planningsemaine, self.planningcalendar, self.ui.tableplanning, 'Planning', next_week=True))
        self.ui.planningPrevWeekBtn.clicked.connect(lambda: self.controller.update_calendar(self.ui.planningsemaine, self.planningcalendar, self.ui.tableplanning, 'Planning', previous_week=True))
        # self.ui.planningPickerWeekBtn.clicked.connect()
        
        
        ## Page Editer
        self.init_table(self.ui.tableedit)
        self.ui.editNextWeekBtn.clicked.connect(lambda: self.controller.update_calendar(self.ui.editsemaine, self.editcalendar, self.ui.tableedit, 'Editer', next_week=True))
        self.ui.editPrevWeekBtn.clicked.connect(lambda: self.controller.update_calendar(self.ui.editsemaine, self.editcalendar, self.ui.tableedit, 'Editer', previous_week=True))
        # self.ui.editPickerWeekBtn.clicked.connect()
        self.ui.editAddEventBtn.clicked.connect(lambda: self.controller.displaypopup(iseditable=True))
        
        
        self.ui.editpersonpicker.currentIndexChanged.connect(lambda: self.controller.update_calendar(self.ui.editsemaine, self.editcalendar, self.ui.tableedit, 'Editer'))
        
        ## Popup event
        self.ui.closepopupBtn.clicked.connect(lambda: self.ui.popupContainer.collapseMenu())
        self.ui.popupsaveBtn.clicked.connect(lambda: self.controller.save_edit_event())
        
        self.ui.popupdatedebut.setCalendarPopup(True)
        self.ui.popupdatedebut.setDateTime(QDateTime.currentDateTime())
        self.ui.popupdatefin.setCalendarPopup(True)
        self.ui.popupdatefin.setDateTime(QDateTime.currentDateTime())
        
        # self.ui.popuplieux.setEditable(True) # Permet d'ecrire et non pas seulement selectionner dans la liste si a True

        ## Initialisation des valeurs par default
        self.ui.name.setText(globals.PRENOM_UTILISATEUR)
                
        current_date = datetime.now().strftime("%d/%m/%Y")
        self.controller.update_calendar(self.ui.planningsemaine, self.planningcalendar, self.ui.tableplanning, 'Planning', option_date=current_date)  
        self.controller.update_calendar(self.ui.editsemaine, self.editcalendar, self.ui.tableedit, 'Editer', option_date=current_date)       
    
    def init_table(self, table: QTableWidget):
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setSelectionMode(QTableWidget.NoSelection)# Désactiver la sélection des cellules
        table.setEditTriggers(QTableWidget.NoEditTriggers) # Désactiver l'édition des cellules
        table.setFocusPolicy(Qt.NoFocus)  # Desactive les effets sur les cellules lors d'un clic
    
    def disconnect(self):
        if os.path.exists(globals.PATH_TEMP_FILE):
            os.remove(globals.PATH_TEMP_FILE)   
            
            self.close()
            new_login_dialog = LoginDialog()
            if new_login_dialog.exec_() == QDialog.Accepted:
                save_user()
                new_main_window = MainWindow()
                new_main_window.show()



if __name__ == "__main__":

    globals.EVENT_LIEUX = [element[0] for element in globals.db.fetch('SELECT LIEU.Nom FROM LIEU')]
    globals.EQUIPES = [element[0] for element in globals.db.fetch('SELECT EQUIPE.Nom FROM EQUIPE')]
    globals.EVENT_TYPES_AND_COLORS = {types: colors for types, colors in globals.db.fetch('SELECT TYPE.Nom, TYPE.Couleur FROM TYPE')}
    globals.PERSONNES = [element[0] for element in globals.db.fetch('SELECT EMPLOYES.Username, EMPLOYES.Nom FROM EMPLOYES')]
    print(globals.PERSONNES)
    
    app = QApplication(sys.argv)

    # Vérifier si le fichier temporaire existe
    if os.path.exists(globals.PATH_TEMP_FILE):
        read_user()
    else:
        login = LoginDialog()
        if login.exec_() == QDialog.Accepted:
            save_user()

    # Lancer l'application
    mainwindow = MainWindow()
    mainwindow.show()
    
    sys.exit(app.exec_())

