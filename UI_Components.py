# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLCDNumber, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QToolButton,
    QVBoxLayout, QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 396)
        MainWindow.setStyleSheet(u"/*\n"
"Dark: #16191d\n"
"Accent_1: #1f2322\n"
"Accent_2: #2c313c\n"
"Accent_3: #343b47\n"
"Text_1: #fff\n"
"Text_2: #838ea2\n"
"*/\n"
"\n"
"QMainWindow {\n"
"	\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #fff;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	color: #fff;\n"
"}\n"
"QCheckBox {\n"
"	color: #fff;\n"
"}\n"
"\n"
"\n"
"#centralwidget {\n"
"	background-color: #16191d;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#menuFrame  {\n"
"	background-color: #16191d;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"#menuFrame QToolButton {\n"
"	background-color: #16191d;\n"
"	color: #fff;\n"
"	text-align: left;\n"
"	border: none;\n"
"	padding: 5px 0px 5px 0px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#menuFrame QToolButton:hover {\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"#windowButtonFrame {\n"
"	text-align: center;\n"
"}\n"
"\n"
"#titleFrame {\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"#contentFrame {\n"
"	background-color: #1"
                        "f2322;\n"
"}\n"
"\n"
"#homeWidget {\n"
"	background-color: #1f2322;\n"
"}\n"
"\n"
"#homeWidget QToolButton {\n"
"	background-color: #2c313c;\n"
"	color: #fff;\n"
"	border-radius: 5px;\n"
"	/*border: none;*/\n"
"	padding: 0px 0px 0px 5px;\n"
"}\n"
"\n"
"#kitsWidget {\n"
"	background-color: #1f2322;\n"
"}\n"
"\n"
"#kitsWidget QToolButton {\n"
"	background-color: #2c313c;\n"
"	color: #fff;\n"
"	border-radius: 5px;\n"
"	/*border: none;*/\n"
"	padding: 0px 0px 0px 5px;\n"
"}\n"
"\n"
"#logWidget {\n"
"	background-color: #1f2322;\n"
"}\n"
"\n"
"#midiWidget {\n"
"	background-color: #1f2322;\n"
"	\n"
"}\n"
"\n"
"#midiWidget QGroupBox{\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"\n"
"#midiWidget QRadioButton{\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#midiWidget Line{\n"
"	color: #ffffff;\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"#stackedWidget QLineEdit{\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"#stackedWidget QTableWidget{\n"
"	background-color: #2c313c;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#settingsWidget {\n"
"	background-c"
                        "olor: #1f2322;\n"
"}\n"
"\n"
"#proxyWidget QToolButton {\n"
"	background-color: #2c313c;\n"
"	color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#proxyWidget QRadioButton {\n"
"	color: #fff;\n"
"}\n"
"\n"
"#statusBarFrame {\n"
"	background-color: #16191d;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menuFrame = QFrame(self.centralwidget)
        self.menuFrame.setObjectName(u"menuFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuFrame.sizePolicy().hasHeightForWidth())
        self.menuFrame.setSizePolicy(sizePolicy)
        self.menuFrame.setMinimumSize(QSize(150, 0))
        self.menuFrame.setFrameShape(QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menuFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.menuFrame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.homeMenuButton = QToolButton(self.frame_2)
        self.homeMenuButton.setObjectName(u"homeMenuButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.homeMenuButton.sizePolicy().hasHeightForWidth())
        self.homeMenuButton.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(14)
        self.homeMenuButton.setFont(font)
        self.homeMenuButton.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/resources/img/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeMenuButton.setIcon(icon)
        self.homeMenuButton.setIconSize(QSize(24, 24))
        self.homeMenuButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.homeMenuButton)

        self.drumKitsMenuButton = QToolButton(self.frame_2)
        self.drumKitsMenuButton.setObjectName(u"drumKitsMenuButton")
        sizePolicy2.setHeightForWidth(self.drumKitsMenuButton.sizePolicy().hasHeightForWidth())
        self.drumKitsMenuButton.setSizePolicy(sizePolicy2)
        self.drumKitsMenuButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/resources/img/icons/music.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.drumKitsMenuButton.setIcon(icon1)
        self.drumKitsMenuButton.setIconSize(QSize(24, 24))
        self.drumKitsMenuButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.drumKitsMenuButton)

        self.midiLogMenuButton = QToolButton(self.frame_2)
        self.midiLogMenuButton.setObjectName(u"midiLogMenuButton")
        sizePolicy2.setHeightForWidth(self.midiLogMenuButton.sizePolicy().hasHeightForWidth())
        self.midiLogMenuButton.setSizePolicy(sizePolicy2)
        self.midiLogMenuButton.setFont(font)
        self.midiLogMenuButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/resources/img/icons/headphones.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.midiLogMenuButton.setIcon(icon2)
        self.midiLogMenuButton.setIconSize(QSize(24, 24))
        self.midiLogMenuButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.midiLogMenuButton)

        self.appLogMenuButton = QToolButton(self.frame_2)
        self.appLogMenuButton.setObjectName(u"appLogMenuButton")
        sizePolicy2.setHeightForWidth(self.appLogMenuButton.sizePolicy().hasHeightForWidth())
        self.appLogMenuButton.setSizePolicy(sizePolicy2)
        self.appLogMenuButton.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/resources/img/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.appLogMenuButton.setIcon(icon3)
        self.appLogMenuButton.setIconSize(QSize(24, 24))
        self.appLogMenuButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.appLogMenuButton)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame = QFrame(self.menuFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.settingsButton = QToolButton(self.frame)
        self.settingsButton.setObjectName(u"settingsButton")
        sizePolicy2.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy2)
        self.settingsButton.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/resources/img/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon4)
        self.settingsButton.setIconSize(QSize(24, 24))
        self.settingsButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.settingsButton)

        self.githubButton = QToolButton(self.frame)
        self.githubButton.setObjectName(u"githubButton")
        sizePolicy2.setHeightForWidth(self.githubButton.sizePolicy().hasHeightForWidth())
        self.githubButton.setSizePolicy(sizePolicy2)
        self.githubButton.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/resources/img/icons/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.githubButton.setIcon(icon5)
        self.githubButton.setIconSize(QSize(24, 24))
        self.githubButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.githubButton)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.menuFrame)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy4)
        self.mainFrame.setStyleSheet(u"border: none;\n"
"")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contentFrame = QFrame(self.mainFrame)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setFrameShape(QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.contentFrame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.contentFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMidLineWidth(2)
        self.homeWidget = QWidget()
        self.homeWidget.setObjectName(u"homeWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.homeWidget.sizePolicy().hasHeightForWidth())
        self.homeWidget.setSizePolicy(sizePolicy5)
        self.homeWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_6 = QVBoxLayout(self.homeWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.curKitGroupBox = QGroupBox(self.homeWidget)
        self.curKitGroupBox.setObjectName(u"curKitGroupBox")
        self.curKitGroupBox.setStyleSheet(u"QGroupBox{\n"
"	border: 1px solid white;\n"
"	color: #ffffff;\n"
"}")
        self.curKitLineEdit = QLineEdit(self.curKitGroupBox)
        self.curKitLineEdit.setObjectName(u"curKitLineEdit")
        self.curKitLineEdit.setGeometry(QRect(20, 170, 601, 61))
        font1 = QFont()
        font1.setPointSize(36)
        font1.setBold(False)
        self.curKitLineEdit.setFont(font1)
        self.curKitLineEdit.setReadOnly(True)
        self.curKitSubLineEdit = QLineEdit(self.curKitGroupBox)
        self.curKitSubLineEdit.setObjectName(u"curKitSubLineEdit")
        self.curKitSubLineEdit.setGeometry(QRect(20, 240, 601, 61))
        font2 = QFont()
        font2.setPointSize(36)
        self.curKitSubLineEdit.setFont(font2)
        self.curKitSubLineEdit.setReadOnly(True)
        self.groupBox = QGroupBox(self.curKitGroupBox)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 30, 181, 121))
        self.kitLCD = QLCDNumber(self.groupBox)
        self.kitLCD.setObjectName(u"kitLCD")
        self.kitLCD.setGeometry(QRect(0, 0, 181, 121))
        self.kitLCD.setStyleSheet(u"QLCDNumber {\n"
"	color: #343b47;\n"
"}")
        self.kitLCD.setMidLineWidth(0)
        self.kitLCD.setDigitCount(3)
        self.kitLCD.setMode(QLCDNumber.Dec)
        self.kitLCD.setSegmentStyle(QLCDNumber.Filled)
        self.refreshKitDataButton = QToolButton(self.curKitGroupBox)
        self.refreshKitDataButton.setObjectName(u"refreshKitDataButton")
        self.refreshKitDataButton.setGeometry(QRect(430, 119, 191, 31))
        self.refreshKitDataButton.setFont(font)
        self.refreshKitDataButton.setStyleSheet(u"QToolButton {\n"
"	border-width: 1px;\n"
"	border-width: 1px;\n"
"	border-width: 1px;\n"
" 	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"	border-style:solid;\n"
"	border-width:1px;\n"
"	border-color: #ffffff;\n"
"	margin-left: 3px;\n"
"	margin-top: 3px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/resources/img/icons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshKitDataButton.setIcon(icon6)
        self.refreshKitDataButton.setIconSize(QSize(24, 24))
        self.refreshKitDataButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_6.addWidget(self.curKitGroupBox)

        self.stackedWidget.addWidget(self.homeWidget)
        self.kitsWidget = QWidget()
        self.kitsWidget.setObjectName(u"kitsWidget")
        self.verticalLayout_13 = QVBoxLayout(self.kitsWidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.kitsWidget)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_7)

        self.kitTableWidget = QTableWidget(self.kitsWidget)
        if (self.kitTableWidget.columnCount() < 2):
            self.kitTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.kitTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.kitTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.kitTableWidget.rowCount() < 100):
            self.kitTableWidget.setRowCount(100)
        self.kitTableWidget.setObjectName(u"kitTableWidget")
        self.kitTableWidget.setStyleSheet(u"alternate-background-color: #16191d;")
        self.kitTableWidget.setFrameShape(QFrame.StyledPanel)
        self.kitTableWidget.setAlternatingRowColors(True)
        self.kitTableWidget.setRowCount(100)
        self.kitTableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_13.addWidget(self.kitTableWidget)

        self.stackedWidget.addWidget(self.kitsWidget)
        self.midiWidget = QWidget()
        self.midiWidget.setObjectName(u"midiWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.midiWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.midiFilterFrame = QWidget(self.midiWidget)
        self.midiFilterFrame.setObjectName(u"midiFilterFrame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.midiFilterFrame.sizePolicy().hasHeightForWidth())
        self.midiFilterFrame.setSizePolicy(sizePolicy6)
        self.midiFilterFrame.setMinimumSize(QSize(150, 0))
        self.verticalLayout_8 = QVBoxLayout(self.midiFilterFrame)
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.msgTypeGroupBox = QGroupBox(self.midiFilterFrame)
        self.msgTypeGroupBox.setObjectName(u"msgTypeGroupBox")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.msgTypeGroupBox.sizePolicy().hasHeightForWidth())
        self.msgTypeGroupBox.setSizePolicy(sizePolicy7)
        self.msgTypeGroupBox.setStyleSheet(u"QGroupBox{\n"
"	border: 1px solid white;\n"
"}\n"
"\n"
"Line {\n"
"	color: blue;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.msgTypeGroupBox)
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 21, -1, -1)
        self.midiLogShowSysExCheckBox = QCheckBox(self.msgTypeGroupBox)
        self.midiLogShowSysExCheckBox.setObjectName(u"midiLogShowSysExCheckBox")

        self.verticalLayout_12.addWidget(self.midiLogShowSysExCheckBox)

        self.midiLogShowNoteOnCheckBox = QCheckBox(self.msgTypeGroupBox)
        self.midiLogShowNoteOnCheckBox.setObjectName(u"midiLogShowNoteOnCheckBox")

        self.verticalLayout_12.addWidget(self.midiLogShowNoteOnCheckBox)

        self.midiLogShowNoteOffCheckBox = QCheckBox(self.msgTypeGroupBox)
        self.midiLogShowNoteOffCheckBox.setObjectName(u"midiLogShowNoteOffCheckBox")

        self.verticalLayout_12.addWidget(self.midiLogShowNoteOffCheckBox)

        self.midiLogShowPolyCheckBox = QCheckBox(self.msgTypeGroupBox)
        self.midiLogShowPolyCheckBox.setObjectName(u"midiLogShowPolyCheckBox")

        self.verticalLayout_12.addWidget(self.midiLogShowPolyCheckBox)

        self.midiLogShowProgChangeCheckBox = QCheckBox(self.msgTypeGroupBox)
        self.midiLogShowProgChangeCheckBox.setObjectName(u"midiLogShowProgChangeCheckBox")

        self.verticalLayout_12.addWidget(self.midiLogShowProgChangeCheckBox)

        self.midiLogShowControlChangeCheckBox = QCheckBox(self.msgTypeGroupBox)
        self.midiLogShowControlChangeCheckBox.setObjectName(u"midiLogShowControlChangeCheckBox")

        self.verticalLayout_12.addWidget(self.midiLogShowControlChangeCheckBox)

        self.midiLogShowClockCheckBox = QCheckBox(self.msgTypeGroupBox)
        self.midiLogShowClockCheckBox.setObjectName(u"midiLogShowClockCheckBox")

        self.verticalLayout_12.addWidget(self.midiLogShowClockCheckBox)

        self.line = QFrame(self.msgTypeGroupBox)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"#line {\n"
"	border: 5px solid white;\n"
"}")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line)

        self.midiLogShowAllCheckBox = QCheckBox(self.msgTypeGroupBox)
        self.midiLogShowAllCheckBox.setObjectName(u"midiLogShowAllCheckBox")

        self.verticalLayout_12.addWidget(self.midiLogShowAllCheckBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)


        self.verticalLayout_8.addWidget(self.msgTypeGroupBox)


        self.verticalLayout_5.addWidget(self.midiFilterFrame)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.midiWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.midiLogBrowser = QTextBrowser(self.midiWidget)
        self.midiLogBrowser.setObjectName(u"midiLogBrowser")

        self.verticalLayout_7.addWidget(self.midiLogBrowser)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.stackedWidget.addWidget(self.midiWidget)
        self.logWidget = QWidget()
        self.logWidget.setObjectName(u"logWidget")
        self.verticalLayout_9 = QVBoxLayout(self.logWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_9 = QFrame(self.logWidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 10, 20, 20)
        self.logBrowser = QTextBrowser(self.frame_9)
        self.logBrowser.setObjectName(u"logBrowser")

        self.verticalLayout_10.addWidget(self.logBrowser)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.logWidget)
        self.settingsWidget = QWidget()
        self.settingsWidget.setObjectName(u"settingsWidget")
        self.settingsWidget.setStyleSheet(u"QToolButton {\n"
"	background-color: #2c313c;\n"
"	color: #fff;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
"	padding: 0px 0px 0px 5px;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.settingsWidget)
        self.verticalLayout_11.setSpacing(9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 12, -1, -1)
        self.midiDeviceGroupBox = QGroupBox(self.settingsWidget)
        self.midiDeviceGroupBox.setObjectName(u"midiDeviceGroupBox")
        sizePolicy2.setHeightForWidth(self.midiDeviceGroupBox.sizePolicy().hasHeightForWidth())
        self.midiDeviceGroupBox.setSizePolicy(sizePolicy2)
        self.midiDeviceGroupBox.setMinimumSize(QSize(0, 70))
        self.midiDeviceGroupBox.setStyleSheet(u"QGroupBox{\n"
"	border: 1px solid white;\n"
"	color: #ffffff;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.midiDeviceGroupBox)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 20, -1)
        self.midiDeviceComboBox = QComboBox(self.midiDeviceGroupBox)
        self.midiDeviceComboBox.addItem("")
        self.midiDeviceComboBox.setObjectName(u"midiDeviceComboBox")
        sizePolicy2.setHeightForWidth(self.midiDeviceComboBox.sizePolicy().hasHeightForWidth())
        self.midiDeviceComboBox.setSizePolicy(sizePolicy2)
        self.midiDeviceComboBox.setMinimumSize(QSize(400, 20))

        self.horizontalLayout_5.addWidget(self.midiDeviceComboBox)

        self.refreshDevicesButton = QToolButton(self.midiDeviceGroupBox)
        self.refreshDevicesButton.setObjectName(u"refreshDevicesButton")
        self.refreshDevicesButton.setMinimumSize(QSize(100, 25))
        self.refreshDevicesButton.setStyleSheet(u"QToolButton {\n"
"	border-width: 1px;\n"
"	border-width: 1px;\n"
"	border-width: 1px;\n"
" 	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"	border-style:solid;\n"
"	border-width:1px;\n"
"	border-color: #ffffff;\n"
"	margin-left: 3px;\n"
"	margin-top: 3px;\n"
"}")
        self.refreshDevicesButton.setIcon(icon6)
        self.refreshDevicesButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_5.addWidget(self.refreshDevicesButton)


        self.verticalLayout_11.addWidget(self.midiDeviceGroupBox)

        self.groupBox_4 = QGroupBox(self.settingsWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"QGroupBox{\n"
"	border: 1px solid white;\n"
"	color: #ffffff;\n"
"}")
        self.obsFileLineEdit = QLineEdit(self.groupBox_4)
        self.obsFileLineEdit.setObjectName(u"obsFileLineEdit")
        self.obsFileLineEdit.setGeometry(QRect(20, 51, 471, 21))
        self.obsFileLineEdit.setReadOnly(True)
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 49, 16))
        self.browseFileButton = QToolButton(self.groupBox_4)
        self.browseFileButton.setObjectName(u"browseFileButton")
        self.browseFileButton.setGeometry(QRect(510, 50, 100, 21))
        self.browseFileButton.setStyleSheet(u"QToolButton {\n"
"	border-width: 1px;\n"
"	border-width: 1px;\n"
"	border-width: 1px;\n"
" 	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"	border-style:solid;\n"
"	border-width:1px;\n"
"	border-color: #ffffff;\n"
"	margin-left: 3px;\n"
"	margin-top: 3px;\n"
"}")
        self.browseFileButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.browseFileButton.setAutoRaise(False)
        self.obsFileTemplateEdit = QPlainTextEdit(self.groupBox_4)
        self.obsFileTemplateEdit.setObjectName(u"obsFileTemplateEdit")
        self.obsFileTemplateEdit.setGeometry(QRect(20, 110, 471, 51))
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 49, 16))
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(500, 90, 121, 16))
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(500, 110, 111, 51))

        self.verticalLayout_11.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(self.settingsWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.groupBox_2.setMinimumSize(QSize(0, 70))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"	border: 1px solid white;\n"
"	color: #ffffff;\n"
"}")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 30, 49, 21))
        self.settingsChatBotCheckbox = QCheckBox(self.groupBox_2)
        self.settingsChatBotCheckbox.setObjectName(u"settingsChatBotCheckbox")
        self.settingsChatBotCheckbox.setGeometry(QRect(20, 30, 181, 20))
        self.settingsChatBotCheckbox.setChecked(True)
        self.settingsChannelLineEdit = QLineEdit(self.groupBox_2)
        self.settingsChannelLineEdit.setObjectName(u"settingsChannelLineEdit")
        self.settingsChannelLineEdit.setGeometry(QRect(270, 30, 341, 22))

        self.verticalLayout_11.addWidget(self.groupBox_2)

        self.stackedWidget.addWidget(self.settingsWidget)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.contentFrame)

        self.statusBarFrame = QFrame(self.mainFrame)
        self.statusBarFrame.setObjectName(u"statusBarFrame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.statusBarFrame.sizePolicy().hasHeightForWidth())
        self.statusBarFrame.setSizePolicy(sizePolicy8)
        self.statusBarFrame.setMinimumSize(QSize(0, 30))
        self.statusBarFrame.setFrameShape(QFrame.StyledPanel)
        self.statusBarFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.statusBarFrame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 10, 0)
        self.statusLabel = QLabel(self.statusBarFrame)
        self.statusLabel.setObjectName(u"statusLabel")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.statusLabel.setFont(font4)
        self.statusLabel.setLayoutDirection(Qt.LeftToRight)
        self.statusLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.statusLabel.setMargin(3)

        self.gridLayout.addWidget(self.statusLabel, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.statusBarFrame)


        self.horizontalLayout_4.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeMenuButton.setText(QCoreApplication.translate("MainWindow", u" Home", None))
        self.drumKitsMenuButton.setText(QCoreApplication.translate("MainWindow", u" Drum Kits", None))
        self.midiLogMenuButton.setText(QCoreApplication.translate("MainWindow", u" Midi Log", None))
        self.appLogMenuButton.setText(QCoreApplication.translate("MainWindow", u" App Log", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
        self.githubButton.setText(QCoreApplication.translate("MainWindow", u" Github", None))
        self.curKitGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Current Kit", None))
        self.curKitLineEdit.setText("")
        self.curKitSubLineEdit.setText("")
        self.groupBox.setTitle("")
        self.refreshKitDataButton.setText(QCoreApplication.translate("MainWindow", u"Get Current Kit", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Drum Kit List", None))
        ___qtablewidgetitem = self.kitTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.kitTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Subname", None));
        self.msgTypeGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Message Type", None))
        self.midiLogShowSysExCheckBox.setText(QCoreApplication.translate("MainWindow", u"Sys Ex", None))
        self.midiLogShowNoteOnCheckBox.setText(QCoreApplication.translate("MainWindow", u"Note On", None))
        self.midiLogShowNoteOffCheckBox.setText(QCoreApplication.translate("MainWindow", u"Note Off", None))
        self.midiLogShowPolyCheckBox.setText(QCoreApplication.translate("MainWindow", u"Polytouch", None))
        self.midiLogShowProgChangeCheckBox.setText(QCoreApplication.translate("MainWindow", u"Prog Change", None))
        self.midiLogShowControlChangeCheckBox.setText(QCoreApplication.translate("MainWindow", u"Control Change", None))
        self.midiLogShowClockCheckBox.setText(QCoreApplication.translate("MainWindow", u"Timing Clock", None))
        self.midiLogShowAllCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show Everything", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Midi Log", None))
        self.midiDeviceGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Midi Devices", None))
        self.midiDeviceComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select a MIDI Device", None))

        self.refreshDevicesButton.setText(QCoreApplication.translate("MainWindow", u" Refresh", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"OBS Overlay File", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Path:", None))
#if QT_CONFIG(tooltip)
        self.browseFileButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.browseFileButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.browseFileButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.obsFileTemplateEdit.setPlainText(QCoreApplication.translate("MainWindow", u"{kit_num} {kit_name} {kit_subname}", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contents:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Template Keywords:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"{kit_num}\n"
"{kit_name}\n"
"{kit_subname}", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Chat Bot", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Channel:", None))
        self.settingsChatBotCheckbox.setText(QCoreApplication.translate("MainWindow", u"Send Data To Chat Bot", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"KitConnect Launching", None))
    # retranslateUi



