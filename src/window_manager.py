import win32gui
import win32con
from PyQt5.QtWidgets import QTableWidgetItem
from .buttons import ModernButton

class WindowManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.pinned_windows = {}

    def get_window_title(self, hwnd: int) -> str:
        return win32gui.GetWindowText(hwnd)
    
    def get_active_window(self) -> int:
        return win32gui.GetForegroundWindow()

    def toggle_window_top(self, hwnd: int):
        if hwnd in self.pinned_windows:
            win32gui.SetWindowPos(
                hwnd,
                win32con.HWND_NOTOPMOST,
                0, 0, 0, 0,
                win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
            )
            del self.pinned_windows[hwnd]
        else:
            title = self.get_window_title(hwnd)
            if title:
                win32gui.SetWindowPos(
                    hwnd,
                    win32con.HWND_TOPMOST,
                    0, 0, 0, 0,
                    win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
                )
                self.pinned_windows[hwnd] = title

    def update_window_lists(self):
        # Update pinned windows table
        self.main_window.pinned_table.setRowCount(len(self.pinned_windows))
        for i, (hwnd, title) in enumerate(list(self.pinned_windows.items())):
            try:
                if not win32gui.IsWindow(hwnd):
                    del self.pinned_windows[hwnd]
                    continue
                
                self.main_window.pinned_table.setItem(i, 0, QTableWidgetItem(title))
                unpin_btn = ModernButton("Unpin")
                unpin_btn.setProperty("type", "unpin")
                unpin_btn.clicked.connect(lambda _, h=hwnd: self.toggle_window_top(h))
                self.main_window.pinned_table.setCellWidget(i, 1, unpin_btn)
            except:
                continue
        
        # Update available windows table
        def enum_windows_callback(hwnd, windows):
            if win32gui.IsWindowVisible(hwnd) and self.get_window_title(hwnd):
                windows.append(hwnd)
        
        windows = []
        win32gui.EnumWindows(enum_windows_callback, windows)
        
        available_windows = [(hwnd, self.get_window_title(hwnd)) 
                          for hwnd in windows 
                          if hwnd not in self.pinned_windows]
        
        self.main_window.available_table.setRowCount(len(available_windows))
        for i, (hwnd, title) in enumerate(available_windows):
            self.main_window.available_table.setItem(i, 0, QTableWidgetItem(title))
            pin_btn = ModernButton("Pin")
            pin_btn.clicked.connect(lambda _, h=hwnd: self.toggle_window_top(h))
            self.main_window.available_table.setCellWidget(i, 1, pin_btn)