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
    return json_files

def read_json_file_list(json_files):
    for json_file in json_files:
        # search for the file name
        # read the file into a dictionary
        file_name = os.path.splitext(os.path.basename(json_file))[0]
        if file_name and file_name != "None":
            # Read the JSON file into a DataFrame
            df = pd.read_json(json_file)
            df_name = file_name
            return df, df_name
        else:
            print(f"Skipped a file with no name or 'None' name: {json_file}")

        # 使用文件名作为字典键
        # all_data[os.path.splitext(os.path.basename(json_file))[0]] = pp_read_json(json_file)


def convert_to_gpt35_format(dataset):
    fine_tuning_data = []
    for _, row in dataset.iterrows():
        json_response = '{"Top Category": "' + row['Top Category'] + '", "Sub Category": "' + row[
            'Sub Category'] + '"}'
        fine_tuning_data.append({
            "messages": [
                {"role": "system", "content": json_response},
                {"role": "user", "content": row['Support Query']},
                {"role": "assistant", "content": row['Support Response']}

            ]
        })
    return fine_tuning_data

fin_dict = read_all_json_files(venture_capital_data_file_location)

from sklearn.model_selection import train_test_split

def train_val_split(dataset):
    train_data, val_data = train_test_split(
        dataset,
        test_size=0.2,
        stratify=dataset['Top Category'],
        random_state=42  # for reproducibility
    )
    return train_data, val_data


train_val_split
