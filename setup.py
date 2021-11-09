import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {
    "build_exe": {
        # exclude packages that are not really needed
        "excludes": [
            "tkinter",
            "unittest",
            "email",
            "http",
            "xml",
            "pydoc",
        ]
    }
}

executables = [
    Executable("__main__.py", base=base, target_name="PDFU", icon="PDFU.ico")
]

setup(
    name="PDFU",
    version="0.1",
    description="PDF Merge",
    options=options,
    executables=executables,
)
