import xml.etree.ElementTree as ET
import os

# The directory where your .xml files are located
# You can change this to any directory you want
directory = input("Enter directory: ")

# Get a list of all .xml files in the directory
xml_files = [f for f in os.listdir(directory) if f.endswith(".xml")]

# The properties that you want to add to your .xml files
properties = """
  <prop name="RefFileName">Scs/ui/reference/objectReference.xml</prop>
"""

# Counter for the number of modified files
modified_files = 0

# Iterate over the .xml files
for xml_file in xml_files:
  # Check if the file ends with ".xml"
  if xml_file.endswith(".xml"):
    # Parse the .xml file
    tree = ET.parse(os.path.join(directory, xml_file))
    root = tree.getroot()

    # Find the <properties> element
    properties_elem = root.find("properties")

    # If there is a <properties> element, add the "RefFileName" property
    if properties_elem is not None:
      properties_elem.append(ET.fromstring(properties))

    # Write the updated XML to the file
    tree.write(os.path.join(directory, xml_file))

    # Increment the modified files counter
    modified_files += 1

    # Print the name of the modified file
    print(f"Modified file: {xml_file}")

# Print the total number of modified files
print(f"Total modified files: {modified_files}")
