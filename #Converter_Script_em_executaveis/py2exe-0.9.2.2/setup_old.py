from cx_Freeze import setup, Executable

setup(
    name="Time_Date EXECUTABLE",
    version = "1.0.0",
    description = ".py to .exe",
    executable = [Executable("Time_Date.py")])
