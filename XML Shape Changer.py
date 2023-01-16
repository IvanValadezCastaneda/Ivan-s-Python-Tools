import os
import xml.etree.ElementTree as ET

def shape_changer():
    print("ShapeChanger XML")
    print("Running")

    # Get file directory and verify it is an XML file
    file_dir = input("Enter the directory of the file to parse: ")
    if not file_dir.endswith(".xml"):
        raise ValueError("Error: Not an XML file.")

    new_shape_name = input("Enter the new shape name: ")

    tree = ET.parse(file_dir)
    root = tree.getroot()

    shape_count = 1
    for shape in root.iter("shape"):
        if shape.attrib["Name"] != "ALARM_FRAME":
            shape.attrib["Name"] = new_shape_name + str(shape_count)
            shape_count += 1

    tree.write(file_dir)
    print("File {} has been completed.".format(file_dir))
    print("Shape Changer is Stopped.")

shape_changer()
