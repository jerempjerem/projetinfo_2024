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
        MainWindow.resize(1574, 847)
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
"\n"
"#frame_9{\n"
"	background-color: rgb(239, 239, 239);\n"
"	border-top-left-radius: 30px;	\n"
"	border-top-right-radius: 30px;	\n"
"	padding: 7px 0;\n"
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
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_2 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
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
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.stackedplanning = QStackedWidget(self.mainBodyContent)
        self.stackedplanning.setObjectName(u"stackedplanning")
        self.planningPage = QWidget()
        self.planningPage.setObjectName(u"planningPage")
        self.verticalLayout_8 = QVBoxLayout(self.planningPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget = QWidget(self.planningPage)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255, 242, 225);\n"
"	border: 3px solid #D7B78E;	\n"
"	border-top-right-radius: 20px;\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.planningnbheures = QLabel(self.frame_8)
        self.planningnbheures.setObjectName(u"planningnbheures")
        self.planningnbheures.setFont(font)
        self.planningnbheures.setStyleSheet(u"padding: 0 30px;")
        self.planningnbheures.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.planningnbheures)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.planningsemaine = QLabel(self.frame_7)
        self.planningsemaine.setObjectName(u"planningsemaine")
        self.planningsemaine.setFont(font)
        self.planningsemaine.setStyleSheet(u"")
        self.planningsemaine.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.planningsemaine)


        self.horizontalLayout_5.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 242, 225);\n"
"	padding: 15px 15px;\n"
"	border-radius: 25px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.planningPrevWeekBtn = QPushButton(self.frame_6)
        self.planningPrevWeekBtn.setObjectName(u"planningPrevWeekBtn")
        self.planningPrevWeekBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.planningPrevWeekBtn.setIcon(icon6)
        self.planningPrevWeekBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.planningPrevWeekBtn)

        self.planningNextWeekBtn = QPushButton(self.frame_6)
        self.planningNextWeekBtn.setObjectName(u"planningNextWeekBtn")
        self.planningNextWeekBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.planningNextWeekBtn.setIcon(icon7)
        self.planningNextWeekBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.planningNextWeekBtn)

        self.planningPickerWeekBtn = QPushButton(self.frame_6)
        self.planningPickerWeekBtn.setObjectName(u"planningPickerWeekBtn")
        self.planningPickerWeekBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.planningPickerWeekBtn.setIcon(icon)
        self.planningPickerWeekBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.planningPickerWeekBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignLeft)


        self.verticalLayout_8.addWidget(self.widget, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.planningPage)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.widget_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.planninglundi = QLabel(self.frame_9)
        self.planninglundi.setObjectName(u"planninglundi")
        font3 = QFont()
        font3.setFamily(u"Sans Serif Collection")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.planninglundi.setFont(font3)
        self.planninglundi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.planninglundi)

        self.planningmardi = QLabel(self.frame_9)
        self.planningmardi.setObjectName(u"planningmardi")
        self.planningmardi.setFont(font3)
        self.planningmardi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.planningmardi)

        self.planningmercredi = QLabel(self.frame_9)
        self.planningmercredi.setObjectName(u"planningmercredi")
        self.planningmercredi.setFont(font3)
        self.planningmercredi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.planningmercredi)

        self.planningjeudi = QLabel(self.frame_9)
        self.planningjeudi.setObjectName(u"planningjeudi")
        self.planningjeudi.setFont(font3)
        self.planningjeudi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.planningjeudi)

        self.planningvendredi = QLabel(self.frame_9)
        self.planningvendredi.setObjectName(u"planningvendredi")
        self.planningvendredi.setFont(font3)
        self.planningvendredi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.planningvendredi)

        self.planningsamedi = QLabel(self.frame_9)
        self.planningsamedi.setObjectName(u"planningsamedi")
        self.planningsamedi.setFont(font3)
        self.planningsamedi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.planningsamedi)

        self.planningdimanche = QLabel(self.frame_9)
        self.planningdimanche.setObjectName(u"planningdimanche")
        self.planningdimanche.setFont(font3)
        self.planningdimanche.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.planningdimanche)


        self.verticalLayout_11.addWidget(self.frame_9)


        self.verticalLayout_10.addWidget(self.widget_3, 0, Qt.AlignTop)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.verticalLayout_12 = QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 0, 5, 0)
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setPointSize(9)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(0)

        self.verticalLayout_12.addWidget(self.label_2)

        self.label_18 = QLabel(self.widget_5)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setFont(font4)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_18)

        self.label_24 = QLabel(self.widget_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font4)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_24)


        self.horizontalLayout_9.addWidget(self.widget_5, 0, Qt.AlignLeft)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.widget_6)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        if (self.tableWidget.rowCount() < 20):
            self.tableWidget.setRowCount(20)
        self.tableWidget.setObjectName(u"tableWidget")
        font5 = QFont()
        font5.setFamily(u"Sans Serif Collection")
        self.tableWidget.setFont(font5)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.DotLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_10.addWidget(self.tableWidget)


        self.horizontalLayout_9.addWidget(self.widget_6)


        self.verticalLayout_10.addWidget(self.widget_4)


        self.verticalLayout_8.addWidget(self.widget_2)

        self.stackedplanning.addWidget(self.planningPage)
        self.timelinePage = QWidget()
        self.timelinePage.setObjectName(u"timelinePage")
        self.label_3 = QLabel(self.timelinePage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(490, 300, 111, 51))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedplanning.addWidget(self.timelinePage)
        self.editPage = QWidget()
        self.editPage.setObjectName(u"editPage")
        self.label_4 = QLabel(self.editPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(570, 380, 121, 71))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedplanning.addWidget(self.editPage)

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
        self.planningnbheures.setText(QCoreApplication.translate("MainWindow", u"Nombre d'heures : 30h/34h", None))
        self.planningsemaine.setText("")
        self.planningPrevWeekBtn.setText("")
        self.planningNextWeekBtn.setText("")
        self.planningPickerWeekBtn.setText("")
        self.planninglundi.setText(QCoreApplication.translate("MainWindow", u"Lun 12", None))
        self.planningmardi.setText(QCoreApplication.translate("MainWindow", u"Mar 13", None))
        self.planningmercredi.setText(QCoreApplication.translate("MainWindow", u"Mer 14", None))
        self.planningjeudi.setText(QCoreApplication.translate("MainWindow", u"Jeu 15", None))
        self.planningvendredi.setText(QCoreApplication.translate("MainWindow", u"Ven 16", None))
        self.planningsamedi.setText(QCoreApplication.translate("MainWindow", u"Sam 17", None))
        self.planningdimanche.setText(QCoreApplication.translate("MainWindow", u"Dim 18", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"8h", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"13h", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"18h", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Timeline", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Editer", None))
    # retranslateUi

