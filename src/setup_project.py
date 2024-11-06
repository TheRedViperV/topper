
import os
import shutil

def create_project_structure():
    # Create base directory
    base_dir = "topper"
    os.makedirs(os.path.join(base_dir, "src"), exist_ok=True)
    
    # Create run.py
    with open(os.path.join(base_dir, "run.py"), "w") as f:
        f.write('''import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.main import main

if __name__ == "__main__":
    main()
''')
    
    # Create __init__.py
    with open(os.path.join(base_dir, "src", "__init__.py"), "w") as f:
        f.write('''"""
Topper - Always on Top Window Manager
Created by The Red Viper (GOAT)
Version 1.0
"""

__version__ = "1.0"
__author__ = "The Red Viper (GOAT)"
''')
    
    # Create setup.py
    with open(os.path.join(base_dir, "setup.py"), "w") as f:
        f.write('''from setuptools import setup, find_packages

setup(
    name="topper",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "PyQt5>=5.15.0",
        "pywin32>=228",
        "keyboard>=0.13.5"
    ],
)
''')
    
    # Copy current .py files to src directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    python_files = [f for f in os.listdir(current_dir) if f.endswith('.py')]
    for file in python_files:
        if file != "setup_project.py":
            shutil.copy(
                os.path.join(current_dir, file),
                os.path.join(base_dir, "src", file)
            )
    
    # If icon exists, copy it
    icon_path = os.path.join(current_dir, "goat_icon.ico")
    if os.path.exists(icon_path):
        shutil.copy(icon_path, os.path.join(base_dir, "goat_icon.ico"))

    print(f"Project structure created in {os.path.abspath(base_dir)}")
    print("\nTo run the application:")
    print("1. cd topper")
    print("2. python run.py")

if __name__ == "__main__":
    create_project_structure()