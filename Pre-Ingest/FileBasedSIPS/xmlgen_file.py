import xml.etree.ElementTree as ET
import uuid

schemaName = "ead"
namespaces = {"xmlns": "urn:isbn:1-931666-22-9", "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
              "xsi:schemaLocation": "urn:isbn:1-931666-22-9 http://www.loc.gov/ead/ead.xsd"}
fileName = "description.xml"

def createXmlString (path, filename, parentIpName):
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
    
    unitLocalId = ET.SubElement(did, "unitid")
    unitLocalId.set("label", "localId")
    unitLocalId.text = f"{parentIpName}-{str(uuid.uuid4())}"

    creator = ET.SubElement(did, "origination")
    creator.set("label", "creator")
    name1 = ET.SubElement(creator, "name")
    name1.text = "Christiaan Kieckens" #TODO make variable

    producer = ET.SubElement(did, "origination")
    producer.set("label", "producer")
    name2 = ET.SubElement(producer, "name")
    name2.text = "AIDA" #TODO make variable

    repository = ET.SubElement(did, "repository")
    corpname = ET.SubElement(repository, "corpname")
    corpname.text = "VAi" #TODO make variable

    scopeContent = ET.SubElement(archdesc, "scopecontent")
    p = ET.SubElement(scopeContent, "p")
    p.text = "Niet raadpleegbaar." #TODO make variable

    xml = ET.tostring(root, encoding="UTF-8", xml_declaration=True).decode("UTF-8")
    return xml
