import sys
import os
import shutil
import uuid
from xmlgen_file import createXmlString
from xmlValidator import isValidXml
from pathlib import Path
import requests

""" sys.argv[0] = script name
    sys.argv[1] = source dir (dir containing transfer sets)
    sys.argv[2] = output dir
    sys.argv[3] = xml description metadata output dir
    sys.argv[4] = delete original after copying to new dir TRUE/FALSE
"""

rootDir = sys.argv[1]
outputDir = sys.argv[2]
xmlOutputDir = sys.argv[3]
deleteOriginal = sys.argv[4].lower() == "true"

# rootDir = r"C:\Users\VAIJelleKleevens\OneDrive - Vlaams Architectuurinstituut vzw\Bureaublad"
# outputDir = r"C:\Users\VAIJelleKleevens\OneDrive - Vlaams Architectuurinstituut vzw\Bureaublad\testoutput"
# xmlOutputDir = r"C:\Users\VAIJelleKleevens\OneDrive - Vlaams Architectuurinstituut vzw\Bureaublad\xmltestoutput"
# deleteOriginal = False

schemaLink = "http://www.loc.gov/ead/ead.xsd"
response = requests.get(schemaLink)
xmlschema_doc = etree.fromstring(bytes(response.text, encoding='utf-8'))
xmlschema = etree.XMLSchema(xmlschema_doc)

for transferSet in next(os.walk(rootDir))[1]:
    """0. Create Transfer Set dir in outputDir."""
    print(f"Now handeling: {transferSet}")
    tsOutputDir = os.path.join(outputDir, transferSet)
    Path(tsOutputDir).mkdir(parents=True, exist_ok=True)
    transferSetDir = os.path.join(rootDir, transferSet)
    tsFolderName = transferSet

    for d, _dirs, files in os.walk(transferSetDir):
        for f in files:
            """1. Prepare variables + make new folder in tsOutputDir."""
            relDir = os.path.relpath(d, transferSetDir)
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
            xml = createXmlString(relFilePath, filenameWithExtension, tsFolderName)
            if (isValidXml(xml, xmlschema)):
                xmlSavePath = os.path.join(xmlOutputDir, f"{fileSipTargetDirName}.xml")
                try:
                    with open(xmlSavePath, 'w', encoding='UTF-8') as file:
                        file.write(xml)
                except Exception as Argument:
                    print(Argument)
            else:
                print(f"XML failed validation against schema: {schemaLink}.")
