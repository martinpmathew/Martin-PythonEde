import xml.etree.ElementTree
import os

file_path = '\\rest_api\\nyse.xml'

xml_e = xml.etree.ElementTree.parse(os.getcwd() + file_path).getroot()
print(xml_e.tag)

for q in xml_e.findall("quote"):
    print(type(q))
    for prop in q.attrib:
        print(prop)