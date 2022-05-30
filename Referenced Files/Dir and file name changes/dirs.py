import os
import sys

rootDir = sys.argv[1]

for dirpath, dirs, _files in os.walk(rootDir):
    for dir in dirs:
        newDir = dir.replace(".", "")
        oldPath = os.path.join(dirpath, dir)
        newPath = os.path.join(dirpath, newDir)
        os.rename(oldPath, newPath)