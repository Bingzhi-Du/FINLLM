# Description: This file is used to fetch data from Alpha Vantage and News API
from apikey import apikey_Alpha_Vantage, apikey_news
from fetchdef import fetch_newsapi_data, fetch_alpha_vantage_data, fetch_github_repositories


# Define the industries list
industries = [
    "economy_macro", "energy_transportation", "finance",
    "life_sciences", "manufacturing", "real_estate",
    "retail_wholesale", "technology"
]
# Define the keywords list
keywords_list = ["data science", "machine learning", "artificial intelligence", "cs job"]  #
# programming language list
language_list = ["objective-c", "groovy", "powershell", "haskell", "julia", "dart", "coffeescript", "vba", "assembly",
                 "abap", "plsql", "t-sql", "plpgsql", "transact-sql", "sqlpl", "plsql", "t-sql", "tsql", "sql", "mysql",
                 "postgresql", "oracle", "microsoft sql server", "sqlite", "mongodb", "redis", "cassandra", "couchbase",
                 "couchdb", "neo4j", "orientdb", "arangodb", "ravendb", "cosmos db"]
language_list_condensed = []
# "python", "java", "javascript", "c++", "c#", "rust", "go", "kotlin", "swift", "ruby","php", "typescript", "shell", "html", "css", "r", "scala", "perl", "lua", "matlab",

# Fetch data from Alpha Vantage and News API
# fetch_alpha_vantage_data(apikey_Alpha_Vantage, industries)
# fetch_newsapi_data(apikey_news, keywords_list)
fetch_github_repositories(query_list=None, language_list=language_list)
