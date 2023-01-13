import re
import csv

# Data of Serial Transmission stored in a file
file = open("input.txt", "r")
str = file.read()

# Regular Expression parsing data
pattern = '..{46}\s*' 

# Find all matches - stored in a list
result = re.findall(pattern, str)

# Write results in a .csv file€
data = open("data.csv", "w")

for x in result:
    data.write(x + '\n')

data.close()

