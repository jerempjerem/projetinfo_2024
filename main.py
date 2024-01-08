# pyside2-uic ui/login.ui -o ui_login.py
# pyside2-uic ui/mainwindow.ui -o ui_mainwindow.py
# pyrcc5 ressources.qrc -o ressources_rc.py



import sys
from database import *
########################################################################
# IMPORT GUI FILE
from ui_login import *
from ui_mainwindow import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
########################################################################


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
        self.ui.loginbtn.clicked.connect(self.login)
        self.show()
        
    def login(self):
        username = self.ui.username
        password = self.ui.password
                
        if login(username.text(),password.text()):
            print('Correct !')
            self.hide()
            mainwindow.show()
            
        else:
            username.clear()
            password.clear()
            self.ui.error_password.setText('Credentials error !')


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