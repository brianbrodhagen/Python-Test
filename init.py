import csv 
import json

file_name = 'data_file.json'
json_file = open(file_name, 'w')
with open('test.csv') as csvfile:
    readCSV = csv.DictReader(csvfile, delimiter=',')
    
    for row in readCSV:
        json.dump(row, json_file)
        json_file.write('\n')
print(f'SUCCESS, file written: {file_name}')   