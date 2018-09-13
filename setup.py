
from cx_Freeze import setup, Executable
import sys
import pyaudio


#main
exe = Executable(script="F:\Jarvis\Jarvis.py",icon="F:\Jarvis\icon.ico")
buildOptions = dict(excludes = ["tkinter"], includes =["idna.idnadata","pyaudio"], optimize=1, )
setup(name = "Jarvis",version = "0.01", description = "test", executables = [exe], options = dict(build_exe = buildOptions))

from cx_Freeze import setup, Executable



