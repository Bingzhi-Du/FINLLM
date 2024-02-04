###this is the pre-process data pipeline
from data_ingestion import fetch_alpha_vantage_data, fetch_newsapi_data, fetch_github_repositories
import json
import glob
import os
import pandas as pd

def pp_read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


###data file location
venture_capital_data_file_location = "../FINLLM/data"


def read_all_json_files(directory_path):
    json_files = glob.glob(f"{directory_path}/*.json")

    for json_file in json_files:
        # search for the file name
        # read the file into a dictionary
        file_name = os.path.splitext(os.path.basename(json_file))[0]
        if file_name and file_name != "None":
            # Read the JSON file into a DataFrame
            df = pd.read_json(json_file)
            df_name = file_name
            # Store the DataFrame in a dictionary with the file name as the key
            df[df_name] = df
        else:
            print(f"Skipped a file with no name or 'None' name: {json_file}")

        # 使用文件名作为字典键
        # all_data[os.path.splitext(os.path.basename(json_file))[0]] = pp_read_json(json_file)
    return df


fin_dict = read_all_json_files(venture_capital_data_file_location)

from sklearn.model_selection import train_test_split


# Stratified splitting. Assuming 'Top Category' can be used for stratification
def train_val_split(dataset):
    train_data, val_data = train_test_split(
        dataset,
        test_size=0.2,
        stratify=dataset['Top Category'],
        random_state=42  # for reproducibility
    )
    return train_data, val_data