#!python3

# This program will parse out the .json files created using XOLA software, and write the data
# to a .csv file.
# A key assumption included in this code regards the implied Transaction numbers in the XOLA .json files.
# If the top level key is 'data', and the first subkey is 'object', column B in the .csv file will keep
# a running Transaction Number.  If the keys don't match this format, the Transaction Number will always
# be -1.

import json
import csv
import sys

# Function traverse_json runs through the .json file recursively and returns each data value, along with
# the "path" - the hierarchical nesting of keys.  This function can deal with any type of valid .json
# input, as it parses until there is no more data.

def traverse_json(obj, path=None):
    # First pass through the path is undefined (no keys have been identified)
    global transaction_number
    if path is None:
        transaction_number = -1
        path = []
    elif len(path) == 2 and path[1] == 'object':
        transaction_number +=1

    # If a dictionary is found, the value is used for the next round through the function
    if isinstance(obj, dict):
        return {k: traverse_json(v, path + [k]) for k, v in obj.items()}
    # If a list is found, the list values are used for the next round through the function
    elif isinstance(obj,list):
        return [traverse_json(elem, path + []) for elem in obj]
   # When a single object is found, the search is complete for that path (key hierarchy)
    else:
        value = obj
        if transaction_number != -1:
            csvData = ['Transaction'] + [transaction_number] + path + [value]
        else:
            csvData = path + [value]
        outputWriter.writerow(csvData)
    return value

# Main entry point

Fix empty lists in file.  Original file is not modified.
with open(filename + '.json', 'r') as fp1:
    jfile = fp1.readlines()

with open(filename + '_mod.json', 'w') as fp2:
    for line in jfile:
        newline = line.replace('[]', '[""]')
        fp2.writelines(newline)

try:
    with open(filename +'_mod.json') as jsonContent:
        jsonData = json.loads(jsonContent.read())
except IOError:
    print('Could not locate JSON file. Correct problem and try again.')
    sys.exit()

try:
    fp = open(filename + '_mod.csv', 'w', newline='')  # newline is for PCs to avoid double spacing
except IOError:
    print('Could not open .csv file.  Please close Excel and try again.')
    sys.exit()
outputWriter = csv.writer(fp)

a = traverse_json(jsonData)  # a is never used.
fp.close()


