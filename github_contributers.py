import requests

url = "https://gh-trending-api.herokuapp.com/developers"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())
