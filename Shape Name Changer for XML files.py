import xml.etree.ElementTree as ET
import os

print("Shape changer name is initiated")


file_dir = input("Enter the directory of the .xml file: ")


shape_type = input("What shapeType? ")


new_name = input("Enter the new name: ")

# Parse XML file
tree = ET.parse(file_dir)
root = tree.getroot()
count = 1

for shape in root.iter("shape"):
    
    if shape.get("shapeType") == shape_type:
        
        if shape.get("Name").startswith(shape_type):
        
            shape.set("Name", new_name + str(count))
            count += 1

print("Name changer has finished. Total names changed: ", count-1)

tree.write(file_dir)
