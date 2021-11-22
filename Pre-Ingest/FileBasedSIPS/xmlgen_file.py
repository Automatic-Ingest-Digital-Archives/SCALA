import xml.etree.ElementTree as ET

schemaName = "ead"
namespaces = {"xmlns": "urn:isbn:1-931666-22-9", "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
              "xsi:schemaLocation": "urn:isbn:1-931666-22-9 http://www.loc.gov/ead/ead.xsd"}
fileName = "description.xml"

def createXmlString (path, filename):
    root = ET.Element(schemaName, **namespaces)

    eadheader = ET.SubElement(root, "eadheader")
    eadid = ET.SubElement(eadheader, "eadid")
    filedesc = ET.SubElement(eadheader, "filedesc")
    titlestmt = ET.SubElement(filedesc, "titlestmt")
    titleproper = ET.SubElement(titlestmt, "titleproper")
    profiledesc = ET.SubElement(eadheader, "profiledesc")
    creation = ET.SubElement(profiledesc, "creation")

    archdesc = ET.SubElement(root, "archdesc")
    archdesc.set("level", "item")
    did = ET.SubElement(archdesc, "did")
    unittitle = ET.SubElement(did, "unittitle")
    unittitle.text = filename
    unitIdOriginalFilepath = ET.SubElement(did, "unitid")
    unitIdOriginalFilepath.set("label", "original_filepath")
    unitIdOriginalFilepath.text = path

    xml = ET.tostring(root, encoding="UTF-8", xml_declaration=True).decode("UTF-8")
    return xml
