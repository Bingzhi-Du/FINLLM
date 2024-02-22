# fine-tune pgpt-3.5 using your own dataset
# from https://blog.futuresmart.ai/fine-tuning-gpt-35-a-step-by-step-guide
import pandas as pd
from sklearn.model_selection import train_test_split
import openai
from openai import OpenAI
from apikey import openai_api_key
from sklearn.model_selection import train_test_split

client = OpenAI(api_key=openai_api_key)


# {"messages":
# [
# {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
# {"role": "user", "content": "What's the capital of France?"},
# {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}
# ]
# }



def fine_tune_gpt35(fine_tuning_data):
    openai
    openai.api_key = openai_api_key


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