# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1517, 815)
        MainWindow.setStyleSheet(u"* {\n"
"letter-spacing: 1px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"#leftmenuContainer {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#leftMenuSubContainer {\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#mainBodyContainer{\n"
"	background-color: rgb(0, 72, 112);\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"#headerContainer {\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"\n"
"#mainBodyContent {\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftmenuContainer = QWidget(self.centralwidget)
        self.leftmenuContainer.setObjectName(u"leftmenuContainer")
        self.leftmenuContainer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftmenuContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.leftMenuSubContainer = QWidget(self.leftmenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid #D7B78E;\n"
"	padding: 3px 10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#frame_2 {\n"
"	border-top: 3px solid #004870;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 15)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(90, 90))
        self.label.setPixmap(QPixmap(u"./icons/user.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter)

        self.name = QLabel(self.frame)
        self.name.setObjectName(u"name")
        font = QFont()
        font.setFamily(u"Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.name)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 25, -1, -1)
        self.planningBtn = QPushButton(self.frame_2)
        self.planningBtn.setObjectName(u"planningBtn")
        font1 = QFont()
        font1.setFamily(u"Sans Serif Collection")
        font1.setPointSize(10)
        self.planningBtn.setFont(font1)
        self.planningBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.planningBtn.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/icons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.planningBtn.setIcon(icon)

        self.verticalLayout_3.addWidget(self.planningBtn)

        self.timelineBtn = QPushButton(self.frame_2)
        self.timelineBtn.setObjectName(u"timelineBtn")
        self.timelineBtn.setFont(font1)
        self.timelineBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.timelineBtn.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.timelineBtn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.timelineBtn)

        self.editBtn = QPushButton(self.frame_2)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setFont(font1)
        self.editBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editBtn.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/edit-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editBtn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.editBtn)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.decoBtn = QPushButton(self.frame_3)
        self.decoBtn.setObjectName(u"decoBtn")
        font2 = QFont()
        font2.setFamily(u"Sans Serif Collection")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.decoBtn.setFont(font2)
        self.decoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.decoBtn.setFocusPolicy(Qt.NoFocus)
        self.decoBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/power.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.decoBtn.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.decoBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftmenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_2 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.headerContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.minimizeBtn = QPushButton(self.frame_4)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/minus_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon4)
        self.minimizeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.closeBtn = QPushButton(self.frame_4)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/x_white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon5)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout_2.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.verticalLayout_7 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stackedplanning = QStackedWidget(self.mainBodyContent)
        self.stackedplanning.setObjectName(u"stackedplanning")
        self.stackedplanningPage1 = QWidget()
        self.stackedplanningPage1.setObjectName(u"stackedplanningPage1")
        self.label_2 = QLabel(self.stackedplanningPage1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(520, 270, 121, 51))
        self.label_2.setStyleSheet(u"color: white\n"
"")
        self.stackedplanning.addWidget(self.stackedplanningPage1)
        self.stackedplanningPage2 = QWidget()
        self.stackedplanningPage2.setObjectName(u"stackedplanningPage2")
        self.label_3 = QLabel(self.stackedplanningPage2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(490, 300, 111, 51))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedplanning.addWidget(self.stackedplanningPage2)
        self.stackedplanningPage3 = QWidget()
        self.stackedplanningPage3.setObjectName(u"stackedplanningPage3")
        self.label_4 = QLabel(self.stackedplanningPage3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(570, 380, 121, 71))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedplanning.addWidget(self.stackedplanningPage3)

        self.verticalLayout_7.addWidget(self.stackedplanning)


        self.verticalLayout_6.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedplanning.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.name.setText("")
        self.planningBtn.setText(QCoreApplication.translate("MainWindow", u"  Planning", None))
        self.timelineBtn.setText(QCoreApplication.translate("MainWindow", u"  Timeline", None))
        self.editBtn.setText(QCoreApplication.translate("MainWindow", u"  \u00c9diter", None))
        self.decoBtn.setText(QCoreApplication.translate("MainWindow", u"  D\u00e9connexion", None))
        self.minimizeBtn.setText("")
        self.closeBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Planning", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Timeline", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Editer", None))
    # retranslateUi

