import xml.etree.ElementTree as ET
import os

DETAILEDFILES = []
# The directory where your .xml files are located
# You can change this to any directory you want
directory = input("Enter directory")

# Get a list of all .xml files in the directory
xml_files = [f for f in os.listdir(directory) if f.endswith(".xml")]

# Print the names of all .xml files that end with  desired word "desiredword.xml"
for xml_file in xml_files:
  if xml_file.endswith(".xml"):
    print(xml_file)
    DETAILEDFILES.append(xml_file)
#print (DETAILEDFILES)

# The name of the .xml file that you want to update
xml_file = input(" Ingresa el archivo ")

# The properties that you want to add to your .xml file
properties = """
<properties>
  <prop name="Name">
  </prop>
  <prop name="Size"></prop>
  <prop name="BackColor"></prop>
  <prop name="RefFileName" />
  <prop name="layoutType">None</prop>
 </properties>
"""

# Parse the .xml file
tree = ET.parse(xml_file)
root = tree.getroot()

# Find the <properties> element
properties_elem = root.find("properties")

# If there is a <properties> element, replace it with the new one
if properties_elem is not None:
  root.remove(properties_elem)
  root.append(ET.fromstring(properties))

# Write the updated XML to the file
tree.write(xml_file)
