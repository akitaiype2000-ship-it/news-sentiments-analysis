import requests
import json

api_key = "ba901fc4867d4cc3b1dcfc0f87949b3e"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

response = requests.get(url)
data = response.json()
with open("news_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("News saved locally")
print(data)
