from PyQt5.QtWidgets import QPushButton

class ModernButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 5px 15px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 12px;
                min-width: 70px;
                height: 28px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #2573a7;
            }
            QPushButton[type="unpin"] {
                background-color: #e74c3c;
            }
            QPushButton[type="unpin"]:hover {
                background-color: #c0392b;
            }
        """)