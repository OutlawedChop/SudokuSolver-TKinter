import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'c:/Users/Admin/AppData/Local/Programs/Python/Python36-32/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'c:/Users/Admin/AppData/Local/Programs/Python/Python36-32//tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=['c:/Users/Admin/AppData/Local/Programs/Python/Python36-32/DLLs/tcl86t.dll', 'C:/Users/Admin/AppData/Local/Programs/Python/Python36-32/DLLs/tk86t.dll']
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('SudofuFullmy.py', base=base)
]

setup(name='SudofuFullmy',
      version = '1.0',
      description = 'TopApp',
      options = dict(build_exe = buildOptions),
      executables = executables)