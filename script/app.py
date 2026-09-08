import requests
import json
from textblob import TextBlob
api_key = "ba901fc4867d4cc3b1dcfc0f87949b3e"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

response = requests.get(url)
data = response.json()
with open("news_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("News saved locally")
pos = 0
neg = 0
neut = 0
news_data = []
for article in data["articles"]:

    title = article["title"]
    source = article["source"]["name"]
    author = article["author"]
    description = article["description"]
    published = article["publishedAt"]
    article_url = article["url"]
    # Sentiment Analysis
    blob = TextBlob(title)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
        pos += 1
    elif polarity < 0:
        sentiment = "Negative"
        neg += 1
    else:
        sentiment = "Neutral"
        neut += 1
    print("Title:", title)
    print("Source:", source)
    print("Author:", author)
    print("Published:", published)
    print("Description:", description)
    print("URL:", article_url)
    print("Sentiment:", sentiment)
    print("Polarity:", polarity)
    print("-" * 80)
    news_data.append({
    "Title": title,
    "Source": source,
    "Author": author,
    "Published": published,
    "Description": description,
    "URL": article_url,
    "Sentiment": sentiment,
    "Polarity": polarity
    })
print("\n========== SUMMARY ==========")
print("Total Articles:", len(data["articles"]))
print("Positive:", pos)
print("Negative:", neg)
print("Neutral:", neut)

