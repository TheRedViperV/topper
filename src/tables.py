from PyQt5.QtWidgets import QTableWidget

class ModernTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QTableWidget {
                background-color: #f5f6fa;
                border: 1px solid #dcdde1;
                border-radius: 4px;
                gridline-color: #dcdde1;
            }
            QTableWidget::item {
                padding: 4px;
            }
            QHeaderView::section {
                background-color: #2d3436;
                color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
            }
        """)
        self.verticalHeader().setDefaultSectionSize(38)  # Set row height
        self.setAlternatingRowColors(True)