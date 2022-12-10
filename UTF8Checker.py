import os
import re

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

import csv
for element in files:
  with open(element)as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
              s1 = "Ã¡"
              s2 = "Ã©"
              s3 = "Ã\xad"
              s4 = "Ã³"
              s5 = "Ãº"
              if lines.count(s1):
                print("Character " +s1 + " equals to á found in file" + element)
              elif lines.count(s2):
                print("Character " +s2 + " equals to é found in file" + element)
              elif lines.count(s3):
                print("Character " +s3 + "equals to í found in file" + element)
              elif lines.count(s4):
                print("Character " +s4 + " equals to ó found in file" + element)
              elif lines.count(s4):
                print("Character " +s4 + "equals to ú found in file" + element)
    print("file "+element+" completed")

              
 
