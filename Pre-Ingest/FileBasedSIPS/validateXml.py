from lxml import etree

def isValidXml(xmlString, xmlSchema):
    doc = etree.parse(xmlString)
    return xmlSchema.validate(doc)
