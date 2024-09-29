import json

from db import db_dict


def json_wright():
    with open('db_file.json', 'w') as file:
        json.dump(db_dict, file)
