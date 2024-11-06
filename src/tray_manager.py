import os
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QStyle
from PyQt5.QtGui import QIcon

class TrayManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.tray_icon = None
        self.setup_tray()

    def setup_tray(self):
        self.tray_icon = QSystemTrayIcon(self.main_window)
        
        # Set icon
        icon_path = "goat_icon.ico"
        if os.path.exists(icon_path):
            self.tray_icon.setIcon(QIcon(icon_path))
        else:
            self.tray_icon.setIcon(self.main_window.style().standardIcon(QStyle.SP_ComputerIcon))
        
        # Create tray menu
        tray_menu = QMenu()
        show_action = tray_menu.addAction("Show Topper")
        show_action.triggered.connect(self.main_window.show_window)
        
        tray_menu.addSeparator()
        
        quit_action = tray_menu.addAction("Quit")
        quit_action.triggered.connect(self.main_window.quit_application)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        
        # Connect double click
        self.tray_icon.activated.connect(self._handle_tray_activation)

    def _handle_tray_activation(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.main_window.show_window()

    def show_message(self, title, message, icon=QSystemTrayIcon.Information, duration=2000):
        if self.tray_icon:
            self.tray_icon.showMessage(title, message, icon, duration)

    def is_visible(self):
        return self.tray_icon and self.tray_icon.isVisible()