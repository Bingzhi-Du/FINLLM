# Description: This file is used to fetch data from Alpha Vantage and News API
from apikey import apikey_Alpha_Vantage, apikey_news
from fetchdef import fetch_newsapi_data, fetch_alpha_vantage_data

# Define the industries list
industries = [
    "economy_macro", "energy_transportation", "finance",
    "life_sciences", "manufacturing", "real_estate",
    "retail_wholesale", "technology"
]
# Define the keywords list
keywords_list = ["data science", "machine learning", "artificial intelligence", "cs job"]
# Fetch data from Alpha Vantage and News API
fetch_alpha_vantage_data(apikey_Alpha_Vantage, industries)
fetch_newsapi_data(apikey_news, keywords_list)
