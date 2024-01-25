import requests
import json
import os


url_Alpha_Vantage = "https://www.alphavantage.co/query"

param_blockchain = {
    "function": "NEWS_SENTIMENT",
    "time_from": "20220410T0130",
    "limit": 1000,
    "apikey": ""
}

response_blockchain = requests.get(url_Alpha_Vantage, params=param_blockchain)

if response_blockchain.status_code == 200:
    print("Success!")
    print(response_blockchain.json())
else:
    print("Error:", response_blockchain.status_code, response_blockchain.text)

with open('data.json', 'w') as file:
    json.dump(response_blockchain.json(), file)