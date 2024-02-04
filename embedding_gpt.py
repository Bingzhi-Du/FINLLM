# embedding gpt3.5 using your own dataset


import pandas as pd
from sklearn.model_selection import train_test_split
import os
import json
import data_pre
from apikey import openai_api_key
from openai import OpenAI

client = OpenAI(api_key=openai_api_key)

response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small"
)

print(response.data[0].embedding)
