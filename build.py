import PyInstaller.__main__
import sys
import os

# Run PyInstaller
PyInstaller.__main__.run([
    'run.py',
    '--onefile',
    '--noconsole',
    '--name=Topper',
    '--icon=goat_icon.ico',
    '--clean',
    '--windowed'
])