import zipfile
import tempfile
import sys
import os
from xml.etree import ElementTree as ET

""" sys.argv[0] = script name
    sys.argv[1] = root folder
"""

# rootDir = sys.argv[1]
rootDir = r"C:\Users\VAIJelleKleevens\OneDrive - Vlaams Architectuurinstituut vzw\Bureaublad\unzipeditrezip\zips"
filename = "scala.xml"

def updateZip(zipname, filename, data):
    # generate a temp file
    tmpfd, tmpname = tempfile.mkstemp(dir=os.path.dirname(zipname))
    os.close(tmpfd)

    # create a temp copy of the archive without filename 
    xmlPath = ""           
    with zipfile.ZipFile(zipname, 'r') as zin:
        listOfFileNames = myzip.namelist()
        xmlPathInZip = [x for x in listOfFileNames if filename in x][0]
        myzip.extract(xmlPathInZip, rootDir)
        xmlPath = os.path.join(rootDir, xmlPathInZip)
        with zipfile.ZipFile(tmpname, 'w') as zout:
            zout.comment = zin.comment # preserve the comment
            for item in zin.infolist():
                if item.filename != filename:
                    zout.writestr(item, zin.read(item.filename))

    # create a copy of the file
    

    # replace with the temp archive
    os.remove(zipname)
    os.rename(tmpname, zipname)

    # now add filename with its new data
    with zipfile.ZipFile(zipname, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(filename, data)

for _dirpath, _dirs, zips in os.walk(rootDir):
    """ 1. Unzip file """
    """ 2. Edit scala xml """
    """ 3. Zip file """
    for zip in zips:
        xmlPath = ""
        with ZipFile(os.path.join(rootDir, zip)) as myzip:
            listOfFileNames = myzip.namelist()
            xmlPathInZip = [x for x in listOfFileNames if filename in x][0]
            myzip.extract(xmlPathInZip, rootDir)
            xmlPath = os.path.join(rootDir, xmlPathInZip)
            
        tree = ET.parse(xmlPath)
        root = tree.getroot()
        
        """Insert changes here"""
        scopeContent = root.find("scopecontent")
        text = scopeContent.text
        scopeContent.text = ""
        p = ET.SubElement(scopeContent, "p")
        p.text = text

        tree.write(xmlPath)

        with myzip.open(xmlPath, mode='w') as myXml:
            xmlContent = myXml.write(xmlContent)