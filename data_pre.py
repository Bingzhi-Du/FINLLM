###this is the pre-process data pipeline
from data_ingestion import fetch_alpha_vantage_data, fetch_newsapi_data, fetch_github_repositories
import json


def pp_read_json(file_path):
    with open(file_path, 'r') as file:
        json.load(file)
    return json.load(file)


pp_read_json(file_path="")
