import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QDialog
from PyQt5.QtCore import QTimer, pyqtSlot, QEvent
from PyQt5.QtCore import Qt as QtCore
from .dialogs import ShortcutDialog  # Changed to relative import
from .window_manager import WindowManager  # Changed to relative import
from .settings_manager import SettingsManager  # Changed to relative import
from .ui_builder import UIBuilder  # Changed to relative import
from .tray_manager import TrayManager  # Changed to relative import

class TopperGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize managers
        self.settings_manager = SettingsManager(self)
        self.window_manager = WindowManager(self)
        self.tray_manager = TrayManager(self)
        
        # Build UI
        self.ui_builder = UIBuilder(self)
        self.ui_builder.setup_ui()
        
        # Setup update timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.window_manager.update_window_lists)
        self.timer.start(1000)

    @pyqtSlot()
    def toggle_active_window(self):
        hwnd = self.window_manager.get_active_window()
        self.window_manager.toggle_window_top(hwnd)
        self.window_manager.update_window_lists()

    def show_window(self):
        if not self.isVisible() or self.isMinimized():
            self.showNormal()
            self.activateWindow()
            self.raise_()
            self.setWindowState(self.windowState() & ~QtCore.WindowMinimized | QtCore.WindowActive)

    def edit_shortcut(self, shortcut_type):
        dialog = ShortcutDialog(self.settings_manager.shortcuts[shortcut_type], self)
        if dialog.exec_() == QDialog.Accepted:
            new_shortcut = dialog.get_shortcut()
            if self.settings_manager.edit_shortcut(shortcut_type, new_shortcut):
                if shortcut_type == 'toggle':
                    self.toggle_shortcut_btn.setText(f"Toggle Window: {new_shortcut}")
                else:
                    self.show_shortcut_btn.setText(f"Show Topper: {new_shortcut}")

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() & QtCore.WindowMinimized:
                event.accept()
                self.tray_manager.show_message(
                    "Topper",
                    "Application minimized to tray. Double-click tray icon to restore."
                )
            else:
                event.accept()

    def closeEvent(self, event):
        if self.tray_manager.is_visible():
            reply = QMessageBox.question(
                self, 'Exit Confirmation',
                "Do you want to quit Topper? All pinned windows will be unpinned.",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                for hwnd in list(self.window_manager.pinned_windows.keys()):
                    self.window_manager.toggle_window_top(hwnd)
                event.accept()
                QApplication.quit()
            else:
                event.ignore()
                self.hide()
        else:
            event.accept()

    def quit_application(self):
        reply = QMessageBox.question(
            self, 'Exit Confirmation',
            "Do you want to quit Topper? All pinned windows will be unpinned.",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            for hwnd in list(self.window_manager.pinned_windows.keys()):
                self.window_manager.toggle_window_top(hwnd)
            QApplication.quit()