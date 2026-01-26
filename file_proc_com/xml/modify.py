import os
import xml.etree.ElementTree as ET

file_path = '\\file_proc_com\\xml\\books.xml'

tree = ET.parse(os.getcwd() + file_path)
root = tree.getroot()

for child in root:
    child.tag = 'movie'
    # for removing element
    child.remove(child.find('author'))
    child.remove(child.find('year'))
    child.set('rate', '5')  # setting attribute
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ": ", sub_child.text)

