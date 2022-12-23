import csv
import svgwrite
import os


input_filename = input("Enter the location of the input CSV file: ")


output_dir = input("Enter the location where the SVG files should be created: ")


if not os.path.exists(output_dir):
  os.makedirs(output_dir)

# Initialize a counter for the number of SVG files created
num_files_created = 0

# Open the input CSV file
with open(input_filename, 'r') as input_file:
  csv_reader = csv.reader(input_file)

  # Iterate over the rows in the CSV
  for row in csv_reader:

    title = row[0]

    # Create a new SVG file with the title as the filename
    filename = os.path.join(output_dir, title + '.svg')
    dwg = svgwrite.Drawing(filename=filename)

    # Add the title as text to the SVG file
    dwg.add(dwg.text(title, insert=(10, 20)))

    # Save the SVG file
    dwg.save()

    num_files_created += 1

    print(f"File {filename} created")

print(f"{num_files_created} SVG files were created")
