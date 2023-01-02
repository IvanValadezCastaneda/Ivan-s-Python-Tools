This is a Set of Python Tools that I developed (with more to come) some of them for fun and others for work use.

Feel free to use them as you wish or to modify them.
1. Automatic Raffle Maker.
  The purpose of it is to make Raffles in an automatic and random manner without repetition and for many participants as you want
  In order to use it you must run the Script using Python and the name of the Script.
  It will be for 6 participants and 6 options to pair them against and it will output an array randomizing each participant an option to make a raffle.
  If you want to modify it just modify the number of entries or the number to compare against
 
2. Autogenerate SVGs with CSV files
   This script reads a CSV file and creates a new SVG file for each row in the CSV file. It prompts the user to enter the location of the input CSV file and the output    directory where the SVG files should be created. If the output directory does not exist, it creates it.
  The script reads the CSV file line by line and creates an SVG file for each line. The SVG file is created using the svgwrite module, which must be installed if it is   not already present. The SVG file is given a filename based on the first column of the current row in the CSV file, and the title is added as text to the SVG file.     The script then saves the SVG file and increments a counter for the number of SVG files created.
  This script could be useful in a situation where you have a CSV file with a list of titles and you want to create an SVG file for each title. The script could be       modified to include additional content in the SVG files, such as images or other text, by using the functions provided by the svgwrite module.

3. UTF8 Checker
  The purpose of this Script is to check in a series of .csv files in a given directory for if any of those files include characters reserved for the Latin UTF8 
  this means:"á", "é", "í", "ó", "ú" if by any third party script the inclusion of these characters may cause an error with this script you can sort the one that is     causing
  The script uses the os module to get the current working directory and to list all the files in the directory. It then uses the csv module to read the contents of     each file as a CSV file. For each line in the CSV file, it checks if it contains any of the specified characters using an if-elif chain. If a character is found, it   prints a message indicating which character was found in which file.
  This script could be useful in a situation where you want to search for specific characters in a set of CSV files and print a message if any of the characters are     found. You could modify the script to perform other actions based on the presence of the characters, such as replacing them with a different character or deleting  t   hem. You could also modify the script to search for other types of files besides CSV files, or to search for characters in a single file rather than a directory of     files.
  
  4. Property Changer (ChangeBackground)
  This script reads all the .xml files in a specified directory and adds the specified properties to any of the files that end with "SISMO_NAVIGATION_SYM.xml". It    uses the xml.etree.ElementTree module to parse the .xml files and add the properties to the XML.
The script prompts the user to enter the directory where the .xml files are located, and then uses the os module to get a list of all the .xml files in the directory. It then iterates over the .xml files and checks if each file ends with "SISMO_NAVIGATION_SYM.xml". If a file meets this condition, the script opens the file, adds the properties to the XML, and then saves the modified XML back to the same file. The script also keeps track of the number of modified files and prints the names of the modified files and the total number of modified files when it is finished.
This script could be useful in a situation where you have a directory of .xml files and you want to add specific properties to some of the files based on their filenames. You could modify the script to add different properties or to add the properties to a different set of files based on different criteria.
