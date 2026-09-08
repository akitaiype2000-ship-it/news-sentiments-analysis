import requests
import json

api_key = "ba901fc4867d4cc3b1dcfc0f87949b3e"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

response = requests.get(url)
data = response.json()

print(data)
