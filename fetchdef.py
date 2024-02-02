# functions of fetch api data
import requests
import json
import os
from datetime import datetime, timedelta


def fetch_alpha_vantage_data(apikey_Alpha_Vantage, industries):
    url_Alpha_Vantage = "https://www.alphavantage.co/query"
    os.makedirs('data', exist_ok=True)

    for industry in industries:
        param_Alpha_Vantage = {
            "function": "NEWS_SENTIMENT",
            "time_from": "20220410T0130",
            "limit": 1000,
            "topics": industry,
            "apikey": apikey_Alpha_Vantage
        }

        response = requests.get(url_Alpha_Vantage, params=param_Alpha_Vantage)
        data = response.json()

        # 保存数据到 JSON 文件
        with open(f'data/{industry}.json', 'w') as file:
            json.dump(data, file, indent=4)


def fetch_newsapi_data(apikey_news, keywords_list):
    url_newsapi = "https://newsapi.org/v2/everything"

    # 获取前一天的日期
    current_date = datetime.now()
    date = current_date - timedelta(days=1)
    formatted_date = date.strftime('%Y-%m-%d')

    # 创建存储数据的文件夹
    os.makedirs('data_newsapi', exist_ok=True)

    # 遍历关键词列表并发送请求
    for keywords in keywords_list:
        params_newsapi = {
            "q": keywords,
            "from": formatted_date,
            "sortBy": "publishedAt",
            "apiKey": apikey_news
        }

        response = requests.get(url_newsapi, params=params_newsapi)
        data = response.json()

        # 将数据保存到 JSON 文件
        with open(f'data_newsapi/{keywords.replace(" ", "_")}.json', 'w') as file:
            json.dump(data, file, indent=4)


# factch github data
def fetch_github_repositories(query_list, language_list=["python"]):
    os.makedirs('data_github', exist_ok=True)

    url = "https://api.github.com/search/repositories"
    if not query_list:
        # 如果没有提供 query_list，对每种语言执行默认操作
        for language in language_list:
            params = {
                'q': f'language:{language}',
                'sort': 'stars',
                'order': 'desc'
            }
            response = requests.get(url, params=params)
            data = response.json()
            with open(f'data_github/{language}.json', 'w') as file:
                json.dump(data, file, indent=4)
    else:
        # 如果提供了 query_list，遍历它和 language_list
        for query in query_list:
            for language in language_list:
                params = {
                    'q': f'{query} language:{language}',
                    'sort': 'stars',
                    'order': 'desc'
                }
                response = requests.get(url, params=params)
                data = response.json()
                with open(f'data_github/{query}_{language}.json', 'w') as file:
                    json.dump(data, file, indent=4)
