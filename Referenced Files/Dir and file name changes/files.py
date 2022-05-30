import os
import sys

rootDir = sys.argv[1]

for _d, _dirs, files in os.walk(rootDir):
    for file in files:
        filepath, filename = os.path.split(file)
        basename, extension = os.path.splitext(filename)
        newBasename = basename.replace(".", "")
        newFilename = newBasename + extension
        oldPath = os.path.join(rootDir, filename)
        newPath = os.path.join(rootDir, newFilename)
        os.rename(oldPath, newPath)