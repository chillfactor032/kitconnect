# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
    QGridLayout, QGroupBox, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextBrowser,
    QToolButton, QVBoxLayout, QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 613)
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
"	background-color: #1f2322;\n"
"}\n"
"\n"
"#kitsWidg"
                        "et {\n"
"	background-color: #1f2322;\n"
"}\n"
"\n"
"#kitsWidget QToolButton {\n"
"	background-color: #2c313c;\n"
"	color: #fff;\n"
"	border-radius: 5px;\n"
"	border: none;\n"
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
        self.topSpacerFrame = QFrame(self.menuFrame)
        self.topSpacerFrame.setObjectName(u"topSpacerFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.topSpacerFrame.sizePolicy().hasHeightForWidth())
        self.topSpacerFrame.setSizePolicy(sizePolicy1)
        self.topSpacerFrame.setMinimumSize(QSize(0, 30))
        self.topSpacerFrame.setFrameShape(QFrame.StyledPanel)
        self.topSpacerFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.topSpacerFrame)

        self.frame_2 = QFrame(self.menuFrame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.homeMenuButton = QToolButton(self.frame_2)
        self.homeMenuButton.setObjectName(u"homeMenuButton")
        sizePolicy1.setHeightForWidth(self.homeMenuButton.sizePolicy().hasHeightForWidth())
        self.homeMenuButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(14)
        self.homeMenuButton.setFont(font)
        self.homeMenuButton.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/resources/img/icons/music.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeMenuButton.setIcon(icon)
        self.homeMenuButton.setIconSize(QSize(24, 24))
        self.homeMenuButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.homeMenuButton)

        self.midiLogMenuButton = QToolButton(self.frame_2)
        self.midiLogMenuButton.setObjectName(u"midiLogMenuButton")
        self.midiLogMenuButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/resources/img/icons/headphones.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.midiLogMenuButton.setIcon(icon1)
        self.midiLogMenuButton.setIconSize(QSize(24, 24))
        self.midiLogMenuButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.midiLogMenuButton)

        self.appLogMenuButton = QToolButton(self.frame_2)
        self.appLogMenuButton.setObjectName(u"appLogMenuButton")
        sizePolicy1.setHeightForWidth(self.appLogMenuButton.sizePolicy().hasHeightForWidth())
        self.appLogMenuButton.setSizePolicy(sizePolicy1)
        self.appLogMenuButton.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/resources/img/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.appLogMenuButton.setIcon(icon2)
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
        self.aboutButton = QToolButton(self.frame)
        self.aboutButton.setObjectName(u"aboutButton")
        sizePolicy1.setHeightForWidth(self.aboutButton.sizePolicy().hasHeightForWidth())
        self.aboutButton.setSizePolicy(sizePolicy1)
        self.aboutButton.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/resources/img/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutButton.setIcon(icon3)
        self.aboutButton.setIconSize(QSize(24, 24))
        self.aboutButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.aboutButton)

        self.githubButton = QToolButton(self.frame)
        self.githubButton.setObjectName(u"githubButton")
        sizePolicy1.setHeightForWidth(self.githubButton.sizePolicy().hasHeightForWidth())
        self.githubButton.setSizePolicy(sizePolicy1)
        self.githubButton.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/resources/img/icons/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.githubButton.setIcon(icon4)
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
        self.titleFrame = QFrame(self.mainFrame)
        self.titleFrame.setObjectName(u"titleFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.titleFrame.sizePolicy().hasHeightForWidth())
        self.titleFrame.setSizePolicy(sizePolicy5)
        self.titleFrame.setMinimumSize(QSize(0, 30))
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleFrame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.titleLabel = QLabel(self.titleFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy6)
        self.titleLabel.setMinimumSize(QSize(400, 0))
        self.titleLabel.setFont(font)
        self.titleLabel.setCursor(QCursor(Qt.SizeAllCursor))
        self.titleLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.titleLabel)

        self.windowButtonFrame = QFrame(self.titleFrame)
        self.windowButtonFrame.setObjectName(u"windowButtonFrame")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.windowButtonFrame.sizePolicy().hasHeightForWidth())
        self.windowButtonFrame.setSizePolicy(sizePolicy7)
        self.windowButtonFrame.setMinimumSize(QSize(100, 0))
        self.windowButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.windowButtonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.windowButtonFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QToolButton(self.windowButtonFrame)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(24, 24))
        icon5 = QIcon()
        icon5.addFile(u":/resources/img/icons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon5)
        self.minimizeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeButton)

        self.maximizeButton = QToolButton(self.windowButtonFrame)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setMinimumSize(QSize(24, 24))
        icon6 = QIcon()
        icon6.addFile(u":/resources/img/icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeButton.setIcon(icon6)
        self.maximizeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeButton)

        self.closeButton = QToolButton(self.windowButtonFrame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(24, 24))
        icon7 = QIcon()
        icon7.addFile(u":/resources/img/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon7)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeButton)


        self.horizontalLayout.addWidget(self.windowButtonFrame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.titleFrame)

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
        self.kitsWidget = QWidget()
        self.kitsWidget.setObjectName(u"kitsWidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.kitsWidget.sizePolicy().hasHeightForWidth())
        self.kitsWidget.setSizePolicy(sizePolicy8)
        self.kitsWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_6 = QVBoxLayout(self.kitsWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.devicesGroupBox = QGroupBox(self.kitsWidget)
        self.devicesGroupBox.setObjectName(u"devicesGroupBox")
        sizePolicy5.setHeightForWidth(self.devicesGroupBox.sizePolicy().hasHeightForWidth())
        self.devicesGroupBox.setSizePolicy(sizePolicy5)
        self.devicesGroupBox.setMinimumSize(QSize(0, 75))
        self.devicesGroupBox.setStyleSheet(u"QGroupBox{\n"
"	border: 1px solid white;\n"
"	color: #ffffff;\n"
"}\n"
"")
        self.refreshDevicesButton = QToolButton(self.devicesGroupBox)
        self.refreshDevicesButton.setObjectName(u"refreshDevicesButton")
        self.refreshDevicesButton.setGeometry(QRect(480, 20, 121, 31))
        self.refreshDevicesButton.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/resources/img/icons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshDevicesButton.setIcon(icon8)
        self.refreshDevicesButton.setIconSize(QSize(24, 24))
        self.refreshDevicesButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.deviceComboBox = QComboBox(self.devicesGroupBox)
        self.deviceComboBox.setObjectName(u"deviceComboBox")
        self.deviceComboBox.setGeometry(QRect(20, 30, 401, 18))

        self.verticalLayout_6.addWidget(self.devicesGroupBox)

        self.curKitGroupBox = QGroupBox(self.kitsWidget)
        self.curKitGroupBox.setObjectName(u"curKitGroupBox")
        self.curKitGroupBox.setStyleSheet(u"QGroupBox{\n"
"	border: 1px solid white;\n"
"	color: #ffffff;\n"
"}")
        self.curKitLineEdit = QLineEdit(self.curKitGroupBox)
        self.curKitLineEdit.setObjectName(u"curKitLineEdit")
        self.curKitLineEdit.setGeometry(QRect(220, 40, 401, 51))
        font1 = QFont()
        font1.setPointSize(24)
        self.curKitLineEdit.setFont(font1)
        self.curKitSubLineEdit = QLineEdit(self.curKitGroupBox)
        self.curKitSubLineEdit.setObjectName(u"curKitSubLineEdit")
        self.curKitSubLineEdit.setGeometry(QRect(220, 110, 401, 51))
        self.curKitSubLineEdit.setFont(font1)
        self.getCurKitButton = QToolButton(self.curKitGroupBox)
        self.getCurKitButton.setObjectName(u"getCurKitButton")
        self.getCurKitButton.setGeometry(QRect(480, 170, 141, 31))
        self.getCurKitButton.setFont(font)
        self.getCurKitButton.setIcon(icon8)
        self.getCurKitButton.setIconSize(QSize(24, 24))
        self.getCurKitButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.kitLeftButton = QToolButton(self.curKitGroupBox)
        self.kitLeftButton.setObjectName(u"kitLeftButton")
        self.kitLeftButton.setGeometry(QRect(20, 170, 41, 31))
        self.kitLeftButton.setFont(font)
        icon9 = QIcon()
        icon9.addFile(u":/resources/img/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.kitLeftButton.setIcon(icon9)
        self.kitLeftButton.setIconSize(QSize(24, 24))
        self.kitLeftButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.kitRightButton = QToolButton(self.curKitGroupBox)
        self.kitRightButton.setObjectName(u"kitRightButton")
        self.kitRightButton.setGeometry(QRect(160, 170, 41, 31))
        self.kitRightButton.setFont(font)
        icon10 = QIcon()
        icon10.addFile(u":/resources/img/icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.kitRightButton.setIcon(icon10)
        self.kitRightButton.setIconSize(QSize(24, 24))
        self.kitRightButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.groupBox = QGroupBox(self.curKitGroupBox)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 40, 181, 121))
        self.kitLCD = QLCDNumber(self.groupBox)
        self.kitLCD.setObjectName(u"kitLCD")
        self.kitLCD.setGeometry(QRect(0, 0, 181, 121))
        self.kitLCD.setDigitCount(3)
        self.kitLCD.setMode(QLCDNumber.Dec)
        self.kitLCD.setSegmentStyle(QLCDNumber.Outline)

        self.verticalLayout_6.addWidget(self.curKitGroupBox)

        self.widget = QWidget(self.kitsWidget)
        self.widget.setObjectName(u"widget")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 390, 61, 21))
        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(90, 390, 113, 22))
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(30, 360, 181, 20))
        self.checkBox_2 = QCheckBox(self.widget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(240, 380, 181, 20))

        self.verticalLayout_6.addWidget(self.widget)

        self.stackedWidget.addWidget(self.kitsWidget)
        self.midiWidget = QWidget()
        self.midiWidget.setObjectName(u"midiWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.midiWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.midiFilterFrame = QWidget(self.midiWidget)
        self.midiFilterFrame.setObjectName(u"midiFilterFrame")
        sizePolicy7.setHeightForWidth(self.midiFilterFrame.sizePolicy().hasHeightForWidth())
        self.midiFilterFrame.setSizePolicy(sizePolicy7)
        self.midiFilterFrame.setMinimumSize(QSize(150, 0))
        self.verticalLayout_8 = QVBoxLayout(self.midiFilterFrame)
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.msgFormatGroupBox = QGroupBox(self.midiFilterFrame)
        self.msgFormatGroupBox.setObjectName(u"msgFormatGroupBox")
        sizePolicy5.setHeightForWidth(self.msgFormatGroupBox.sizePolicy().hasHeightForWidth())
        self.msgFormatGroupBox.setSizePolicy(sizePolicy5)
        self.msgFormatGroupBox.setMinimumSize(QSize(0, 150))
        self.msgFormatGroupBox.setStyleSheet(u"QGroupBox{\n"
"	border: 1px solid white;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.msgFormatGroupBox)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 12, -1, -1)
        self.humanReadableCheckBox = QCheckBox(self.msgFormatGroupBox)
        self.humanReadableCheckBox.setObjectName(u"humanReadableCheckBox")

        self.verticalLayout_11.addWidget(self.humanReadableCheckBox)

        self.midiFilterLine = QFrame(self.msgFormatGroupBox)
        self.midiFilterLine.setObjectName(u"midiFilterLine")
        self.midiFilterLine.setFrameShape(QFrame.HLine)
        self.midiFilterLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.midiFilterLine)

        self.hexRadioButton = QRadioButton(self.msgFormatGroupBox)
        self.hexRadioButton.setObjectName(u"hexRadioButton")

        self.verticalLayout_11.addWidget(self.hexRadioButton)

        self.decRadioButton = QRadioButton(self.msgFormatGroupBox)
        self.decRadioButton.setObjectName(u"decRadioButton")

        self.verticalLayout_11.addWidget(self.decRadioButton)


        self.verticalLayout_8.addWidget(self.msgFormatGroupBox)

        self.msgTypeGroupBox = QGroupBox(self.midiFilterFrame)
        self.msgTypeGroupBox.setObjectName(u"msgTypeGroupBox")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.msgTypeGroupBox.sizePolicy().hasHeightForWidth())
        self.msgTypeGroupBox.setSizePolicy(sizePolicy9)
        self.msgTypeGroupBox.setStyleSheet(u"QGroupBox{\n"
"	border: 1px solid white;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.msgTypeGroupBox)
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 21, -1, -1)
        self.sysexRadioButton = QCheckBox(self.msgTypeGroupBox)
        self.sysexRadioButton.setObjectName(u"sysexRadioButton")

        self.verticalLayout_12.addWidget(self.sysexRadioButton)

        self.progRadioButton = QCheckBox(self.msgTypeGroupBox)
        self.progRadioButton.setObjectName(u"progRadioButton")

        self.verticalLayout_12.addWidget(self.progRadioButton)

        self.chanRadioButton = QCheckBox(self.msgTypeGroupBox)
        self.chanRadioButton.setObjectName(u"chanRadioButton")

        self.verticalLayout_12.addWidget(self.chanRadioButton)

        self.timingRadioButton = QCheckBox(self.msgTypeGroupBox)
        self.timingRadioButton.setObjectName(u"timingRadioButton")

        self.verticalLayout_12.addWidget(self.timingRadioButton)

        self.allRadioButton = QCheckBox(self.msgTypeGroupBox)
        self.allRadioButton.setObjectName(u"allRadioButton")

        self.verticalLayout_12.addWidget(self.allRadioButton)

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
        self.frame_8 = QFrame(self.logWidget)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy10)
        self.frame_8.setMinimumSize(QSize(0, 60))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_8)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(20, 0, 20, 0)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.showErrorsCheckbox = QCheckBox(self.frame_8)
        self.showErrorsCheckbox.setObjectName(u"showErrorsCheckbox")
        self.showErrorsCheckbox.setMinimumSize(QSize(20, 0))

        self.gridLayout_3.addWidget(self.showErrorsCheckbox, 1, 0, 1, 1)

        self.showDebugCheckbox = QCheckBox(self.frame_8)
        self.showDebugCheckbox.setObjectName(u"showDebugCheckbox")

        self.gridLayout_3.addWidget(self.showDebugCheckbox, 1, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.logWidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 10, 20, 20)
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        sizePolicy10.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy10)
        self.label_5.setMinimumSize(QSize(0, 30))

        self.verticalLayout_10.addWidget(self.label_5)

        self.logBrowser = QTextBrowser(self.frame_9)
        self.logBrowser.setObjectName(u"logBrowser")

        self.verticalLayout_10.addWidget(self.logBrowser)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.logWidget)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.contentFrame)

        self.statusBarFrame = QFrame(self.mainFrame)
        self.statusBarFrame.setObjectName(u"statusBarFrame")
        sizePolicy5.setHeightForWidth(self.statusBarFrame.sizePolicy().hasHeightForWidth())
        self.statusBarFrame.setSizePolicy(sizePolicy5)
        self.statusBarFrame.setMinimumSize(QSize(0, 30))
        self.statusBarFrame.setFrameShape(QFrame.StyledPanel)
        self.statusBarFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.statusBarFrame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 10, 0)
        self.statusLabel = QLabel(self.statusBarFrame)
        self.statusLabel.setObjectName(u"statusLabel")

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
        self.homeMenuButton.setText(QCoreApplication.translate("MainWindow", u" Drum Kits", None))
        self.midiLogMenuButton.setText(QCoreApplication.translate("MainWindow", u" Midi Log", None))
        self.appLogMenuButton.setText(QCoreApplication.translate("MainWindow", u" App Log", None))
        self.aboutButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.githubButton.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"KitConnect TD-50X Midi GUI Client", None))
        self.minimizeButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.maximizeButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.devicesGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Midi Device", None))
        self.refreshDevicesButton.setText(QCoreApplication.translate("MainWindow", u" Refresh", None))
        self.curKitGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Current Kit", None))
        self.curKitLineEdit.setText(QCoreApplication.translate("MainWindow", u"Trash Noiser", None))
        self.curKitSubLineEdit.setText(QCoreApplication.translate("MainWindow", u"My Favorite Kit", None))
        self.getCurKitButton.setText(QCoreApplication.translate("MainWindow", u" Refresh Kit", None))
        self.kitLeftButton.setText(QCoreApplication.translate("MainWindow", u" Refresh Kit", None))
        self.kitRightButton.setText(QCoreApplication.translate("MainWindow", u" Refresh Kit", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"HTML File", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"~/chill/kit.html", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Write Kit Info To HTML File", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Send Kit Info to BackBeatBot", None))
        self.msgFormatGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Message Format", None))
        self.humanReadableCheckBox.setText(QCoreApplication.translate("MainWindow", u"Human Readable", None))
        self.hexRadioButton.setText(QCoreApplication.translate("MainWindow", u"Hex", None))
        self.decRadioButton.setText(QCoreApplication.translate("MainWindow", u"Decimal", None))
        self.msgTypeGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Message Type", None))
        self.sysexRadioButton.setText(QCoreApplication.translate("MainWindow", u"Sys Ex", None))
        self.progRadioButton.setText(QCoreApplication.translate("MainWindow", u"Prog Change", None))
        self.chanRadioButton.setText(QCoreApplication.translate("MainWindow", u"Channel Mode", None))
        self.timingRadioButton.setText(QCoreApplication.translate("MainWindow", u"Timing Clock", None))
        self.allRadioButton.setText(QCoreApplication.translate("MainWindow", u"Everything Else", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Midi Log", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Log Settings:", None))
        self.showErrorsCheckbox.setText(QCoreApplication.translate("MainWindow", u"Show Errors", None))
        self.showDebugCheckbox.setText(QCoreApplication.translate("MainWindow", u"Show Debug", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Log:", None))
        self.statusLabel.setText("")
    # retranslateUi



