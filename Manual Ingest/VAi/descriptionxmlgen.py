import sys
import xml.etree.ElementTree as ET
''' sys.argv[0] = script name
    sys.argv[1] = csv line to be parsed
    sys.argv[2] = delimiter
'''

data = sys.argv[1].split(sys.argv[2])
schemaName = 'scala'
root = ET.Element(schemaName, xmlns="urn:isbn:1-931666-22-9",
                  xsi="http://www.w3.org/2001/XMLSchema-instance",
                  schemaLocation="urn:isbn:1-931666-22-9 ../schemas/ead2002.xsd")

ET.SubElement(root, 'type').text = 'http://purl.org/dc/dcmitype/Collection'
ET.SubElement(root, 'scalaId')
ET.SubElement(root, 'localId').text = data[1]
ET.SubElement(root, 'titel').text = data[2]
ET.SubElement(root, 'beschrijving').text = data[6]
ET.SubElement(root, 'archiefvormer')
ET.SubElement(root, 'datering').text = '/'.join(data[3:5]) if data[3] != '' and data[4] != '' else '/'.join(data[3], "..") if data[3] != '' and data[4] == '' else '/'.join("..", data[4]) if data[3] == '' and data[4] != '' else ''
ET.SubElement(root, 'isOnderdeelVan').text = data[5]
ET.SubElement(root, 'naamBewaarinstelling')
ET.SubElement(root, 'idBewaarinstelling')
ET.SubElement(root, 'toegangsvoorwaarden')

ET.ElementTree(root).write(sys.stdout, encoding="unicode", xml_declaration=True)