import json

# json.load() to read JSON File - It takes fiel content not the file path
with open ("weather.json") as f:
    text = json.load(f)
    print(text)
    # print(text["sensors"]) # print only sensor type