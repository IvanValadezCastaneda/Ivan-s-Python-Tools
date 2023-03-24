import xml.etree.ElementTree as ET
import os


directory = input("Enter directory: ")

# Get a list of all .xml files in the directory
xml_files = [f for f in os.listdir(directory) if f.endswith(".xml")]

# The properties that you want to add to your .xml files
properties = """
<properties>
  <prop name="Name">
   <prop name="es_MX.utf8" />
  </prop>
  <prop name="Size">2085 796</prop>
  <prop name="BackColor">ISA_11_BackgroundGrey</prop>
 </properties>
"""

# Counter for the number of modified files
modified_files = 0

for xml_file in xml_files:
  # Check if the file ends with "SYM.xml"
  if xml_file.endswith("DETAILED.xml"):
    tree = ET.parse(os.path.join(directory, xml_file))
    root = tree.getroot()

    properties_elem = root.find("properties")

    if properties_elem is not None:
      root.remove(properties_elem)
      root.append(ET.fromstring(properties))

    tree.write(os.path.join(directory, xml_file))

    modified_files += 1

    print(f"Modified file: {xml_file}")

print(f"Total modified files: {modified_files}")
