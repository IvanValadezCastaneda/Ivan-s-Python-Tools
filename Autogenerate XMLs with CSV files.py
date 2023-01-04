import csv
import os

# Try to import xml.etree.ElementTree. If it is not installed, install it using pip
try:
  import xml.etree.ElementTree as ET
except ImportError:
  import pip
  pip.main(['install', 'xml.etree.ElementTree'])
  import xml.etree.ElementTree as ET

# The properties that you want to add to your .xml files
properties = """
<properties>
  <prop name="Name">
   <prop name="es_MX.utf8"></prop>
  </prop>
  <prop name="Size">250 250</prop>
  <prop name="BackColor">ISA_11_BackgroundGrey</prop>
  <prop name="RefPoint">-1 -1</prop>
  <prop name="InitAndTermRef">True</prop>
  <prop name="SendClick">False</prop>
  <prop name="RefFileName"></prop>
  <prop name="DPI">96</prop>
  <prop name="PDPI">93.23185778609438</prop>
  <prop name="layoutType">None</prop>
 </properties>
"""

# Get the input CSV file location from the user
input_filename = input("Enter the location of the input CSV file: ")

# Get the output directory location from the user
output_dir = input("Enter the location where the XML files should be created: ")

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
  os.makedirs(output_dir)

# Initialize a counter for the number of XML files created
num_files_created = 0

# Open the input CSV file
with open(input_filename, 'r') as input_file:
  csv_reader = csv.reader(input_file)

  # Iterate over the rows in the CSV
  for row in csv_reader:

    # Get the title from the first column
    title = row[0]

    # Create the XML file with the specified wrapper
    xml_file = f"<?xml version='1.0' encoding='UTF-8'?><panel version='14'>{properties}</panel>"

    # Create the XML file with the title as the filename
    filename = os.path.join(output_dir, title + '.xml')
    with open(filename, 'w') as output_file:
      output_file.write(xml_file)

    num_files_created += 1

    print(f"File {filename} created")

print(f"{num_files_created} XML files were created")
