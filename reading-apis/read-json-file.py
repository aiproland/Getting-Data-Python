import json

# json.load() to read JSON File - It takes fiel content not the file path
with open ("book.json") as f:
    res = json.load(f)
    print(res["info"][0]["author"])