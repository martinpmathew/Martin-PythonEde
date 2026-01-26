import os
import xml.etree.ElementTree as ET


file_path = '\\file_proc_com\\xml\\books.xml'

tree = ET.parse(os.getcwd() + file_path)
root = tree.getroot()

print(f'root is {root}')

# The find method returns the first child element containing the specified tag or matching XPath expression
print(root.find('book').get('title'))
