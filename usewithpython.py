# Import library
import os
# Make directory
os.mkdir("mypy")
# Go into the directory mypy
os.chdir("mypy/")
# Make a file
mfile = open("textpy.txt","w")
mfile.write("a")
# Rename file textpy.txt to textpy2.txt
os.rename("textpy.txt","textpy2.txt")
# Remove file
