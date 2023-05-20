import json
import os
import datetime
import sys
import base64
import requests
from enum import Enum
from threading import Thread

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QStyle, QMessageBox, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget, QToolButton
from PySide6.QtCore import Qt, QSettings, QFile, QTextStream, QStandardPaths, QPoint, QTimer, QUrl, QSize, Signal, QObject, QRunnable, QThreadPool
from PySide6.QtGui import QPixmap, QIcon, QDesktopServices, QIntValidator, QMovie, QCursor

import Resources_rc
from UI_Components import Ui_MainWindow
from td50x import TD50X

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load UI Components
        self.setupUi(self)
        
        # App Variables
        self.geometryToRestore = None
        self.repoUrl = QUrl("https://github.com/chillfactor032/kitconnect")
        self.midi_devices = []
        self.current_kit_id = 100
        self.midi_log_entries = 0
        self.midi_log_max_entries = 10000
        self.midi_log_filter = []
        self.midi_log_filter_possible_values = ['sysex', 'note_on', 'note_off', 'polytouch', 'program_change', 'control_change', 'clock', 'all']
        self.twitchbot_key = "1234"

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
        self.documents = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        if(not os.path.isdir(self.config_dir)):
            os.mkdir(self.config_dir)
        self.ini_path = os.path.join(self.config_dir, f"kitconnectgui.ini").replace("\\", "/")
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)

        # Read Settings
        self.testport_midi_enabled = self.settings.value(f"{self.project_name}/EnableTestPortMidiDevice", "0") == "1"
        self.obsFilePath = self.settings.value(f"{self.project_name}/OBSFilePath", "")
        self.device = self.settings.value(f"{self.project_name}/MidiDevice", "")
        b64_template_str = self.settings.value(f"{self.project_name}/OBSFileTemplate", "e2tpdF9udW19IHtraXRfbmFtZX0ge2tpdF9zdWJuYW1lfQ==")
        template_str = base64.b64decode(b64_template_str.encode("utf-8")).decode("utf-8")
        self.obsFileTemplateEdit.setPlainText(template_str)
        self.chatBotCommsEnabled = self.settings.value(f"{self.project_name}/ChatBotCommsEnabled", "0") == "1"
        self.twitch_channel = self.settings.value(f"{self.project_name}/TwitchChannel", "")
        self.midiLogShowSysExCheckBox.setChecked(self.settings.value(f"MidiLogFilter/SysEx", "1") == "1")
        self.midiLogShowNoteOnCheckBox.setChecked(self.settings.value(f"MidiLogFilter/NoteOn", "1") == "1")
        self.midiLogShowNoteOffCheckBox.setChecked(self.settings.value(f"MidiLogFilter/NoteOff", "1") == "1")
        self.midiLogShowPolyCheckBox.setChecked(self.settings.value(f"MidiLogFilter/Poly", "1") == "1")
        self.midiLogShowProgChangeCheckBox.setChecked(self.settings.value(f"MidiLogFilter/ProgramChange", "1") == "1")
        self.midiLogShowControlChangeCheckBox.setChecked(self.settings.value(f"MidiLogFilter/ControlChange", "1") == "1")
        self.midiLogShowClockCheckBox.setChecked(self.settings.value(f"MidiLogFilter/Clock", "0") == "1")
        self.midiLogShowAllCheckBox.setChecked(self.settings.value(f"MidiLogFilter/All", "1") == "1")
        if self.midiLogShowSysExCheckBox.isChecked():
            self.midi_log_filter.append("sysex")
        if self.midiLogShowNoteOnCheckBox.isChecked():
            self.midi_log_filter.append("note_on")
        if self.midiLogShowNoteOffCheckBox.isChecked():
            self.midi_log_filter.append("note_off")
        if self.midiLogShowPolyCheckBox.isChecked():
            self.midi_log_filter.append("poly")
        if self.midiLogShowProgChangeCheckBox.isChecked():
            self.midi_log_filter.append("program_change")
        if self.midiLogShowControlChangeCheckBox.isChecked():
            self.midi_log_filter.append("control_change")
        if self.midiLogShowClockCheckBox.isChecked():
            self.midi_log_filter.append("clock")
        if self.midiLogShowAllCheckBox.isChecked():
            self.midi_log_filter.append("all")

        # Navigation Bar Button Signals
        self.homeMenuButton.clicked.connect(self.navBarButtonClicked)
        self.midiLogMenuButton.clicked.connect(self.navBarButtonClicked)
        self.appLogMenuButton.clicked.connect(self.navBarButtonClicked)
        self.settingsButton.clicked.connect(self.navBarButtonClicked)
        self.githubButton.clicked.connect(self.navBarButtonClicked)

        # Other Button/Widget Signals
        self.midiDeviceComboBox.currentIndexChanged.connect(self.deviceSelected)
        self.getCurKitButton.clicked.connect(self.refreshKit)
        self.refreshDevicesButton.clicked.connect(self.refreshDevices)
        self.browseFileButton.clicked.connect(self.browseOBSFile)
        self.settingsChatBotCheckbox.stateChanged.connect(self.chatBotCheckBoxChanged)
        self.settingsChannelLineEdit.editingFinished.connect(self.twitchChannelChanged)

        # Set Midi Filter Checkbox Signals
        self.midiLogShowSysExCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowNoteOnCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowNoteOffCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowPolyCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowProgChangeCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowControlChangeCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowClockCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowAllCheckBox.stateChanged.connect(self.midiFilterChanged)

        # TD-50X Object
        self.td50x = None

        # ThreadPool
        self.threadpool = QThreadPool()

        # Finally, Show the UI
        self.log("KitConnect started")
        self.stackedWidget.setCurrentWidget(self.kitsWidget)
        self.obsFileLineEdit.setText(self.obsFilePath)
        self.settingsChannelLineEdit.setText(self.twitch_channel)
        self.chatBotCheckBoxChanged()
        self.twitchChannelChanged()
        self.settingsChatBotCheckbox.setChecked(self.chatBotCommsEnabled)
        geometry = self.settings.value(f"{self.project_name}/geometry")
        window_state = self.settings.value(f"{self.project_name}/windowState")
        if(geometry and window_state):
            self.restoreGeometry(geometry) 
            self.restoreState(window_state)
        if self.testport_midi_enabled:
            self.log("Test MIDI Device TestPort Enabled")
        self.log(f"Midi Log Filter:")
        self.log(self.midi_log_filter)
        self.refreshDevices()
        self.show()

    def refreshDevices(self):
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        if self.td50x: 
            self.closeTD50X()
        self.midiDeviceComboBox.clear()
        self.midi_devices = TD50X.get_midi_devices()
        self.log("Refreshing MIDI Device List:")
        self.log(str(self.midi_devices))
        self.midiDeviceComboBox.addItem("Select a MIDI Device", None)
        if self.testport_midi_enabled:
            self.midi_devices.append("TestPort")
        for device in self.midi_devices:
            self.midiDeviceComboBox.addItem(device, device)
        self.status("MIDI devices refreshed.", 3000)
        # Try to auto-connect to previous Midi Device
        if self.device in self.midi_devices:
            self.midiDeviceComboBox.setCurrentText(self.device)
        QApplication.restoreOverrideCursor()
    
    def createTD50X(self, device):
        if self.td50x is not None:
            self.td50x.midi_stop()
        self.td50x = TD50X(device)
        self.device = device
        self.td50x.signals.midi_send.connect(self.midi_send)
        self.td50x.signals.midi_recv.connect(self.midi_recv)
        self.td50x.signals.kit_chg.connect(self.kit_updated)
        self.td50x.midi_start()

    def closeTD50X(self):
        if self.td50x:
            self.log(f"Disconnecting old MIDI device [{self.td50x.port_name}]")
            self.td50x.midi_stop()
            self.td50x = None
            self.log("MIDI Device Disconnected")
        
    def deviceSelected(self, index):
        self.closeTD50X()
        if index <= 0:
            return
        self.device = self.midiDeviceComboBox.currentData()
        self.log(f"MIDI Device Selected: {self.device}")
        self.createTD50X(self.device)

    def kit_updated(self, num, name, subname):
        self.kitLCD.display(int(num))
        self.curKitLineEdit.setText(name)
        self.curKitSubLineEdit.setText(subname)
        if not os.path.exists(self.obsFilePath):
            return
        template_str = self.obsFileTemplateEdit.document().toPlainText()
        out_str = template_str.replace("{kit_num}", str(num))
        out_str = out_str.replace("{kit_name}", name)
        out_str = out_str.replace("{kit_subname}", subname)
        try:
            with open(self.obsFilePath, "w") as file:
                file.write(out_str)
        except Exception as e:
            self.log("Error: "+str(e))
        self.updateChatBotKit(self.twitchbot_key, self.twitch_channel, num, name, subname)

    # Select the file to write kit into to for OBS
    def browseOBSFile(self):
        selection = QFileDialog.getOpenFileName(self, "Select OBS Kit File", self.documents)
        if selection is None:
            return
        file = selection[0]
        if not os.path.exists(file):
            QMessageBox.Critical(self, "Error", "The file does not exist.")
            return
        self.obsFilePath = file
        self.obsFileLineEdit.setText(file)

    # Manually refresh the current kit
    def refreshKit(self):
        print("Refresh Kit")

    # Slot for Nav Bar Buttons
    def navBarButtonClicked(self):
        sender = self.sender()
        if sender == self.homeMenuButton:
            self.stackedWidget.setCurrentWidget(self.kitsWidget)
        elif sender == self.midiLogMenuButton:
            self.stackedWidget.setCurrentWidget(self.midiWidget)
        elif sender == self.appLogMenuButton:
            self.stackedWidget.setCurrentWidget(self.logWidget)
        elif sender == self.settingsButton:
            self.stackedWidget.setCurrentWidget(self.settingsWidget)
        elif sender == self.githubButton:
            QDesktopServices.openUrl(self.repoUrl)

    # Slot of ChatBot Comms Checkbox
    def chatBotCheckBoxChanged(self):
        self.chatBotCommsEnabled = self.settingsChatBotCheckbox.isChecked()
        self.log(f"ChatBot Communication Enabled: {self.chatBotCommsEnabled}")

    def twitchChannelChanged(self):
        self.twitch_channel = self.settingsChannelLineEdit.text()
        self.log(f"Twitch Channel: {self.twitch_channel}")

    # Slot for Midi Filter Checkboxes
    def midiFilterChanged(self):
        """To Do Create and add functionality for midi event filter"""
        sender = self.sender()
        if sender == self.midiLogShowSysExCheckBox:
            if self.midiLogShowSysExCheckBox.isChecked():
                if "sysex" not in self.midi_log_filter:
                    self.midi_log_filter.append("sysex")
            else:
                if "sysex" in self.midi_log_filter:
                    self.midi_log_filter.remove("sysex")
        elif sender == self.midiLogShowNoteOnCheckBox:
            if self.midiLogShowNoteOnCheckBox.isChecked():
                if "note_on" not in self.midi_log_filter:
                    self.midi_log_filter.append("note_on")
            else:
                if "note_on" in self.midi_log_filter:
                    self.midi_log_filter.remove("note_on")
        elif sender == self.midiLogShowNoteOffCheckBox:
            if self.midiLogShowNoteOffCheckBox.isChecked():
                if "note_off" not in self.midi_log_filter:
                    self.midi_log_filter.append("note_off")
            else:
                if "note_off" in self.midi_log_filter:
                    self.midi_log_filter.remove("note_off")
        elif sender == self.midiLogShowPolyCheckBox:
            if self.midiLogShowPolyCheckBox.isChecked():
                if "polytouch" not in self.midi_log_filter:
                    self.midi_log_filter.append("polytouch")
            else:
                if "polytouch" in self.midi_log_filter:
                    self.midi_log_filter.remove("polytouch")
        elif sender == self.midiLogShowProgChangeCheckBox:
            if self.midiLogShowProgChangeCheckBox.isChecked():
                if "program_change" not in self.midi_log_filter:
                    self.midi_log_filter.append("program_change")
            else:
                if "program_change" in self.midi_log_filter:
                    self.midi_log_filter.remove("program_change")
        elif sender == self.midiLogShowControlChangeCheckBox:
            if self.midiLogShowControlChangeCheckBox.isChecked():
                if "control_change" not in self.midi_log_filter:
                    self.midi_log_filter.append("control_change")
            else:
                if "control_change" in self.midi_log_filter:
                    self.midi_log_filter.remove("control_change")
        elif sender == self.midiLogShowClockCheckBox:
            if self.midiLogShowClockCheckBox.isChecked():
                if "clock" not in self.midi_log_filter:
                    self.midi_log_filter.append("clock")
            else:
                if "clock" in self.midi_log_filter:
                    self.midi_log_filter.remove("clock")
        elif sender == self.midiLogShowAllCheckBox:
            if self.midiLogShowAllCheckBox.isChecked():
                if "all" not in self.midi_log_filter:
                    self.midi_log_filter.append("all")
            else:
                if "all" in self.midi_log_filter:
                    self.midi_log_filter.remove("all")
        print(self.midi_log_filter)

    # Sent a MIDI Message
    def midi_send(self, msg):
        self.log_midi(msg, outgoing=True)
    
    # Received a MIDI Message
    def midi_recv(self, msg):
        self.log_midi(msg, outgoing=False)

    def updateChatBotKit(self, key, channel, kit_num, kit_name, kit_subname):
        thread = Thread(target=self.updateChatBotKitWorker, args=(key, channel, kit_num, kit_name, kit_subname))
        thread.start()
    
    def updateChatBotKitWorker(self, key, channel, kit_num, kit_name, kit_subname):
        data = {
            "key": key,
            "type": "kit",
            "channel": channel,
            "kit_num": kit_num,
            "kit_name": kit_name,
            "kit_subname": kit_subname
        }
        url = "http://twitchbot.chillaspect.com/kitconnect.php"
        r = requests.post(url, json=data)
        if r.status_code >= 400:
            self.log(f"Error updating chat bot with current kit: {r.text}")

    # Write messages to App Log
    def log(self, msg):
        if not msg:
            return
        print(msg)
        style = "color: #000000;"
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        msg = f'<span style="{style}">{timestamp} - {msg}</span>'
        self.logBrowser.append(msg)

    # Write messages to MIDI Log
    def log_midi(self, msg, outgoing=False):
        if not msg:
            return
        status = msg.dict()["type"]
        if status not in self.midi_log_filter:
            #if "all" in self.midi_log_filter and status in self.midi_log_filter_possible_values:
            return
        if self.midi_log_entries > self.midi_log_max_entries:
            self.midiLogBrowser.clear()
            self.log("Midi Log Max Entries Reached. Cleared Midi Log.")
            self.midi_log_entries = 0
        msg_str = TD50X.to_str(msg)
        style = "color: #000000;"
        if outgoing:
            msg_str = f" &gt; {msg_str}"
            style = "color: #112863;"
        else:
            msg_str = f" &lt; {msg_str}"
            style = "color: #0d7a15;"
        now = datetime.datetime.now()
        #timestamp = now.strftime("%H:%M:%S")
        msg = f'<span style="{style}">{msg_str}</span>'
        self.midiLogBrowser.append(msg)
        self.midi_log_entries += 1

    # Set a status message with optional timeout
    def status(self, msg, timeout=0):
        self.statusLabel.setText(msg)
        if timeout > 0:
            QTimer.singleShot(timeout, lambda : self.check_clear_status(msg))

    # Check to see if status label needs to be cleared
    def check_clear_status(self, msg):
        if self.statusLabel.text() == msg:
            self.statusLabel.setText("")

    # Save Settings to INI File
    def saveSettings(self):
        self.settings.setValue(f"{self.project_name}/geometry", self.saveGeometry())
        self.settings.setValue(f"{self.project_name}/windowState", self.saveState())
        if self.testport_midi_enabled:
            self.settings.setValue(f"{self.project_name}/EnableTestPortMidiDevice", "1")
        else:
            self.settings.setValue(f"{self.project_name}/EnableTestPortMidiDevice", "0")
        self.settings.setValue(f"{self.project_name}/OBSFilePath", self.obsFilePath)
        self.settings.setValue(f"{self.project_name}/MidiDevice", self.device)
        template_str = self.obsFileTemplateEdit.document().toPlainText()
        b64_template_str = base64.b64encode(template_str.encode("utf-8")).decode("utf-8")
        self.settings.setValue(f"{self.project_name}/OBSFileTemplate", b64_template_str)
        if self.chatBotCommsEnabled:
            self.settings.setValue(f"{self.project_name}/ChatBotCommsEnabled", "1")
        else:
            self.settings.setValue(f"{self.project_name}/ChatBotCommsEnabled", "0")
        self.settings.setValue(f"{self.project_name}/TwitchChannel", self.twitch_channel)
        if self.midiLogShowSysExCheckBox.isChecked():
            self.settings.setValue(f"MidiLogFilter/SysEx", "1")
        else:
            self.settings.setValue(f"MidiLogFilter/SysEx", "0")
        if self.midiLogShowNoteOnCheckBox.isChecked():
            self.settings.setValue(f"MidiLogFilter/NoteOn", "1")
        else:
            self.settings.setValue(f"MidiLogFilter/NoteOn", "0")
        if self.midiLogShowNoteOffCheckBox.isChecked():
            self.settings.setValue(f"MidiLogFilter/NoteOff", "1")
        else:
            self.settings.setValue(f"MidiLogFilter/NoteOff", "0")
        if self.midiLogShowPolyCheckBox.isChecked():
            self.settings.setValue(f"MidiLogFilter/Poly", "1")
        else:
            self.settings.setValue(f"MidiLogFilter/Poly", "0")
        if self.midiLogShowProgChangeCheckBox.isChecked():
            self.settings.setValue(f"MidiLogFilter/ProgramChange", "1")
        else:
            self.settings.setValue(f"MidiLogFilter/ProgramChange", "0")
        if self.midiLogShowControlChangeCheckBox.isChecked():
            self.settings.setValue(f"MidiLogFilter/ControlChange", "1")
        else:
            self.settings.setValue(f"MidiLogFilter/ControlChange", "0")
        if self.midiLogShowClockCheckBox.isChecked():
            self.settings.setValue(f"MidiLogFilter/Clock", "1")
        else:
            self.settings.setValue(f"MidiLogFilter/Clock", "0")
        if self.midiLogShowAllCheckBox.isChecked():
            self.settings.setValue(f"MidiLogFilter/All", "1")
        else:
            self.settings.setValue(f"MidiLogFilter/All", "0")
        self.settings.sync()
        
    # App is closing, cleanup
    def closeEvent(self, evt=None):
        # Show the waiting cursor while shutting down
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        
        # Close TD50X Midi Connection
        self.closeTD50X()
        
        # Remember the size and position of the GUI
        self.log("Saving Settings")
        self.saveSettings()
        
        QApplication.restoreOverrideCursor()
        self.log("Exiting")
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