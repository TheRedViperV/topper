# Topper

Keep any window **always on top** on Windows. Pin the window you are working in with a keyboard shortcut,
or pick windows from a list, and they stay above everything else until you unpin them.

## Features

- **Pin with a shortcut:** `Ctrl+Alt+T` pins (or unpins) the window that has focus.
- **Pick from a list:** the *Available Windows* tab lists every open window with a **Pin** button; *Pinned
  Windows* shows what is pinned, each with **Unpin**.
- **Show Topper anywhere:** `Ctrl+Alt+S` brings the Topper window back.
- **Your own shortcuts:** both shortcuts can be changed in the app and are saved in `topper_settings.json`
  next to the program.
- **Lives in the tray:** double-click the tray icon to open Topper; quitting unpins every pinned window.

## Download

Get `Topper.exe` from [Releases](../../releases/latest). It is a single portable file, with no installer.
Windows SmartScreen may warn because the file is not code-signed; choose *More info > Run anyway*.

## Run from source

Requires Windows and Python 3.11+.

```
pip install -r requirements.txt
python run.py
```

The global shortcuts use the `keyboard` package, which may need Topper to run as administrator to catch
keys while an elevated app has focus.

## Build the .exe

```
pip install pyinstaller
python build.py
```

The executable is written to `dist/Topper.exe`.
