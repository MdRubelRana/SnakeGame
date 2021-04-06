from cx_Freeze import *
import sys
includefiles=['icon.ico','head.gif','tail.gif','apple.gif']
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "SnakeGame",
     "TARGETDIR",
     "[TARGETDIR]\snake.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="0.1",
    description="Snake Game",
    author="Md. Rubel Rana",
    name="Snake Game",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="snake.py",
            base=base,
            icon='icon.ico',
        )
    ]
)