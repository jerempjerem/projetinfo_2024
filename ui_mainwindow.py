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

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu

import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1617, 861)
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
"#frame_9, #frame_13{\n"
"	background-color: rgb(239, 239, 239);\n"
"	border-top-left-radius: 30px;	\n"
"	border-top-right-radius: 30px;	\n"
"	padding: 7px 0;\n"
"}\n"
"\n"
"#popupContainer{\n"
"	background-color: #D7B78E;\n"
"	color: rgb(67, 70, 81);\n"
"	width: 700px;\n"
"	height: 500px;\n"
"	border-top-left-radius: 10px;	\n"
"	border-top-right-radius: 10px;	\n"
"	border-b"
                        "ottom-left-radius: 10px;	\n"
"	border-bottom-right-radius: 10px;	\n"
"}\n"
"\n"
"/* Style for header area  ####################################################*/ \n"
"\n"
"QCalendarWidget QWidget {\n"
"	 alternate-background-color: #B8E2FF;\n"
"}\n"
"\n"
"/* style for top navigation area ###############################################*/ \n"
"\n"
"#qt_calendar_navigationbar {\n"
"    background-color: #fff;\n"
"	border: 2px solid  #B8E2FF;\n"
"	border-bottom: 0px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"}\n"
"\n"
"/* style for month change buttons ############################################ */\n"
"\n"
"#qt_calendar_prevmonth, \n"
"#qt_calendar_nextmonth {\n"
"	/* border delete */\n"
"    border: none;  \n"
"    /* delete default icons */\n"
"	qproperty-icon: none; \n"
"	\n"
"    min-width: 13px;\n"
"    max-width: 13px;\n"
"    min-height: 13px;\n"
"    max-height: 13px;\n"
"\n"
"    border-radius: 5px; \n"
"	/* set background transparent */\n"
"    background-color: transparen"
                        "t; \n"
"	padding: 5px;\n"
"}\n"
"\n"
"/* style for pre month button ############################################ */\n"
"\n"
"#qt_calendar_prevmonth {\n"
"	/* set text for button */\n"
"	/*qproperty-text: &quot;&gt;&quot;;*/\n"
"	margin-left:5px;\n"
"	image: url(:/icons/icons/arrow-left.svg);\n"
"}\n"
"\n"
"/* style for next month button ########################################### */\n"
"#qt_calendar_nextmonth {\n"
"	margin-right:5px;\n"
"	image: url(:/icons/icons/arrow-right.svg);\n"
"}\n"
"\n"
"/* Style for month and yeat buttons #################################### */\n"
"\n"
"#qt_calendar_yearbutton {\n"
"    color: #000;\n"
"	margin:5px;\n"
"    border-radius: 5px;\n"
"	font-size: 13px;\n"
"	padding:0px 10px;\n"
"}\n"
"\n"
" #qt_calendar_monthbutton {\n"
"	width: 110px;\n"
"    color: #000;\n"
"	font-size: 13px;\n"
"	margin:5px 0px;\n"
"    border-radius: 5px;\n"
"	padding:0px 2px;\n"
"}\n"
"\n"
"/* Style for year input lineEdit ######################################*/\n"
"\n"
"#qt_calendar_yearedit {\n"
""
                        "    min-width: 53px;\n"
"    color: #000;\n"
"    background: transparent;\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"/* Style for year change buttons ######################################*/\n"
"\n"
"#qt_calendar_yearedit::up-button { \n"
"	image: url(:/icons/icons/arrow-up.svg);\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button { \n"
"	image: url(:/icons/icons/arrow-down.svg);\n"
"    subcontrol-position: left; \n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button, \n"
"#qt_calendar_yearedit::up-button {\n"
"	width:10px;\n"
"	padding: 0px 5px;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"/* Style for month select menu ##################################### */\n"
"\n"
"#calendarWidget QToolButton QMenu {\n"
"     background-color: white;\n"
"\n"
"}\n"
"#calendarWidget QToolButton QMenu::item {\n"
"	/*padding: 10px;*/\n"
"}\n"
" #calendarWidget QToolButton QMenu::item:selected:enabled {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#calendarWidget QToolButton::menu-indicator {\n"
"	/* R"
                        "emove toolButton arrow */\n"
"      /*image: none; */\n"
"	nosubcontrol-origin: margin;\n"
"	subcontrol-position: right center;\n"
"	margin-top: 10px;\n"
"	width:20px;\n"
"}\n"
"\n"
"/* Style for calendar table ########################################## */\n"
"#qt_calendar_calendarview {\n"
"	/* Remove the selected dashed box */\n"
"    outline: 0px;\n"
"\n"
"	border: 2px solid  #B8E2FF;\n"
"	border-top: 0px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
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
        self.label.setPixmap(QPixmap(u":/icons/icons/user.png"))
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
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 11)
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
        self.planningnbheures.setMinimumSize(QSize(380, 0))
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
        self.horizontalLayout_8.setContentsMargins(20, 0, 0, 0)
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
        self.tableplanning = QTableWidget(self.widget_6)
        if (self.tableplanning.columnCount() < 7):
            self.tableplanning.setColumnCount(7)
        if (self.tableplanning.rowCount() < 20):
            self.tableplanning.setRowCount(20)
        self.tableplanning.setObjectName(u"tableplanning")
        font5 = QFont()
        font5.setFamily(u"Sans Serif Collection")
        self.tableplanning.setFont(font5)
        self.tableplanning.setFrameShape(QFrame.NoFrame)
        self.tableplanning.setLineWidth(1)
        self.tableplanning.setMidLineWidth(0)
        self.tableplanning.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableplanning.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableplanning.setAutoScroll(False)
        self.tableplanning.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableplanning.setDragDropOverwriteMode(False)
        self.tableplanning.setShowGrid(True)
        self.tableplanning.setGridStyle(Qt.DotLine)
        self.tableplanning.setSortingEnabled(False)
        self.tableplanning.setCornerButtonEnabled(True)
        self.tableplanning.setRowCount(20)
        self.tableplanning.setColumnCount(7)
        self.tableplanning.horizontalHeader().setVisible(False)
        self.tableplanning.horizontalHeader().setCascadingSectionResizes(False)
        self.tableplanning.horizontalHeader().setStretchLastSection(False)
        self.tableplanning.verticalHeader().setVisible(False)
        self.tableplanning.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_10.addWidget(self.tableplanning)


        self.horizontalLayout_9.addWidget(self.widget_6)


        self.verticalLayout_10.addWidget(self.widget_4)


        self.verticalLayout_8.addWidget(self.widget_2)

        self.stackedplanning.addWidget(self.planningPage)
        self.timelinePage = QWidget()
        self.timelinePage.setObjectName(u"timelinePage")
        self.stackedplanning.addWidget(self.timelinePage)
        self.editPage = QWidget()
        self.editPage.setObjectName(u"editPage")
        sizePolicy.setHeightForWidth(self.editPage.sizePolicy().hasHeightForWidth())
        self.editPage.setSizePolicy(sizePolicy)
        self.editPage.setStyleSheet(u"QComboBox:focus {\n"
"    border: 2px solid #D7B78E;\n"
"}\n"
"\n"
"QComboBox {\n"
"	height: 45px;\n"
"	width: 130px;\n"
"    border-radius: 20px;\n"
"    background-color: #FFF2E1;\n"
"    border: 3px solid #D7B78E;\n"
"    padding: 2px 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(':/icons/icons/chevron-down.svg');\n"
"    width: 20px;\n"
"    margin-right: 20px;\n"
"}\n"
"\n"
"QListView {\n"
"    font-size: 10px;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    outline: 0px;\n"
"    background-color: #FFF2E1;\n"
"}\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.editPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_7 = QWidget(self.editPage)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255, 242, 225);\n"
"	border: 3px solid #D7B78E;	\n"
"	border-top-right-radius: 20px;\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, -1, -1)
        self.frame_11 = QFrame(self.widget_7)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.editsemaine = QLabel(self.frame_11)
        self.editsemaine.setObjectName(u"editsemaine")
        self.editsemaine.setFont(font)
        self.editsemaine.setStyleSheet(u"")
        self.editsemaine.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.editsemaine)


        self.horizontalLayout_11.addWidget(self.frame_11)

        self.editeteampicker = QComboBox(self.widget_7)
        self.editeteampicker.setObjectName(u"editeteampicker")
        self.editeteampicker.setMinimumSize(QSize(0, 0))
        font6 = QFont()
        font6.setFamily(u"Sans Serif Collection")
        font6.setPointSize(9)
        font6.setBold(True)
        font6.setWeight(75)
        self.editeteampicker.setFont(font6)
        self.editeteampicker.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.editeteampicker)

        self.editpersonpicker = QComboBox(self.widget_7)
        self.editpersonpicker.setObjectName(u"editpersonpicker")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.editpersonpicker.sizePolicy().hasHeightForWidth())
        self.editpersonpicker.setSizePolicy(sizePolicy3)
        self.editpersonpicker.setMinimumSize(QSize(220, 0))
        self.editpersonpicker.setFont(font6)
        self.editpersonpicker.setCursor(QCursor(Qt.PointingHandCursor))
        self.editpersonpicker.setFocusPolicy(Qt.NoFocus)
        self.editpersonpicker.setMaxVisibleItems(30)
        self.editpersonpicker.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.editpersonpicker.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_11.addWidget(self.editpersonpicker)

        self.frame_12 = QFrame(self.widget_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 242, 225);\n"
"	padding: 15px 15px;\n"
"	border-radius: 25px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.editPrevWeekBtn = QPushButton(self.frame_12)
        self.editPrevWeekBtn.setObjectName(u"editPrevWeekBtn")
        self.editPrevWeekBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editPrevWeekBtn.setIcon(icon6)
        self.editPrevWeekBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.editPrevWeekBtn)

        self.editNextWeekBtn = QPushButton(self.frame_12)
        self.editNextWeekBtn.setObjectName(u"editNextWeekBtn")
        self.editNextWeekBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editNextWeekBtn.setIcon(icon7)
        self.editNextWeekBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.editNextWeekBtn)

        self.editPickerWeekBtn = QPushButton(self.frame_12)
        self.editPickerWeekBtn.setObjectName(u"editPickerWeekBtn")
        self.editPickerWeekBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editPickerWeekBtn.setIcon(icon)
        self.editPickerWeekBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.editPickerWeekBtn)

        self.editAddEventBtn = QPushButton(self.frame_12)
        self.editAddEventBtn.setObjectName(u"editAddEventBtn")
        self.editAddEventBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editAddEventBtn.setIcon(icon8)
        self.editAddEventBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.editAddEventBtn)


        self.horizontalLayout_11.addWidget(self.frame_12, 0, Qt.AlignLeft)


        self.verticalLayout_17.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.editPage)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy2.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy2)
        self.verticalLayout_14 = QVBoxLayout(self.widget_8)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_15 = QVBoxLayout(self.widget_9)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.widget_9)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, 0, 0, 0)
        self.editlundi = QLabel(self.frame_13)
        self.editlundi.setObjectName(u"editlundi")
        self.editlundi.setFont(font3)
        self.editlundi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.editlundi)

        self.editmardi = QLabel(self.frame_13)
        self.editmardi.setObjectName(u"editmardi")
        self.editmardi.setFont(font3)
        self.editmardi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.editmardi)

        self.editmercredi = QLabel(self.frame_13)
        self.editmercredi.setObjectName(u"editmercredi")
        self.editmercredi.setFont(font3)
        self.editmercredi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.editmercredi)

        self.editjeudi = QLabel(self.frame_13)
        self.editjeudi.setObjectName(u"editjeudi")
        self.editjeudi.setFont(font3)
        self.editjeudi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.editjeudi)

        self.editvendredi = QLabel(self.frame_13)
        self.editvendredi.setObjectName(u"editvendredi")
        self.editvendredi.setFont(font3)
        self.editvendredi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.editvendredi)

        self.editsamedi = QLabel(self.frame_13)
        self.editsamedi.setObjectName(u"editsamedi")
        self.editsamedi.setFont(font3)
        self.editsamedi.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.editsamedi)

        self.editdimanche = QLabel(self.frame_13)
        self.editdimanche.setObjectName(u"editdimanche")
        self.editdimanche.setFont(font3)
        self.editdimanche.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.editdimanche)


        self.verticalLayout_15.addWidget(self.frame_13)


        self.verticalLayout_14.addWidget(self.widget_9, 0, Qt.AlignTop)

        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy2.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy2)
        self.horizontalLayout_15 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.verticalLayout_16 = QVBoxLayout(self.widget_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 0, 5, 0)
        self.label_3 = QLabel(self.widget_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(0)

        self.verticalLayout_16.addWidget(self.label_3)

        self.label_19 = QLabel(self.widget_11)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setFont(font4)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_19)

        self.label_25 = QLabel(self.widget_11)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font4)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_25)


        self.horizontalLayout_15.addWidget(self.widget_11, 0, Qt.AlignLeft)

        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy1.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy1)
        self.horizontalLayout_16 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.tableedit = QTableWidget(self.widget_12)
        if (self.tableedit.columnCount() < 7):
            self.tableedit.setColumnCount(7)
        if (self.tableedit.rowCount() < 20):
            self.tableedit.setRowCount(20)
        self.tableedit.setObjectName(u"tableedit")
        self.tableedit.setFont(font5)
        self.tableedit.setFrameShape(QFrame.NoFrame)
        self.tableedit.setLineWidth(1)
        self.tableedit.setMidLineWidth(0)
        self.tableedit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableedit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableedit.setAutoScroll(False)
        self.tableedit.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableedit.setDragDropOverwriteMode(False)
        self.tableedit.setShowGrid(True)
        self.tableedit.setGridStyle(Qt.DotLine)
        self.tableedit.setSortingEnabled(False)
        self.tableedit.setCornerButtonEnabled(True)
        self.tableedit.setRowCount(20)
        self.tableedit.setColumnCount(7)
        self.tableedit.horizontalHeader().setVisible(False)
        self.tableedit.horizontalHeader().setCascadingSectionResizes(False)
        self.tableedit.horizontalHeader().setStretchLastSection(False)
        self.tableedit.verticalHeader().setVisible(False)
        self.tableedit.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_16.addWidget(self.tableedit)


        self.horizontalLayout_15.addWidget(self.widget_12)


        self.verticalLayout_14.addWidget(self.widget_10)


        self.verticalLayout_17.addWidget(self.widget_8)

        self.stackedplanning.addWidget(self.editPage)

        self.verticalLayout_7.addWidget(self.stackedplanning)


        self.verticalLayout_6.addWidget(self.mainBodyContent)

        self.popupContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupContainer.setObjectName(u"popupContainer")
        self.popupContainer.setMinimumSize(QSize(0, 0))
        self.popupContainer.setMaximumSize(QSize(16777215, 16777215))
        self.popupContainer.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.popupContainer)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, -1, -1, 11)
        self.widget_13 = QWidget(self.popupContainer)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.widget_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.popupeventname = QLineEdit(self.frame_14)
        self.popupeventname.setObjectName(u"popupeventname")
        self.popupeventname.setMaximumSize(QSize(16777215, 30))
        self.popupeventname.setFont(font6)
        self.popupeventname.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.popupeventname)


        self.horizontalLayout_17.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.frame_15 = QFrame(self.widget_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, -1, 0, -1)
        self.closepopupBtn = QPushButton(self.frame_15)
        self.closepopupBtn.setObjectName(u"closepopupBtn")
        self.closepopupBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closepopupBtn.setIcon(icon9)
        self.closepopupBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_19.addWidget(self.closepopupBtn)


        self.horizontalLayout_17.addWidget(self.frame_15, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_18.addWidget(self.widget_13, 0, Qt.AlignTop)

        self.widget_14 = QWidget(self.popupContainer)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"#widget_14 {\n"
"border-bottom: 2px solid black;\n"
"}")
        self.gridLayout = QGridLayout(self.widget_14)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(80)
        self.gridLayout.setVerticalSpacing(0)
        self.popupdatefin = QDateTimeEdit(self.widget_14)
        self.popupdatefin.setObjectName(u"popupdatefin")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.popupdatefin.sizePolicy().hasHeightForWidth())
        self.popupdatefin.setSizePolicy(sizePolicy4)
        self.popupdatefin.setMaximumSize(QSize(16777215, 25))
        font7 = QFont()
        font7.setFamily(u"Sans Serif Collection")
        font7.setPointSize(9)
        self.popupdatefin.setFont(font7)
        self.popupdatefin.setCursor(QCursor(Qt.PointingHandCursor))
        self.popupdatefin.setFocusPolicy(Qt.WheelFocus)
        self.popupdatefin.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.popupdatefin.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)

        self.gridLayout.addWidget(self.popupdatefin, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font6)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.widget_14)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font6)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.widget_14)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.popupdatedebut = QDateTimeEdit(self.widget_14)
        self.popupdatedebut.setObjectName(u"popupdatedebut")
        sizePolicy1.setHeightForWidth(self.popupdatedebut.sizePolicy().hasHeightForWidth())
        self.popupdatedebut.setSizePolicy(sizePolicy1)
        self.popupdatedebut.setMaximumSize(QSize(16777215, 25))
        font8 = QFont()
        font8.setFamily(u"Sans Serif Collection")
        font8.setPointSize(9)
        font8.setBold(False)
        font8.setWeight(50)
        self.popupdatedebut.setFont(font8)
        self.popupdatedebut.setCursor(QCursor(Qt.PointingHandCursor))
        self.popupdatedebut.setFocusPolicy(Qt.WheelFocus)
        self.popupdatedebut.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.popupdatedebut, 0, 1, 1, 1)

        self.popuplieux = QComboBox(self.widget_14)
        self.popuplieux.setObjectName(u"popuplieux")
        self.popuplieux.setMinimumSize(QSize(0, 25))
        self.popuplieux.setFocusPolicy(Qt.WheelFocus)
        self.popuplieux.setEditable(True)

        self.gridLayout.addWidget(self.popuplieux, 2, 1, 1, 1)

        self.label_9 = QLabel(self.widget_14)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font6)

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)

        self.popuptype = QComboBox(self.widget_14)
        self.popuptype.setObjectName(u"popuptype")
        self.popuptype.setMinimumSize(QSize(0, 25))
        self.popuptype.setEditable(True)

        self.gridLayout.addWidget(self.popuptype, 3, 1, 1, 1)


        self.verticalLayout_18.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.popupContainer)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy2.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy2)
        self.gridLayout_2 = QGridLayout(self.widget_15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(10, 0, 10, -1)
        self.label_8 = QLabel(self.widget_15)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font6)

        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_7 = QLabel(self.widget_15)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.popupteams = QListWidget(self.widget_15)
        self.popupteams.setObjectName(u"popupteams")
        self.popupteams.setFont(font5)
        self.popupteams.setFocusPolicy(Qt.NoFocus)
        self.popupteams.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.popupteams.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_2.addWidget(self.popupteams, 1, 0, 1, 1)

        self.popuppersons = QListWidget(self.widget_15)
        self.popuppersons.setObjectName(u"popuppersons")
        self.popuppersons.setFont(font5)
        self.popuppersons.setFocusPolicy(Qt.NoFocus)
        self.popuppersons.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.popuppersons.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_2.addWidget(self.popuppersons, 1, 1, 1, 1)


        self.verticalLayout_18.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.popupContainer)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 10, 0)
        self.frame_16 = QFrame(self.widget_16)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.popupsaveBtn = QPushButton(self.frame_16)
        self.popupsaveBtn.setObjectName(u"popupsaveBtn")
        self.popupsaveBtn.setFont(font6)
        self.popupsaveBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.popupsaveBtn.setIcon(icon10)
        self.popupsaveBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_21.addWidget(self.popupsaveBtn)


        self.horizontalLayout_20.addWidget(self.frame_16, 0, Qt.AlignRight)


        self.verticalLayout_18.addWidget(self.widget_16)


        self.verticalLayout_6.addWidget(self.popupContainer, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedplanning.setCurrentIndex(0)
        self.editeteampicker.setCurrentIndex(-1)
        self.editpersonpicker.setCurrentIndex(-1)


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
        self.planningnbheures.setText("")
        self.planningsemaine.setText("")
        self.planningPrevWeekBtn.setText("")
        self.planningNextWeekBtn.setText("")
        self.planningPickerWeekBtn.setText("")
        self.planninglundi.setText("")
        self.planningmardi.setText("")
        self.planningmercredi.setText("")
        self.planningjeudi.setText("")
        self.planningvendredi.setText("")
        self.planningsamedi.setText("")
        self.planningdimanche.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"8h", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"13h", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"18h", None))
        self.editsemaine.setText("")
        self.editpersonpicker.setCurrentText("")
        self.editpersonpicker.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selection employ\u00e9", None))
        self.editPrevWeekBtn.setText("")
        self.editNextWeekBtn.setText("")
        self.editPickerWeekBtn.setText("")
        self.editAddEventBtn.setText("")
        self.editlundi.setText("")
        self.editmardi.setText("")
        self.editmercredi.setText("")
        self.editjeudi.setText("")
        self.editvendredi.setText("")
        self.editsamedi.setText("")
        self.editdimanche.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"8h", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"13h", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"18h", None))
        self.popupeventname.setText(QCoreApplication.translate("MainWindow", u"Activit\u00e9", None))
        self.closepopupBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Date de debut :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Date de fin :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Lieux :", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Type :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Personnes :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Equipes :", None))
        self.popupsaveBtn.setText(QCoreApplication.translate("MainWindow", u" Save", None))
    # retranslateUi

