import os
import xml.etree.ElementTree as ET

file_path = '\\file_proc_com\\xml\\Hotel.xml'

category = {
    'Vegan Products': {
        'Good Morning Sunshine': {
            "type": "cereals", "producer": "OpenEDG Testing Service", "price": "9.90", "currency": "USD"},
        'Spaghetti Veganietto': {
            "type": "pasta", "producer": "Programmers Eat Pasta", "price": "15.49", "currency": "EUR"},
        'Fantastic Almond Milk': {
            "type": "beverages", "producer": "Drinks4Coders Inc.", "price": "19.75", "currency": "USD"},
    },
}
root = ET.Element('shop')
for categ in category:
    cat = ET.SubElement(root, 'category')
    cat.set('name', categ)
    for product, value in category[categ].items():
            prd = ET.SubElement(root, 'product')
            prd.set('name', product)
            for key, val in value.items():
                ET.SubElement(prd, key).text = val
                # prd.set(key, val)
        
ET.dump(root)
tree = ET.ElementTree(root)
with open("shop.xml", "wb") as file:
    tree.write(file, encoding="UTF-8", xml_declaration=True)

# Objectives

#     improving the student's skills in building an XML document;
#     using the Element class and the SubElement function.

# Scenario

# You are a programmer working for an online store. Your task is to build an XML document containing information about the three vegan products available in the store:

# <?xml version="1.0"?>
# <shop>
#     <category name="Vegan Products">
#         <product name="Good Morning Sunshine">
#             <type>cereals</type>
#             <producer>OpenEDG Testing Service</producer>
#             <price>9.90</price>
#             <currency>USD</currency>
#         </product>
#         <product name="Spaghetti Veganietto">
#             <type>pasta</type>
#             <producer>Programmers Eat Pasta</producer>
#             <price>15.49</price>
#             <currency>EUR</currency>
#         </product>
#         <product name="Fantastic Almond Milk">
#             <type>beverages</type>
#             <producer>Drinks4Coders Inc.</producer>
#             <price>19.75</price>
#             <currency>USD</currency>
#         </product>
#     </category>
# </shop>

# Save the document to the shop.xml file. Use UTF-8 character encoding and don't forget to add the prolog to the beginning of the file. Good luck!
