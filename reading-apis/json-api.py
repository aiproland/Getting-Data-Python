import requests
import json

url = requests.get("https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Stack%20Overflow")
# deserializing the response - json.loads() to decode JSON formatted String
res = json.loads(url.content)

print(res)

