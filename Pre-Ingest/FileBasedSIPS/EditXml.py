from xml.etree import ElementTree as ET
import sys
import os

""" sys.argv[0] = script name
    sys.argv[1] = root folder
"""

rootDir = sys.argv[1]
# rootDir = r"C:\Users\VAIJelleKleevens\OneDrive - Vlaams Architectuurinstituut vzw\Bureaublad\unzipeditrezip\zips"

def updateXml(originalXml):
    tree = ET.parse(originalXml)
    root = tree.getroot()

    """Tree changes here:"""
    
    scopeContents = root.findall(".//scopecontent")
    for scopeContent in scopeContents:
        text = scopeContent.text
        scopeContent.text = ""
        p = ET.SubElement(scopeContent, "p")
        p.text = text

    """"""

    xmlstr = ET.tostring(root, encoding="UTF-8", xml_declaration=True).decode("UTF-8")
    with open(originalXml, 'w', encoding="UTF-8") as f:
        f.write(xmlstr)

for _rootDirs, _dirs, files in os.walk(rootDir):
    for f in files:
        print(f)
        filePath = os.path.join(rootDir, f)
        updateXml(filePath)
