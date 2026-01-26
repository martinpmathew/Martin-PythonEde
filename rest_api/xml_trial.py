import xml.etree.ElementTree
import os

file_path = '\\rest_api\\cars.xml'

cars_for_sale = xml.etree.ElementTree.parse(os.getcwd() + file_path).getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
    print(' =', prop.text)