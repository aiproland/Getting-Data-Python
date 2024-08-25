import requests
import json

api_url = requests.get("https://api.geckoterminal.com/api/v2/networks")
# deserializing the response - json.loads() to decode JSON formatted String
api_content = json.loads(api_url.content)

print(api_content)