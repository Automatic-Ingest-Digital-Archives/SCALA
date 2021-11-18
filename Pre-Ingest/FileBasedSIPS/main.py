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
"""

# rootDir = sys.argv[1]
# outputDir = sys.argv[2]
# xmlOutputDir = sys.argv[3]

rootDir = r"C:\Users\VAIJelleKleevens\Downloads\VoorbeeldSIP"
outputDir = r"C:\Users\VAIJelleKleevens\OneDrive - Vlaams Architectuurinstituut vzw\Bureaublad\testoutput"
xmlOutputDir = r"C:\Users\VAIJelleKleevens\OneDrive - Vlaams Architectuurinstituut vzw\Bureaublad\xmltestoutput"

for transferSet in next(os.walk(rootDir))[1]:
    """0. Create Transfer Set dir in outputDir."""
    tsOutputDir = os.path.join(outputDir, transferSet)
    Path(tsOutputDir).mkdir(parents=True, exist_ok=True)
    transferSetDir = os.path.join(rootDir, transferSet)

    for d, _dirs, files in os.walk(transferSetDir):
        for f in files:
            """1. Prepare variables + make new folder in tsOutputDir."""
            relDir = os.path.relpath(d, transferSetDir)
            filename = os.path.splitext(f)[0]
            fileSipTargetDirName = f"{filename}-{str(uuid.uuid4())}"
            fileSipTargetDir = os.path.join(tsOutputDir, fileSipTargetDirName)
            Path(fileSipTargetDir).mkdir(parents=True, exist_ok=True)

            """2. Copy file in targetDir."""
            sourceFile = os.path.join(d, f)
            shutil.copy(sourceFile, fileSipTargetDir)

            """3. Make description xml and put in xmlOutputDir."""
            relFilePath = os.path.join(relDir, f).replace("\\", "/")
            xml = createXmlString(relFilePath, filename)
            xmlSavePath = os.path.join(xmlOutputDir, f"{fileSipTargetDirName}.xml")
            try:
                with open(xmlSavePath, 'w', encoding='UTF-8') as file:
                    file.write(xml)
            except Exception as Argument:
                print(Argument)
