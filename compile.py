#!/usr/bin/python
"""
Tool to compile the main
plus the bibliography.
An exception is raised if
compilation error
Exit if any exception is caught

"""
import subprocess, sys

commands = [
    ['pdflatex', sys.argv[1]],
    ['bibtex', sys.argv[1].strip('.tex') + '.aux'],
    ['pdflatex', sys.argv[1]],
    ['pdflatex', sys.argv[1]]
]

for c in commands:
    subprocess.call(c)
