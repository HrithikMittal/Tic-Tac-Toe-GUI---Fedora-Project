import os
from setuptools import setup
from nvpy import nvpy

setup(
    name = "myscript",
    version = "1.0",
    author = "Adhikansh Mittal",
    author_email = "adhikanshmittal@gmail.com",
    description = "Tic Tac Toe game",
    license = "BSD",
    url = "https://github.com/HrithikMittal/Tic-Tac-Toe-GUI---Fedora-Project",
    packages=['myscript'],
    entry_points = {
        'console_scripts' : ['myscript = myscript.myscript:main']
    },
    data_files = [
        ('share/applications/', ['tictaktoe.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)