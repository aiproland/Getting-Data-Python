import requests
import json

#serialized json text
mystring =  """{ "title" : "Data Science Book",
                "author" : "Joel Grus",
                "publicationYear" : 2019,
                "topics" : [ "data", "science", "data science"] }"""

res2 = json.loads(mystring)

print(res2)