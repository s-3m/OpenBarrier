import os
import json

db = {}
if os.path.exists('db_file.json'):
    with open('db_file.json', 'r') as file:
        db = json.load(file)


db_dict: dict = db