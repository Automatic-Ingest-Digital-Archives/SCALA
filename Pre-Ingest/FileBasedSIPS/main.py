import sys
import os
import shutil
import uuid
from xmlgen_file import createXmlString
from pathlib import Path

""" sys.argv[0] = script name
    sys.argv[1] = source dir
    sys.argv[2] = output dir
    sys.argv[3] = xml description metadata output dir
    sys.argv[4] = delete original after copying to new dir TRUE/FALSE
"""

rootDir = sys.argv[1]
outputDir = sys.argv[2]
xmlOutputDir = sys.argv[3]
deleteOriginal = sys.argv[4].lower() == "true"

"""0. Create Transfer Set dir in outputDir."""
tsFolderName = os.path.basename(rootDir)
tsOutputDir = os.path.join(outputDir, tsFolderName)
Path(tsOutputDir).mkdir(parents=True, exist_ok=True)

for d, _dirs, files in os.walk(rootDir):
    for f in files:
        """1. Prepare variables + make new folder in tsOutputDir."""
        relDir = os.path.relpath(d, rootDir)
        filenameWithExtension = os.path.basename(f)
        fileSipTargetDirName = f"{filenameWithExtension}-{str(uuid.uuid4())}"
        fileSipTargetDir = os.path.join(tsOutputDir, fileSipTargetDirName)
        Path(fileSipTargetDir).mkdir(parents=True, exist_ok=True)

        """2. Copy file in targetDir. Optionally delete rootDir."""
        try:
            sourceFile = os.path.join(d, f)
            shutil.copy(sourceFile, fileSipTargetDir)
            if deleteOriginal == True:
                os.rmdir(rootDir)
        except Exception as Argument:
            print(Argument)

        """3. Make description xml and put in xmlOutputDir."""
        relFilePath = os.path.join(relDir, f).replace("\\", "/")
        xml = createXmlString(relFilePath, filenameWithExtension)
        xmlSavePath = os.path.join(xmlOutputDir, f"{fileSipTargetDirName}.xml")
        try:
            with open(xmlSavePath, 'w', encoding='UTF-8') as file:
                file.write(xml)
        except Exception as Argument:
            print(Argument)
