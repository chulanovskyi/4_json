# 4_json

###Prerequisites:

Script needs a file in JSON format. Just copy that file with .json extension to the directory with the script.
For example a list of bars in JSON format can be downloaded directly from http://data.mos.ru/opendata/export/1796/json/2/1

---
This script simply help you to print out all data from file in readable format.

Script takes one required and one optional parameters: 
- name - JSON file name;
- -l or --limiter (optional) - limits the number of records to be printed;

How to use:

|Command|Description|
|pprint_json.py my_file_name.json|print out all data from file.|
|pprint_json.py my_file_name.json -l=5|print first 5 records from file|
