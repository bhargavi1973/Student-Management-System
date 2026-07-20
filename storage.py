# this file is to handle read and write operations in a JSON file
import json

FILE_NAME = 'student.json'

def read_data():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def write_data(student):
    with open(FILE_NAME, 'w') as file:
        json.dump(student, file, indent=4)