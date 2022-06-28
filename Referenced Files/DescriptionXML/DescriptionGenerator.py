import pandas as pd
import xml.etree.ElementTree as ET
import sys
import os

""" sys.argv[0] = script name
    sys.argv[1] = XLSX path
    sys.argv[2] = output dir
"""

""" 1. Read records from XLS"""
xlsPath = sys.argv[1]
dataFrame = pd.read_excel(xlsPath, na_filter=False, dtype=object)
records = dataFrame.to_dict('records')

""" 2. Define how to build the XML"""
""" Expected XLSX headers in records: destinationDirectory	creation	archdeskLevel	unitTitle	scalaID	repositoryCode	localID	unitDate	corpName	creatorName	producerName	scopeContent	relatedMaterial	accessRestrict	processDate
"""
def buildXml (schemaName, namespaces, record):
    root = ET.Element(schemaName, **namespaces)

    eadheader = ET.SubElement(root, "eadheader")
    eadid = ET.SubElement(eadheader, "eadid")
    filedesc = ET.SubElement(eadheader, "filedesc")
    titlestmt = ET.SubElement(filedesc, "titlestmt")
    titleproper = ET.SubElement(titlestmt, "titleproper")
    profiledesc = ET.SubElement(eadheader, "profiledesc")
    creation = ET.SubElement(profiledesc, "creation")
    creation.text = record["creation"]

    archdesc = ET.SubElement(root, "archdesc")
    archdesc.set("level", record["archdeskLevel"])
    did = ET.SubElement(archdesc, "did")
    unittitle = ET.SubElement(did, "unittitle")
    unittitle.text = record["unitTitle"]
    unitid1 = ET.SubElement(did, "unitid")
    unitid1.set("label", "scalaID")
    unitid1.text = record["scalaID"]
    unitid2 = ET.SubElement(did, "unitid")
    unitid2.set("repositorycode", record["repositoryCode"])
    unitid2.set("label", "localID")
    unitid2.text = record["localID"]
    unitdate = ET.SubElement(did, "unitdate")
    unitdate.text = record["unitDate"]
    repository = ET.SubElement(did, "repository")
    corpname = ET.SubElement(repository, "corpname")
    corpname.text = record["corpName"]

    origination1 = ET.SubElement(did, "origination")
    origination1.set("label", "creator")
    name1 = ET.SubElement(origination1, "name")
    name1.text = record["creatorName"]
    origination2 = ET.SubElement(did, "origination")
    origination2.set("label", "producer")
    name2 = ET.SubElement(origination2, "name")
    name2.text = record["producerName"]
    scopecontent = ET.SubElement(archdesc, "scopecontent")
    p1 = ET.SubElement(scopecontent, "p")
    p1.text = record["scopeContent"]
    relatedmaterial = ET.SubElement(archdesc, "relatedmaterial")
    p2 = ET.SubElement(relatedmaterial, "p")
    p2.text = record["relatedMaterial"]
    accessrestrict = ET.SubElement(archdesc, "accessrestrict")
    p3 = ET.SubElement(accessrestrict, "p")
    p3.text = record["accessRestrict"]
    processinfo = ET.SubElement(archdesc, "processinfo")
    p4 = ET.SubElement(processinfo, "p")
    date = ET.SubElement(p4, "date")
    date.text = record["processDate"].strftime("%Y-%m-%d")
    dsc = ET.SubElement(archdesc, "dsc")
    dsc.set("type", "combined")

    xml = ET.tostring(root, encoding="UTF-8",
                      xml_declaration=True).decode("UTF-8")
    fileName = record["destinationDirectory"] + ".xml"

    return (xml, fileName)

""" 3. Build and save XML for each record"""
outputDir = sys.argv[2]
schemaName = "ead"
namespaces = {"xmlns": "urn:isbn:1-931666-22-9", "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
              "xsi:schemaLocation": "urn:isbn:1-931666-22-9 http://www.loc.gov/ead/ead.xsd"}
for record in records:
    xml, fileName = buildXml(schemaName, namespaces, record)
    savePath = os.path.join(outputDir, fileName)
    try:
        with open(savePath, 'w', encoding='UTF-8') as file:
            print(f"Writing descriptive metadata for {fileName}.")
            file.write(xml)
    except Exception as Argument:
        print(Argument)
