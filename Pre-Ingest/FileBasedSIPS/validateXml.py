from lxml import etree

def isValid(filePath, xmlSchema):
    with open (filePath, "r") as myfile:
        doc = etree.parse(myfile)
        return xmlSchema.validate(doc)
