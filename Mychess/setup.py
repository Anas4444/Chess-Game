from cx_Freeze import Executable, setup

executables = [Executable("chess.py", shortcutName = 'Mychess', shortcutDir = 'DesktopFolder', icon = 'Mychess.ico')]
setup(
    name="Mychess",
    options={"build_exe": {"packages": ["pygame"]}},
    executables = executables
)