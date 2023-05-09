import json
import os
import datetime
import sys
from enum import Enum

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle, QMessageBox, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget, QToolButton
from PySide6.QtCore import Qt, QSettings, QFile, QTextStream, QStandardPaths, QPoint, QTimer, QUrl, QSize, Signal, QObject, QRunnable, QThreadPool
from PySide6.QtGui import QPixmap, QIcon, QDesktopServices, QIntValidator, QMovie

import Resources_rc
from UI_Components import Ui_MainWindow
from td50x import LogLevel, TD50X

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load UI Components
        self.setupUi(self)
        
        # App Variables
        self.geometryToRestore = None
        self.repoUrl = QUrl("https://github.com/chillfactor032/kitconnect")
        self.midi_devices = []
        self.showDebug = True
        self.showError = True
        self.current_kit_id = 100

        # Read Version File From Resources
        version_file = QFile(":version.json")
        version_file.open(QFile.ReadOnly)
        text_stream = QTextStream(version_file)
        version_file_text = text_stream.readAll()
        self.version_dict = json.loads(version_file_text)
        self.app_name = self.version_dict["product_name"]
        self.version = self.version_dict["version"]
        self.description = self.version_dict["description"]
        self.author = self.version_dict["author"]
        self.author_email = self.version_dict["author_email"]
        self.project_name = self.app_name.title().replace(" ", "")
        self.setWindowTitle(f"{self.app_name} {self.version}")
        
        # Load Settings
        self.config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        if(not os.path.isdir(self.config_dir)):
            os.mkdir(self.config_dir)
        self.ini_path = os.path.join(self.config_dir, f"kitconnectgui.ini").replace("\\", "/")
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)

        # Button/Menu Signals
        self.closeButton.clicked.connect(self.closeButtonClicked)
        self.minimizeButton.clicked.connect(self.minimizedButtonClicked)
        self.maximizeButton.clicked.connect(self.maximizedButtonClicked)
        self.appLogMenuButton.clicked.connect(self.showLogPane)
        self.homeMenuButton.clicked.connect(self.showHomePane)
        self.midiLogMenuButton.clicked.connect(self.showMidiLogPane)
        self.aboutButton.clicked.connect(self.showAbout)
        self.githubButton.clicked.connect(self.showGithub)
        self.refreshDevicesButton.clicked.connect(self.refreshDevices)
        self.deviceComboBox.currentIndexChanged.connect(self.deviceSelected)
        self.kitRightButton.clicked.connect(self.selectNextKitRight)
        self.kitLeftButton.clicked.connect(self.selectNextKitLeft)
        self.getCurKitButton.clicked.connect(self.refreshKit)

        # TD-50X Object
        self.td50x = TD50X()
        self.td50x.signals.log.connect(self.log)
        self.td50x.signals.midi_msg.connect(self.log_midi)

        # ThreadPool
        self.threadpool = QThreadPool()

        # Finally, Show the UI
        self.stackedWidget.setCurrentWidget(self.kitsWidget)
        geometry = self.settings.value(f"{self.project_name}/geometry")
        window_state = self.settings.value(f"{self.project_name}/windowState")
        if(geometry and window_state):
            self.restoreGeometry(geometry) 
            self.restoreState(window_state)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()
        self.log("KitConnect started")

    def refreshDevices(self):
        print("Refresh Devices")
        self.deviceComboBox.clear()
        self.deviceComboBox.addItem("Select a device", None)
        self.midi_devices = self.td50x.get_devices()
        for device in self.midi_devices:
            self.deviceComboBox.addItem(device["desc"], device)

    def deviceSelected(self, index):
        if index <= 0:
            return
        print(f"Device Selected: {index}")
        device = self.deviceComboBox.currentData()
        self.td50x.update_devices(device["input_id"], device["output_id"])

    def refreshKit(self):
        print("Refresh Kit")

    def selectNextKitLeft(self):
        print("Select Next Kit <")
        self.current_kit_id = (self.current_kit_id - 1) % 128
        msg = [0xC9, self.current_kit_id, 0x00, 0x7F]
        self.td50x.send_msg(msg)

    def selectNextKitRight(self):
        print("Select Next Kit >")
        self.current_kit_id = (self.current_kit_id - 1) % 128
        msg = [0xC9, self.current_kit_id, 0x00, 0x7F]
        self.td50x.send_msg(msg)

    def showAbout(self):
        repo = self.repoUrl.toString()
        text = f"KitConnect TD-50X Midi GUI Client\n\n{self.description}\n\nGitHub: {repo}\nAuthor: {self.author} <{self.author_email}>"
        mb = QMessageBox(QMessageBox.Icon.Information, "About", text)
        mb.setTextInteractionFlags(Qt.TextSelectableByMouse)
        mb.exec()

    def showGithub(self):
        QDesktopServices.openUrl(self.repoUrl)

    def showHomePane(self):
        self.stackedWidget.setCurrentWidget(self.kitsWidget)

    def showLogPane(self):
        self.stackedWidget.setCurrentWidget(self.logWidget)

    def showMidiLogPane(self):
        self.stackedWidget.setCurrentWidget(self.midiWidget)

    def log_midi(self, type_int, incoming, data):
        msg = " > "
        if incoming:
            msg = " < "
        msg += str(TD50X.to_str(data))
        msg = f'<span style="">{msg}</span>'
        self.midiLogBrowser.append(msg)

    def log(self, msg, level=LogLevel.INFO):
        print(msg)
        if not msg:
            return
        if level == LogLevel.ERROR:
            if not self.showErrors:
                return
            style = "color: #cc0000;"
        elif level == LogLevel.DEBUG:
            if not self.showDebug:
                return
            style = "color: #006600;"
        else:
            style = "color: #000000;"
        now = datetime.datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        msg = f'<span style="{style}">{timestamp} - {msg}</span>'
        self.logBrowser.append(msg)

    def mousePressEvent(self, event):
        globalPos = event.globalPosition().toPoint()
        relativePos = event.position().toPoint()
        source = self.childAt(relativePos)
        if source == self.titleLabel:
            self.oldPos = globalPos

    def mouseMoveEvent(self, event):
        globalPos = event.globalPosition().toPoint()
        relativePos = event.position().toPoint()
        source = self.childAt(relativePos)
        if source == self.titleLabel:
            delta = QPoint(globalPos - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = globalPos

    def minimizedButtonClicked(self):
        self.setWindowState(Qt.WindowMinimized)

    def maximizedButtonClicked(self):
        if self.isMaximized():
            #Restore the non-maximized window geometry
            self.restoreGeometry(self.geometryToRestore)
        else:
            #Save window geometry before minimizing
            self.geometryToRestore = self.saveGeometry()
            self.setWindowState(Qt.WindowMaximized)

    def closeButtonClicked(self):
        self.close()

    # App is closing, cleanup
    def closeEvent(self, evt=None):
        # Remember the size and position of the GUI
        self.settings.setValue(f"{self.project_name}/geometry", self.saveGeometry())
        self.settings.setValue(f"{self.project_name}/windowState", self.saveState())
        self.settings.sync()
        evt.accept()


# Start the PySide6 App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    version_file = QFile(":version.json")
    version_file.open(QFile.ReadOnly)
    text_stream = QTextStream(version_file)
    version_file_text = text_stream.readAll()
    version_dict = json.loads(version_file_text)
    org_name = version_dict["company_name"]
    app_name = version_dict["product_name"]
    version = version_dict["version"]
    app.setOrganizationName(org_name)
    app.setApplicationName(app_name)
    app.setApplicationVersion(version)
    window = MainWindow()
    sys.exit(app.exec())