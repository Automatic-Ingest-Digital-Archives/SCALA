from xml.etree import ElementTree as ET
import sys
import os

""" sys.argv[0] = script name
    sys.argv[1] = root folder
"""

rootDir = sys.argv[1]
# rootDir = r"C:\Users\VAIJelleKleevens\OneDrive - Vlaams Architectuurinstituut vzw\Bureaublad\unzipeditrezip\zips"
prefixMap = {"ns0": "urn:isbn:1-931666-22-9"}

def updateXml(originalXml):
    try:
        tree = ET.parse(originalXml)
        root = tree.getroot()

        """Tree changes here:"""
        
        archdesc = root.findall(".//ns0:archdesc", prefixMap)[0]
        did = archdesc.findall(".//ns0:did", prefixMap)[0]
        oldScopeContent = root.findall(".//ns0:scopecontent", prefixMap)[0]

        scopeContent = ET.SubElement(archdesc, "ns0:scopecontent")
        p = ET.SubElement(scopeContent, "ns0:p")
        p.text = oldScopeContent.findall("ns0:p", prefixMap)[0].text

        did.remove(oldScopeContent)

        """"""

        xmlstr = ET.tostring(root, encoding="UTF-8", xml_declaration=True).decode("UTF-8")
        with open(originalXml, 'w', encoding="UTF-8") as f:
            f.write(xmlstr)
    except Exception as Argument:
        print(Argument)

for _rootDirs, _dirs, files in os.walk(rootDir):
    for f in files:
        print(f)
        filePath = os.path.join(rootDir, f)
        updateXml(filePath)
