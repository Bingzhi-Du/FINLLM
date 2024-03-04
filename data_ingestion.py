# Description: This file is used to fetch data from Alpha Vantage and News API
from apikey import apikey_Alpha_Vantage, apikey_news, github_fine_grained_api_key
from fetchdef import fetch_newsapi_data, fetch_alpha_vantage_data, fetch_github_repositories_base, \
    fetch_github_repositories_language



# Define the industries list
industries = [
    "economy_macro", "energy_transportation", "finance",
    "life_sciences", "manufacturing", "real_estate",
    "retail_wholesale", "technology"
]
# Define the keywords list
keywords_list = ["data science", "machine learning", "artificial intelligence", "cs job"]  #
# programming language list
language_list = ["plpgsql", "transact-sql", "sqlpl", "plsql", "t-sql", "tsql", "sql", "mysql",
                 "postgresql", "oracle", "microsoft sql server", "sqlite", "mongodb", "redis", "cassandra", "couchbase",
                 "couchdb", "neo4j", "orientdb", "arangodb", "ravendb", "cosmos db"]
language_list_condensed = []

query_list = ["data science", "machine learning", "artificial intelligence", "cs job"]
# "python", "java", "javascript", "c++", "c#", "rust", "go", "kotlin", "swift", "ruby","php", "typescript", "shell", "html", "css", "r", "scala", "perl", "lua", "matlab",
# "objective-c", "groovy", "powershell", "haskell", "julia", "dart", "coffeescript", "vba", "assembly", "abap", "plsql", "t-sql",
# Fetch data from Alpha Vantage and News API
# fetch_alpha_vantage_data(apikey_Alpha_Vantage, industries)
# fetch_newsapi_data(apikey_news, keywords_list)
# fetch_github_repositories(query_list=None, language_list=language_list)
fetch_github_repositories_language(github_fine_grained_api_key, per_page=100, max_pages=10)
def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo-0613":  # note: future models may deviate from this
        num_tokens = 0
        for message in messages:
            num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":  # if there's a name, the role is omitted
                    num_tokens += -1  # role is always required and always 1 token
        num_tokens += 2  # every reply is primed with <im_start>assistant
        return num_tokens
    else:
        raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
  See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")
