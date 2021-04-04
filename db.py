import xml.etree.ElementTree as ET


XML = 'db.xml'

tree = ET.parse(XML)
root = tree.getroot()

attrib = {}

attrib = {'name': 'Book3'}
element = root.makeelement('topic', attrib)
root.append(element)
# adding an element to the seconditem node

attrib2 = {'name': 'extension'}
attrib3 = {'name': ' '}


ET.SubElement(root[4], 'note', attrib2)
ET.SubElement(root[4][0], 'text', {'': ' '})
ET.SubElement(root[4][0], 'timestamp', {'': ' '})

# create a new XML file with the new element
tree.write(XML)