import requests
import json

api_key = "ba901fc4867d4cc3b1dcfc0f87949b3e"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

response = requests.get(url)
data = response.json()
with open("news_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("News saved locally")
for article in data["articles"]:

    title = article["title"]
    source = article["source"]["name"]
    author = article["author"]
    description = article["description"]
    published = article["publishedAt"]
    article_url = article["url"]

    print("Title:", title)
    print("Source:", source)
    print("Author:", author)
    print("Published:", published)
    print("Description:", description)
    print("URL:", article_url)
    print("-" * 80)
print(data)
