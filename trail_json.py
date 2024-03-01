import json
import os


def pp_read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


pp_read_json("~data_github/python.json")
