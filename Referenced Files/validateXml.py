from lxml import etree

def isValidXml(xmlString, xmlSchema):
    doc = etree.XML(xmlString.encode())
    return xmlSchema.validate(doc)
