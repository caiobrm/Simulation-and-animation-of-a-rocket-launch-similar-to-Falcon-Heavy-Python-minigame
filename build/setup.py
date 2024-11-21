import sys
from cx_Freeze import setup, Executable
import pygame

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("Rocket Dynamics.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["pygame", "csv", "datetime"],
        include_files = ['C:\\Users\\Caio Barros\\Desktop\\RocketDynamics\\img'],
        excludes = []
)

setup(
    name = "Rocket Dynamics",
    version = "1.0",
    description = "Simulation of  ",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
