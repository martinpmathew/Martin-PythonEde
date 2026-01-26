import os
import xml.etree.ElementTree as ET


file_path = '\\file_proc_com\\xml\\books.xml'

tree = ET.parse(os.getcwd() + file_path)
root = tree.getroot()

print(f'root is {root}')

# the findall method only searches the children at the first nesting level.

for author in root.findall('book'):
    print(f'book is {author.get("title")}')

for author in root.findall('author'):
    print(f'author is {author.text}')