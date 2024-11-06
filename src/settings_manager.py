import os
import sys
import json
import keyboard
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer

class SettingsManager:
    def __init__(self, main_window):
        self.main_window = main_window
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = os.path.dirname(os.path.dirname(__file__))
        
        self.settings_file = os.path.join(application_path, 'topper_settings.json')
        self.shortcuts = self.load_settings()

    def load_settings(self) -> dict:
        default_shortcuts = {
            "toggle": "ctrl+alt+t",
            "show": "ctrl+alt+s"
        }
        
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, 'r') as f:
                    loaded_settings = json.load(f)
                    if all(key in loaded_settings for key in default_shortcuts.keys()):
                        return loaded_settings
        except Exception as e:
            print(f"Error loading settings: {e}")
        
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(default_shortcuts, f)
        except Exception as e:
            print(f"Error saving default settings: {e}")
        
        return default_shortcuts

    def save_settings(self):
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(self.shortcuts, f)
        except Exception as e:
            print(f"Error saving settings: {e}")

    def setup_hotkeys(self):
        try:
            keyboard.unhook_all()
            keyboard.add_hotkey(self.shortcuts['toggle'], self.main_window.toggle_active_window, suppress=True)
            keyboard.add_hotkey(self.shortcuts['show'], self.safe_show_window, suppress=True)
        except Exception as e:
            QMessageBox.warning(self.main_window, "Error", f"Failed to setup hotkeys: {str(e)}")

    def safe_show_window(self):
        QTimer.singleShot(0, self.main_window.show_window)

    def edit_shortcut(self, shortcut_type, new_shortcut):
        try:
            keyboard.unhook_all()
            self.shortcuts[shortcut_type] = new_shortcut
            self.setup_hotkeys()
            self.save_settings()
            return True
        except Exception as e:
            QMessageBox.warning(self.main_window, "Error", f"Failed to set shortcut: {str(e)}")
            return False