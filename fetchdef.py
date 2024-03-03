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
def fetch_github_repositories(query_list=["data science"], language_list=["python"]):
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


def fetch_github_repositories_beta(query_list=["data science"], language_list=["python"], per_page=100, max_pages=10):
    os.makedirs('data_github', exist_ok=True)
    url = "https://api.github.com/search/repositories"

    # 可选：使用GitHub个人访问令牌（PAT）进行认证，以提高速率限制
    headers = {
        'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'
    }

    for query in query_list:
        for language in language_list:
            all_repositories = []
            for page in range(1, max_pages + 1):
                params = {
                    'q': f'{query} language:{language}',
                    'sort': 'stars',
                    'order': 'desc',
                    'per_page': per_page,
                    'page': page
                }
                response = requests.get(url, headers=headers, params=params)
                if response.status_code == 200:
                    data = response.json()
                    repositories = data.get('items', [])
                    if not repositories:
                        break  # 如果没有更多结果，退出循环
                    all_repositories.extend(repositories)
                else:
                    print(f'Failed to fetch page {page}: {response.status_code}')
                    break  # 遇到错误时退出循环

            # 将所有爬取的数据保存到文件
            filename = f'data_github/{query}_{language}.json'
            with open(filename, 'w') as file:
                json.dump(all_repositories, file, indent=4)
            print(f'Successfully saved {len(all_repositories)} repositories to {filename}')


# 示例调用
fetch_github_repositories()
