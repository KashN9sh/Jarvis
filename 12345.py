from cx_Freeze import setup, Executable

setup(
    name = "Freelance",
    version = "1.0",
    description = "Freelance Parser",
    executables = [Executable("Jarvis.py")]
)
