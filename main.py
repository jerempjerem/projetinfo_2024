# pyside2-uic ui/login.ui -o ui_login.py
# pyside2-uic ui/mainwindow.ui -o ui_mainwindow.py
# pyrcc5 ressources.qrc -o ressources_rc.py



import sys
from database import Database
########################################################################
# IMPORT GUI FILE
from ui_login import *
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
class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles={"styles/loginstyle.json"})
        ########################################################################

        ########################################################################   
        self.ui.password.setEchoMode(QLineEdit.Password)    
        self.ui.loginbtn.clicked.connect(self.login)
        
        self.show()
        
    def login(self):
       
        query = f"SELECT Username, Mdp FROM EMPLOYES WHERE Username='{self.ui.username.text()}'"
        result = db.fetch(query)
        
        if result:
            password = result[0][1]
            if password == self.ui.password.text():
                self.hide()
                mainwindow.show()
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

        loadJsonStyle(self, self.ui, jsonFiles={"styles/mainstyle.json"})
        ########################################################################

        ########################################################################       

        


########################################################################
## EXECUTE APP
########################################################################
app = QApplication(sys.argv)
loginwindow = LoginWindow()
mainwindow = MainWindow()
sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  