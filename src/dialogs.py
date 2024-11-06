from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from .buttons import ModernButton  # Note the dot before buttons

class ShortcutDialog(QDialog):
    def __init__(self, current_shortcut="ctrl+alt+t", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Shortcut")
        self.setFixedSize(300, 100)
        self.setStyleSheet("""
            QDialog {
                background-color: #f5f6fa;
            }
        """)
        
        layout = QVBoxLayout()
        
        self.shortcut_input = QLineEdit(current_shortcut)
        self.shortcut_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #dcdde1;
                border-radius: 4px;
            }
        """)
        
        buttons = QHBoxLayout()
        save_btn = ModernButton("Save")
        cancel_btn = ModernButton("Cancel")
        
        save_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        
        buttons.addWidget(save_btn)
        buttons.addWidget(cancel_btn)
        
        layout.addWidget(QLabel("Enter new shortcut:"))
        layout.addWidget(self.shortcut_input)
        layout.addLayout(buttons)
        
        self.setLayout(layout)
    
    def get_shortcut(self):
        return self.shortcut_input.text()