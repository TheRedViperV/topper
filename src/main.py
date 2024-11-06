import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QPalette, QColor
from .main_window import TopperGUI  # Note the dot before main_window

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    # Set application icon
    current_dir = os.path.dirname(os.path.dirname(__file__))
    icon_path = os.path.join(current_dir, "goat_icon.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    # Set color theme
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#f5f6fa"))
    palette.setColor(QPalette.WindowText, QColor("#2d3436"))
    app.setPalette(palette)
    
    window = TopperGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()