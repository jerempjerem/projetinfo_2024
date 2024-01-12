# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Custom_Widgets import *

import ressources_rc

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(955, 696)
        LoginDialog.setStyleSheet(u"* {\n"
"letter-spacing: 1px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: None;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(LoginDialog)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftside = QFrame(LoginDialog)
        self.leftside.setObjectName(u"leftside")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftside.sizePolicy().hasHeightForWidth())
        self.leftside.setSizePolicy(sizePolicy)
        self.leftside.setStyleSheet(u"background-color: rgb(0, 72, 111);\n"
"border-top-left-radius: 50px;")
        self.leftside.setFrameShape(QFrame.StyledPanel)
        self.leftside.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftside)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(11, 70, 11, 11)

        self.label = QLabel(self.leftside)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(400, 450))
        self.label.setPixmap(QPixmap(u"./icons/logo_login.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.leftside)

        self.rightside = QFrame(LoginDialog)
        self.rightside.setObjectName(u"rightside")
        self.rightside.setStyleSheet(u"#rightside {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-bottom-right-radius: 50px;\n"
"}")
        self.rightside.setFrameShape(QFrame.StyledPanel)
        self.rightside.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.rightside)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.frame = QFrame(self.rightside)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 456789))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.minimizebtn = QPushButton(self.frame)
        self.minimizebtn.setObjectName(u"minimizebtn")
        self.minimizebtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizebtn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.minimizebtn)

        self.closebtn = QPushButton(self.frame)
        self.closebtn.setObjectName(u"closebtn")
        self.closebtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closebtn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.closebtn)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignRight)

        self.login_frame = QFrame(self.rightside)
        self.login_frame.setObjectName(u"login_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.login_frame.sizePolicy().hasHeightForWidth())
        self.login_frame.setSizePolicy(sizePolicy1)
        self.login_frame.setMinimumSize(QSize(300, 0))
        self.login_frame.setStyleSheet(u"QLineEdit {\n"
"color: rgb(9, 78, 116);\n"
"border: none;\n"
"border-bottom: 2px solid #094e74;\n"
"}")
        self.login_frame.setFrameShape(QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.login_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 50)
        self.label_2 = QLabel(self.login_frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Sans Serif Collection")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.username = QLineEdit(self.login_frame)
        self.username.setObjectName(u"username")
        font1 = QFont()
        font1.setFamily(u"Sans Serif Collection")
        font1.setPointSize(10)
        self.username.setFont(font1)
        self.username.setStyleSheet(u"")
        self.username.setClearButtonEnabled(False)

        self.verticalLayout_2.addWidget(self.username)

        self.password = QLineEdit(self.login_frame)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setObjectName(u"password")
        self.password.setFont(font1)
        self.password.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.password)

        self.error_password = QLabel(self.login_frame)
        self.error_password.setObjectName(u"error_password")
        font2 = QFont()
        font2.setFamily(u"Sans Serif Collection")
        font2.setBold(True)
        font2.setWeight(75)
        self.error_password.setFont(font2)
        self.error_password.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.error_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.error_password)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.loginbtn = QPushButton(self.login_frame)
        self.loginbtn.setObjectName(u"loginbtn")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setWeight(75)
        self.loginbtn.setFont(font3)
        self.loginbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginbtn.setFocusPolicy(Qt.NoFocus)
        self.loginbtn.setStyleSheet(u"background-color: rgb(9, 78, 116);\n"
"color: white;\n"
"padding-top: 40px;\n"
"padding-bottom: 40px;\n"
"border-radius: 30px;")
        self.loginbtn.setCheckable(False)
        self.loginbtn.setFlat(False)

        self.verticalLayout_2.addWidget(self.loginbtn)


        self.verticalLayout.addWidget(self.login_frame, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.rightside)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.retranslateUi(LoginDialog)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"MainWindow", None))
        self.label.setText("")
        self.minimizebtn.setText("")
        self.closebtn.setText("")
        self.label_2.setText(QCoreApplication.translate("LoginDialog", u"Log In", None))
        self.username.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"Nom d'utilisateur", None))
        self.password.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"Mot de passe", None))
        self.error_password.setText("")
        self.loginbtn.setText(QCoreApplication.translate("LoginDialog", u"Log In", None))
    # retranslateUi

