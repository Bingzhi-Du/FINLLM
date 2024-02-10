# fine-tune pgpt-3.5 using your own dataset
# from https://blog.futuresmart.ai/fine-tuning-gpt-35-a-step-by-step-guide
import pandas as pd
from sklearn.model_selection import train_test_split
import openai

def convert_to_gpt35_format(dataset):
    fine_tuning_data = []
    for _, row in dataset.iterrows():
        json_response = '{"Top Category": "' + row['Top Category'] + '", "Sub Category": "' + row[
            'Sub Category'] + '"}'
        fine_tuning_data.append({
            "messages": [
                {"role": "user", "content": row['Support Query']},
                {"role": "system", "content": json_response}
            ]
        })
    return fine_tuning_data

def fine_tune_gpt35(fine_tuning_data):
    openai
    openai.api_key = 'sk-xxxxx'


    # Create a new fine-tuning event
    response = openai.FineTunes.create(
        model="text-davinci-003",
        data=fine_tuning_data,
        description="Fine-tuning GPT-3.5 on custom support queries"
    )

    # Get the fine-tuning event ID
    fine_tuning_event_id = response['id']
    print(fine_tuning_event_id)

    # Check the status of the fine-tuning event
    response = openai.FineTunes.retrieve(fine_tuning_event_id)
    print(response['status'])

    # Retrieve the fine-tuned model