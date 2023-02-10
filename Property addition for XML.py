import xml.etree.ElementTree as ET
import os

# The directory where your .xml files are located
# You can change this to any directory you want
directory = input("Enter directory: ")

# Get a list of all .xml files in the directory
xml_files = [f for f in os.listdir(directory) if f.endswith(".xml")]

properties = """
  <prop name="RefFileName">Scs/ui/reference/objectReference.xml</prop>
"""

modified_files = 0

for xml_file in xml_files:
  if xml_file.endswith(".xml"):
    tree = ET.parse(os.path.join(directory, xml_file))
    root = tree.getroot()

    properties_elem = root.find("properties")

    if properties_elem is not None:
      properties_elem.append(ET.fromstring(properties))

    tree.write(os.path.join(directory, xml_file))

    modified_files += 1

    print(f"Modified file: {xml_file}")

print(f"Total modified files: {modified_files}")
