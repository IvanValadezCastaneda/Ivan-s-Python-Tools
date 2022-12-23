import xml.etree.ElementTree as ET
import os

DETAILEDFILES = []
# The directory where your .xml files are located
# You can change this to any directory you want
directory = input("Enter directory: ")

# Get a list of all .xml files in the directory
xml_files = [f for f in os.listdir(directory) if f.endswith(".xml")]

# Print the names of all .xml files that end with "DETAILED.xml"
for xml_file in xml_files:
  if xml_file.endswith("SYM.xml"):
    print(xml_file)
    DETAILEDFILES.append(xml_file)
#print (DETAILEDFILES)

# The properties that you want to add to your .xml file
properties = """
<properties>
  <prop name="Name">
   <prop name="es_MX.utf8" />
  </prop>
  <prop name="Size">230 100</prop>
  <prop name="BackColor">ISA_11_BackgroundGrey</prop>
 </properties>
"""

# Loop through all the XML files in the DETAILEDFILES list
for xml_file in DETAILEDFILES:
  # Construct the full file path
  file_path = os.path.join(directory, xml_file)
  
  # Parse the .xml file
  tree = ET.parse(file_path)
  root = tree.getroot()
  
  # Find the <properties> element
  properties_elem = root.find("properties")
  
  # If there is a <properties> element, replace it with the new one
  if properties_elem is not None:
    root.remove(properties_elem)
    root.append(ET.fromstring(properties))
  
  # Write the updated XML to the file
  tree.write(file_path)
