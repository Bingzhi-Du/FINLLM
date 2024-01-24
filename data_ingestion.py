import requests

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
    print(response_blockchain.json())  # 假设响应是 JSON 格式
else:
    print("Error:", response_blockchain.status_code, response_blockchain.text)

