import xml.etree.ElementTree as ET
import os


file_path = '\\file_proc_com\\xml\\books.xml'
# //C:\\Users\\LENOVO\\Codes\\exp\\PythonEDE\\file_proc_com\\xml\\
# cars_for_sale = xml.etree.ElementTree.parse(os.getcwd() + file_path).getroot()

tree = ET.parse(os.getcwd() + file_path)
root = tree.getroot()

print(f'root is {root}')
print(f'the root has following children :')
for child in root:
    print('Title :', child.attrib['title'])
    print('Author :', child[0].text)
    print('Year :', child[1].text)

print('-----------------------------')
for author in root.iter('author'):
    print(author.text)