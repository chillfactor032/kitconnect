"""
KitConnect GUI
"""
import json
import os
import datetime
import sys
import base64
import re
import requests
from enum import Enum
from threading import Thread

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QStyle, QMessageBox, QTableWidgetItem, QDialog, QMessageBox, QHeaderView
from PySide6.QtCore import Qt, QSettings, QFile, QTextStream, QByteArray, QStandardPaths, QTimer, QUrl, QThreadPool
from PySide6.QtGui import QPixmap, QIcon, QDesktopServices, QCursor
from PySide6.QtWebEngineWidgets import QWebEngineView

import Resources_rc
from UI_Components import Ui_MainWindow, Ui_ReactDialog
from td50x import TD50X
from wled import WledWebsocket

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load UI Components
        self.setupUi(self)
        
        # App Variables
        self.geometryToRestore = None
        self.repoUrl = QUrl("https://github.com/chillfactor032/kitconnect")
        self.midi_devices = []
        self.midi_log_entries = 0
        self.midi_log_max_entries = 10000
        self.midi_log_filter = []
        self.midi_log_filter_possible_values = ['sysex', 'note_on', 'note_off', 'polytouch', 'program_change', 'control_change', 'clock', 'all']
        self.twitchbot_key = "1234"
        self.kit_data = []
        self.last_kit_sent = 0
        self.current_kit_num = 0
        self.current_kit_name = ""
        self.current_kit_subname = ""
        self.chatbot_timer = QTimer(self)
        self.chatbot_timer.setInterval(2000)
        self.chatbot_timer.timeout.connect(self.check_send_chatbot)
        self.react_rows = []
        self.menu_button_default_css = self.homeMenuButton.styleSheet()
        self.menu_button_active_css = """
            #menuFrame QToolButton {
                background-color: #343b47;
                color: #fff;
                text-align: left;
                border: none;
                padding: 5px 0px 5px 0px;
                border-radius: 5px;
            }

            #menuFrame QToolButton:hover {
                background-color: #2c313c;
            }
        """.strip()
        
        # Read Version File From Resources
        version_file = QFile(":version.json")
        version_file.open(QFile.ReadOnly)
        text_stream = QTextStream(version_file)
        version_file_text = text_stream.readAll()
        self.version_dict = json.loads(version_file_text)
        version_file.close()
        self.app_name = self.version_dict["product_name"]
        self.version = self.version_dict["version"]
        self.description = self.version_dict["description"]
        self.author = self.version_dict["author"]
        self.author_email = self.version_dict["author_email"]
        self.project_name = self.app_name.title().replace(" ", "")
        self.setWindowTitle(f"{self.app_name} {self.version}")
        kit_img_file = QFile(":resources/img/kit_bttf.png")
        kit_img_file.open(QFile.ReadOnly)
        kit_img_file_bytes = kit_img_file.readAll()
        self.kit_img_b64 = bytes(kit_img_file_bytes.toBase64()).decode()
        font_file = QFile(":resources/files/Seven_Segment.ttf")
        font_file.open(QFile.ReadOnly)
        font_file_bytes = font_file.readAll()
        self.font_b64 = bytes(font_file_bytes.toBase64()).decode()

        self.config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        self.documents = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        if(not os.path.isdir(self.config_dir)):
            os.makedirs(self.config_dir)
        self.ini_path = os.path.join(self.config_dir, f"kitconnectgui.ini").replace("\\", "/")
        self.kit_data_path = os.path.join(self.config_dir, f"kits.json").replace("\\", "/")
        self.font_path = os.path.join(self.config_dir, f"Seven_Segment.ttf").replace("\\", "/")
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)

        # Check if font file exists
        if not os.path.exists(self.font_path):
            font_file = QFile(":resources/files/Seven_Segment.ttf")
            if font_file.copy(self.font_path):
                self.log("Seven Segment Font File Copied Successfully")
            else:
                self.log("Error copying font file")

        # Read Settings
        self.chat_command_url = ""
        self.chat_command_url = self.settings.value(f"{self.project_name}/ChatCommandURL", "https://backbeatbot.com/kitconnect.php")
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

        # Kit Data Table Signal
        self.kitTableWidget.itemChanged.connect(self.saveKitData)

        # Navigation Bar Button Signals
        self.homeMenuButton.clicked.connect(self.navBarButtonClicked)
        self.drumKitsMenuButton.clicked.connect(self.navBarButtonClicked)
        self.reactiveButton.clicked.connect(self.navBarButtonClicked)
        self.midiLogMenuButton.clicked.connect(self.navBarButtonClicked)
        self.appLogMenuButton.clicked.connect(self.navBarButtonClicked)
        self.settingsButton.clicked.connect(self.navBarButtonClicked)
        self.githubButton.clicked.connect(self.navBarButtonClicked)

        # Other Button/Widget Signals
        self.midiDeviceComboBox.currentIndexChanged.connect(self.deviceSelected)
        self.refreshKitDataButton.clicked.connect(self.refreshKitData)
        self.refreshDevicesButton.clicked.connect(self.refreshDevices)
        self.browseFileButton.clicked.connect(self.browseOBSFile)
        self.settingsChatBotCheckbox.stateChanged.connect(self.chatBotCheckBoxChanged)
        self.settingsChannelLineEdit.editingFinished.connect(self.twitchChannelChanged)
        self.reactAddButton.clicked.connect(self.react_add_row)
        self.reactEditButton.clicked.connect(self.react_edit_row)
        self.reactDeleteButton.clicked.connect(self.react_del_row)
        self.reactConnectButton.clicked.connect(self.reactConnectButtonClicked)

        # Set Midi Filter Checkbox Signals
        self.midiLogShowSysExCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowNoteOnCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowNoteOffCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowPolyCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowProgChangeCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowControlChangeCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowClockCheckBox.stateChanged.connect(self.midiFilterChanged)
        self.midiLogShowAllCheckBox.stateChanged.connect(self.midiFilterChanged)

        # React Table
        reactHeaderLabels = ["Drum", "Midi Event", "WLED Msg"]
        self.reactTable.setColumnCount(len(reactHeaderLabels))
        self.reactTable.setHorizontalHeaderLabels(reactHeaderLabels)
        self.reactTable.horizontalHeader().setStretchLastSection(True)
        self.reactTable.verticalHeader().hide()

        # TD-50X Object
        self.td50x = None

        # ThreadPool
        self.threadpool = QThreadPool()

        #Set window Icon
        default_icon_pixmap = QStyle.StandardPixmap.SP_FileDialogListView
        icon_pixmap = QPixmap(":resources/img/icons/drum.ico")
        pc_icon = QIcon(icon_pixmap)
        default_icon = self.style().standardIcon(default_icon_pixmap)
        if(pc_icon):
            self.setWindowIcon(pc_icon)
        else:
            self.setWindowIcon(default_icon)

        self.midi_types = TD50X.get_midi_types()
        self.log(self.font_path)
        self.log(f"Chat Command URL: {self.chat_command_url}")
        self.obs_webview_html = f"""
        <html>
        <style>
        @font-face {{
			font-family: 'seven_segment';
			src: url("data:font/ttf;base64, {self.font_b64}");
		}}
        body {{
            background-color: green;
        }}
        #kit_img {{
            height: 60px;
            width: auto;
        }}
        #kit_info {{
            font-size: 40px;
            text-align: left;
        }}
        .lcd {{
            font-family: "seven_segment";
            text-shadow: -1px 0 white, 0 1px white, 1px 0 white, 0 -1px white;
        }}
        </style>
        <body>
        <div>
        <table width="100%" border=0>
        <tr>
            <td style="width: 1px;"><img id="kit_img" src="data:image/png;base64, {self.kit_img_b64}" /></td>
            <td id="kit_info" class="lcd">{{kit_num}} - {{kit_name}} </td>
        </tr>
        </table>
        </div>
        <body>
        </html>
        """.strip()

        # WLED WebSocket Client
        self.reactWledUrlLineEdit.setText(self.settings.value(""))
        self.wled_url = self.settings.value("wled_url", "")
        self.wled_ws = None
        self.wled_monitor_timer = QTimer()
        self.wled_monitor_timer.timeout.connect(self.checkWledConnection)
        self.wled_monitor_timer.start(5000)
        self.wledConnect()

        self.update_react_rows()
        self.obs_webview = QWebEngineView()
        #self.obsGroupBox.layout().addWidget(self.obs_webview)
        self.obs_webview.setHtml(self.obs_webview_html)
        self.kitTableWidget.setColumnWidth(0, 200)
        self.kitTableWidget.setRowCount(100)
        self.loadKitDataFile()
        self.homeMenuButton.setStyleSheet(self.menu_button_active_css)
        self.stackedWidget.setCurrentWidget(self.homeWidget)
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
        QTimer.singleShot(1000, self.refreshDevices)

        # Finally, Show the UI
        self.status("KitConnect Started")
        self.show()
        

    def checkWledConnection(self):
        if self.wled_ws is not None and self.wled_ws.connected():
            self.reactWledUrlLineEdit.setEnabled(False)
            self.reactConnectButton.setText("Disconnect")
        else:
            self.reactWledUrlLineEdit.setEnabled(True)
            self.reactConnectButton.setText("Connect")

    def wledDisconnect(self):
        if self.wled_ws is not None and self.wled_ws.connected():
            self.wled_ws.stop()
            self.wled_ws.join()

    def wledConnect(self):
        self.wledDisconnect()
        self.wled_url = self.settings.value("wled_url", None)
        self.reactWledUrlLineEdit.setText(self.wled_url)
        if self.wled_url is not None:
            self.wled_ws = WledWebsocket(self.wled_url)
            self.wled_ws.signals.log.connect(self.log)
            self.wled_ws.start()

    def reactConnectButtonClicked(self):
        url = self.reactWledUrlLineEdit.text()
        if len(url) > 0:
            self.settings.setValue("wled_url", url)
        if self.wled_ws is not None and self.wled_ws.connected():
            self.wledDisconnect()
        else:
            self.wledConnect()
        self.reactConnectButton.setText("Working...")
        
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
        self.td50x.signals.midi_connect.connect(self.deviceConnected)
        self.td50x.signals.log.connect(self.log)
        self.td50x.midi_start()

    def loadKitDataFile(self):
        self.kitTableWidget.blockSignals(True)
        self.kitTableWidget.clearContents()
        try:
            if os.path.exists(self.kit_data_path):
                with open(self.kit_data_path, "r") as kit_file:
                    self.kit_data = json.load(kit_file)
            else:
                self.kit_data = self.getDefaultKitData()
        except Exception as e:
            self.kit_data = self.getDefaultKitData()
        row = 0
        for kit in self.kit_data:
            kit_name = QTableWidgetItem(kit["name"])
            sub_name = QTableWidgetItem(kit["subname"])
            self.kitTableWidget.setItem(row, 0, kit_name)
            self.kitTableWidget.setItem(row, 1, sub_name)
            row+=1
        self.kitTableWidget.blockSignals(False)

    def saveKitData(self):
        print("Save kit data")
        row_count = self.kitTableWidget.rowCount()    
        for x in range(0, row_count):
            kit_num = x+1
            kit_name = self.kitTableWidget.item(x, 0).text()
            kit_subname = self.kitTableWidget.item(x, 1).text()
            self.kit_data[x] = {
                "kit_num": kit_num,
                "name": kit_name,
                "subname": kit_subname
            }
        with open(self.kit_data_path, "w") as kit_file:
            json.dump(self.kit_data, kit_file, indent=2)
        self.status("Kit Data Saved", 2000)

    def getDefaultKitData(self):
        kit_default_data_file = QFile(":resources/files/kits_default.json")
        kit_default_data_file.open(QFile.ReadOnly)
        kit_default_data_text_stream = QTextStream(kit_default_data_file)
        kit_default_data_file_text = kit_default_data_text_stream.readAll()
        default_kit_data = json.loads(kit_default_data_file_text)
        return default_kit_data

    def refreshKitData(self):
        self.status("Refreshing Kit Data...", 2000)
        self.refreshKitDataButton.setEnabled(False)
        QTimer.singleShot(2000, lambda: self.refreshKitDataButton.setEnabled(True))
        if self.td50x:
            self.td50x.refresh_current_kit()

    def closeTD50X(self):
        if self.td50x:
            self.log(f"Disconnecting old MIDI device [{self.td50x.port_name}]")
            self.td50x.midi_stop()
            self.td50x = None
            self.log("MIDI Device Disconnected")
    
    def deviceConnected(self):
        self.log("Midi Device Connected")
        self.refreshKitData()

    def deviceSelected(self, index):
        self.closeTD50X()
        if index <= 0:
            return
        self.device = self.midiDeviceComboBox.currentData()
        self.log(f"MIDI Device Selected: {self.device}")
        self.createTD50X(self.device)

    # TD-50X Reports the kit changed to the provided kit num
    def kit_updated(self, num):
        if num < 1 or num > 100:
            return
        kit = self.kit_data[num-1]
        name = kit["name"]
        subname = kit["subname"]
        self.curKitLineEdit.setText(f"{num} - {name}")
        self.curKitSubLineEdit.setText(subname)
        self.current_kit_num = num
        self.current_kit_name = name
        self.current_kit_subname = subname
        self.log(f"Current Kit Updated: {self.current_kit_num} - {self.current_kit_name}")
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
        self.obs_src_label.setText(out_str)
        """
        template_str = self.obs_webview_html
        out_str = template_str.replace("{kit_num}", str(num))
        out_str = out_str.replace("{kit_name}", name)
        out_str = out_str.replace("{kit_subname}", subname)
        self.obs_webview.setHtml(out_str)
        self.obsGroupBox.repaint()
        """
    
    def react_add_row(self):
        print("React Add Row")
        dlg = ReactDialog(self)
        if dlg.exec():
            results = dlg.get_results()
            if results is not None:
                self.react_rows.append(results)
                self.save_react_rows()
                self.update_react_rows()

    def react_edit_row(self):
        print("React Edit Row")
        selected = self.reactTable.currentRow()
        if selected < 0:
            return
        dlg = ReactDialog(self, self.react_rows[selected])
        if dlg.exec():
            results = dlg.get_results()
            if results is not None:
                self.react_rows[selected] = results
                self.save_react_rows()
                self.update_react_rows()
    
    def react_del_row(self):
        print("React Del Row")
        selected = self.reactTable.currentRow()
        if selected < 0:
            return
        self.react_rows.pop(selected)
        self.save_react_rows()
        self.update_react_rows()
    
    def save_react_rows(self):
        self.settings.beginWriteArray("react_triggers")
        for x in range(len(self.react_rows)):
            self.settings.setArrayIndex(x)
            row = self.react_rows[x]
            self.settings.setValue("note_value", str(row[0].value))
            self.settings.setValue("midi_event", str(row[1]))
            message_b64 = base64.b64encode(row[2].encode("utf-8")).decode("utf-8")
            self.settings.setValue("message_b64", message_b64)
        self.settings.endArray()

    def update_react_rows(self):
        size = self.settings.beginReadArray("react_triggers")
        self.react_rows = []
        for i in range(0, size):
            self.settings.setArrayIndex(i)
            row = []
            note_enum = TD50X.NoteNumbers.UNKNOWN
            note_value = int(self.settings.value("note_value", "0"))
            for note in TD50X.NoteNumbers:
                if note.value == note_value:
                    note_enum = note
                    break
            row.append(note_enum)
            midi_value = self.settings.value("midi_event", "any")
            row.append(midi_value)
            message_b64 = self.settings.value("message_b64", "")
            message_text = base64.b64decode(message_b64.encode("utf-8")).decode("utf-8")
            row.append(message_text)
            self.react_rows.append(row)
        self.settings.endArray()
        self.clear_react_table()
        for x in range(len(self.react_rows)-1, -1, -1):
            self.reactTable.insertRow(0)
            self.reactTable.setItem(0, 0, QTableWidgetItem(self.react_rows[x][0].name))
            self.reactTable.setItem(0, 1, QTableWidgetItem(self.react_rows[x][1]))
            msg_txt = self.react_rows[x][2]
            if len(msg_txt) > 32:
                msg_txt = msg_txt[:32]+"..."
            self.reactTable.setItem(0, 2, QTableWidgetItem(msg_txt))

    def clear_react_table(self):
        while self.reactTable.rowCount() > 0:
            self.reactTable.removeRow(0)

    # Called every 2 secs on a timer
    def check_send_chatbot(self):
        if self.current_kit_num != self.last_kit_sent:
            self.updateChatBotKit(self.twitchbot_key, self.twitch_channel, self.current_kit_num, self.current_kit_name, self.current_kit_subname)
            self.last_kit_sent = self.current_kit_num
            self.log(f"Kit Sent To Chatbot: {self.current_kit_num} - {self.current_kit_name}")

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

    def navBarButtonResetBgColors(self):
        self.homeMenuButton.setStyleSheet(self.menu_button_default_css)
        self.drumKitsMenuButton.setStyleSheet(self.menu_button_default_css)
        self.midiLogMenuButton.setStyleSheet(self.menu_button_default_css)
        self.appLogMenuButton.setStyleSheet(self.menu_button_default_css)
        self.settingsButton.setStyleSheet(self.menu_button_default_css)
        self.reactiveButton.setStyleSheet(self.menu_button_default_css)

    # Slot for Nav Bar Buttons
    def navBarButtonClicked(self):
        self.navBarButtonResetBgColors()
        sender = self.sender()
        if sender == self.homeMenuButton:
            self.homeMenuButton.setStyleSheet(self.menu_button_active_css)
            self.stackedWidget.setCurrentWidget(self.homeWidget)
        elif sender == self.drumKitsMenuButton:
            self.drumKitsMenuButton.setStyleSheet(self.menu_button_active_css)
            self.stackedWidget.setCurrentWidget(self.kitsWidget)
        elif sender == self.midiLogMenuButton:
            self.midiLogMenuButton.setStyleSheet(self.menu_button_active_css)
            self.stackedWidget.setCurrentWidget(self.midiWidget)
        elif sender == self.appLogMenuButton:
            self.appLogMenuButton.setStyleSheet(self.menu_button_active_css)
            self.stackedWidget.setCurrentWidget(self.logWidget)
        elif sender == self.settingsButton:
            self.settingsButton.setStyleSheet(self.menu_button_active_css)
            self.stackedWidget.setCurrentWidget(self.settingsWidget)
        elif sender == self.reactiveButton:
            self.reactiveButton.setStyleSheet(self.menu_button_active_css)
            self.stackedWidget.setCurrentWidget(self.reactiveWidget)
        elif sender == self.githubButton:
            QDesktopServices.openUrl(self.repoUrl)

    # Slot of ChatBot Comms Checkbox
    def chatBotCheckBoxChanged(self):
        self.chatBotCommsEnabled = self.settingsChatBotCheckbox.isChecked()
        if self.chatBotCommsEnabled:
            self.chatbot_timer.start()
        else:
            self.chatbot_timer.stop()
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
        #print(self.midi_log_filter)

    # Sent a MIDI Message
    def midi_send(self, msg):
        self.log_midi(msg, outgoing=True)
    
    # Received a MIDI Message
    def midi_recv(self, msg):
        self.log_midi(msg, outgoing=False)
        if self.wled_ws is None or not self.wled_ws.connected():
            return
        note = msg.dict().get("note",TD50X.NoteNumbers.UNKNOWN.value)
        for react in self.react_rows:
            #0: Note 1: midi  2: msg
            if react[0].value == note or react[0] == TD50X.NoteNumbers.UNKNOWN.value:
                if react[1] == msg.type or react[1] == "any":
                    self.wled_ws.send(self.ws_var_replace(react[2], msg.dict()))

    def ws_var_replace(self, ws_msg: str, midi_dict: dict):
        ws_msg = ws_msg.replace("${VELOCITY}", str(midi_dict.get("velocity", 64)))
        return ws_msg
            

    def updateChatBotKit(self, key, channel, kit_num, kit_name, kit_subname):
        thread = Thread(target=self.updateChatBotKitWorker, args=(key, channel, kit_num, kit_name, kit_subname))
        thread.start()
    
    def updateChatBotKitWorker(self, key, channel, kit_num, kit_name, kit_subname):
        payload = {
            "key": key,
            "type": "kit",
            "channel": channel,
            "kit_num": kit_num,
            "kit_name": kit_name,
            "kit_subname": kit_subname
        }
        print(f"Submitting data to chatbot: {payload}")
        r = requests.post(self.chat_command_url, json=payload)
        if r.status_code >= 400:
            print(r.headers)
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
        self.settings.setValue(f"{self.project_name}/ChatCommandURL", self.chat_command_url)
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
        self.save_react_rows()
        self.wled_url = self.reactWledUrlLineEdit.text()
        self.settings.setValue("wled_url", self.wled_url)
        self.settings.sync()
        
    # App is closing, cleanup
    def closeEvent(self, evt=None):
        # Show the waiting cursor while shutting down
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        
        # Close TD50X Midi Connection
        self.closeTD50X()
        
        # Close WLED Connection
        self.wledDisconnect()

        #Stop Timers
        self.wled_monitor_timer.stop()
        self.chatbot_timer.stop()

        # Remember the size and position of the GUI
        self.log("Saving Settings")
        self.saveSettings()
        
        QApplication.restoreOverrideCursor()
        self.log("Exiting")
        evt.accept()

class ReactDialog(QDialog):
    
    def __init__(self, parent=None, values=None):
        super().__init__(parent)
        self.parent_obj = parent
        self.ui = Ui_ReactDialog()
        self.ui.setupUi(self)
        for drum in TD50X.NoteNumbers:
            self.ui.drumCombo.addItem(drum.name, drum)
        midi_types = TD50X.get_midi_types()
        for event in midi_types:
            self.ui.midiEventCombo.addItem(event, event)
        self.ui.okButton.clicked.connect(self.okButtonClick)
        self.ui.cancelButton.clicked.connect(self.cancelButtonClick)
        self.results = [None, None, None]
        if values is not None:
            self.ui.drumCombo.setCurrentText(values[0].name)
            self.ui.midiEventCombo.setCurrentText(values[1])
            self.ui.messageEdit.setPlainText(values[2])

    def get_results(self):
        if self.results is None:
            return None
        for result in self.results:
            if result is None:
                return None
        return self.results
            
    def okButtonClick(self):
        drum = self.ui.drumCombo.currentData()
        event = self.ui.midiEventCombo.currentData()
        message = self.ui.messageEdit.toPlainText()
        try:
            test_message = re.sub(r"\${.*?}", "0", message)
            message_on_obj = json.loads(test_message)
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "Could not parse ON message as JSON.", QMessageBox.StandardButton.Ok)
            self.results = [None, None, None]
            return
        self.results = [drum, event, message]
        self.accept()

    def cancelButtonClick(self):
        self.reject()

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