# test fine-tune.py
import pandas as pd
from sklearn.model_selection import train_test_split
import openai
from apikey import openai_api_key
from data_pre import train_val_split
from openai import OpenAI
import json

train_val_split


def write_to_jsonl(data, file_path):
    with open(file_path, 'w') as file:
        for entry in data:
            json.dump(entry, file)
            file.write('\n')


training_file_name = "train.jsonl"
validation_file_name = "val.jsonl"

write_to_jsonl(train_data, training_file_name)
write_to_jsonl(val_data, validation_file_name)

client = OpenAI(api_key=openai_api_key)

# Upload Training and Validation Files
training_file = client.files.create(
    file=open(training_file_name, "rb"), purpose="fine-tune"
)
validation_file = client.files.create(
    file=open(validation_file_name, "rb"), purpose="fine-tune"
)

# Create Fine-Tuning Job
suffix_name = "yt_tutorial"
response = client.fine_tuning.jobs.create(
    training_file=training_file.id,
    validation_file=validation_file.id,
    model="gpt-3.5-turbo",
    suffix=suffix_name,
)
