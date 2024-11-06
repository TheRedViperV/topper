from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QHeaderView, QFrame, QTabWidget)
from PyQt5.QtCore import Qt as QtCore
from .buttons import ModernButton  # Added dot here
from .tables import ModernTable    # Added dot here

class UIBuilder:
    def __init__(self, main_window):
        self.main_window = main_window

    def setup_ui(self):
        self.main_window.setWindowTitle('Topper (GOAT)')
        self.main_window.setFixedSize(900, 700)
        self.main_window.setStyleSheet("""
            QMainWindow {
                background-color: #f5f6fa;
            }
        """)
        
        central_widget = QWidget()
        self.main_window.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Add components
        main_layout.addLayout(self._create_header())
        main_layout.addWidget(self._create_shortcuts_frame())
        main_layout.addWidget(self._create_tabs())
        main_layout.addWidget(self._create_footer())

    def _create_header(self):
        header = QHBoxLayout()
        title_label = QLabel('Topper (GOAT)')
        title_label.setStyleSheet("""
            QLabel {
                color: #2d3436;
                font-size: 24px;
                font-weight: bold;
            }
        """)
        header.addWidget(title_label)
        header.addStretch()
        return header

    def _create_shortcuts_frame(self):
        shortcuts_frame = QFrame()
        shortcuts_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        shortcuts_layout = QVBoxLayout(shortcuts_frame)
        shortcuts_label = QLabel("Keyboard Shortcuts")
        shortcuts_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        shortcuts_layout.addWidget(shortcuts_label)
        
        shortcut_buttons = QHBoxLayout()
        self.main_window.toggle_shortcut_btn = ModernButton(
            f"Toggle Window: {self.main_window.settings_manager.shortcuts['toggle']}"
        )
        self.main_window.show_shortcut_btn = ModernButton(
            f"Show Topper: {self.main_window.settings_manager.shortcuts['show']}"
        )
        
        self.main_window.toggle_shortcut_btn.clicked.connect(
            lambda: self.main_window.edit_shortcut('toggle')
        )
        self.main_window.show_shortcut_btn.clicked.connect(
            lambda: self.main_window.edit_shortcut('show')
        )
        
        shortcut_buttons.addWidget(self.main_window.toggle_shortcut_btn)
        shortcut_buttons.addWidget(self.main_window.show_shortcut_btn)
        shortcuts_layout.addLayout(shortcut_buttons)
        
        return shortcuts_frame

    def _create_tabs(self):
        tab_widget = QTabWidget()
        tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #dcdde1;
                border-radius: 4px;
            }
            QTabBar::tab {
                background-color: #2d3436;
                color: white;
                padding: 8px 20px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: #636e72;
            }
        """)
        
        # Pinned Windows Tab
        pinned_tab = QWidget()
        pinned_layout = QVBoxLayout(pinned_tab)
        self.main_window.pinned_table = ModernTable()
        self.main_window.pinned_table.setColumnCount(2)
        self.main_window.pinned_table.setHorizontalHeaderLabels(["Window Title", "Actions"])
        self.main_window.pinned_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        pinned_layout.addWidget(self.main_window.pinned_table)
        
        # Available Windows Tab
        available_tab = QWidget()
        available_layout = QVBoxLayout(available_tab)
        self.main_window.available_table = ModernTable()
        self.main_window.available_table.setColumnCount(2)
        self.main_window.available_table.setHorizontalHeaderLabels(["Window Title", "Actions"])
        self.main_window.available_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        available_layout.addWidget(self.main_window.available_table)
        
        tab_widget.addTab(pinned_tab, "Pinned Windows")
        tab_widget.addTab(available_tab, "Available Windows")
        
        return tab_widget

    def _create_footer(self):
        footer = QLabel("Made by The Red Viper (GOAT) v1.0")
        footer.setAlignment(QtCore.AlignRight)
        footer.setStyleSheet("""
            QLabel {
                color: #636e72;
                font-size: 12px;
                padding: 5px;
            }
        """)
        return footer