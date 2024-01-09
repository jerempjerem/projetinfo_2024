# pyside2-uic ui/logindialog.ui -o ui_logindialog.py
# pyside2-uic ui/mainwindow.ui -o ui_mainwindow.py
# pyrcc5 ressources.qrc -o ressources_rc.py



import sys
import globals

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

db = Database()

########################################################################
## LOGIN WINDOW CLASS
########################################################################
class LoginDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles={"styles/loginstyle.json"})
        ########################################################################

        ########################################################################   
        self.ui.password.setEchoMode(QLineEdit.Password)    
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
        self.ui.name.setText(globals.PRENOM_UTILISATEUR)

        loadJsonStyle(self, self.ui, jsonFiles={"styles/mainstyle.json"})
        ########################################################################

        ########################################################################      
        self.ui.planningBtn.clicked.connect(self._go_to_planning_page)
        self.ui.timelineBtn.clicked.connect(self._go_to_timeline_page)
        self.ui.editBtn.clicked.connect(self._go_to_edit_page)


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

# loginwindow = LoginWindow()


# loginwindow.show()
# mainwindow.show()

########################################################################
## END===>
########################################################################  