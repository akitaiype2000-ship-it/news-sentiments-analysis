import os
import json
import requests
import boto3
import psycopg2
from textblob import TextBlob
NEWS_API_KEY = os.environ["NEWS_API_KEY"]
BUCKET_NAME = os.environ["BUCKET_NAME"]

DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_PORT = int(os.environ.get("DB_PORT", "5432"))
def lambda_handler(event, context):

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

    response = requests.get(url)
    data = response.json()

    # Save JSON temporarily
    with open("/tmp/news_data.json", "w") as file:
        json.dump(data, file, indent=4)

    # Upload JSON to Amazon S3
    s3 = boto3.client("s3")

    s3.upload_file(
        "/tmp/news_data.json",
        BUCKET_NAME,
        "news_data.json"
    )
    # Connect to PostgreSQL
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS news (
    id SERIAL PRIMARY KEY,
    title TEXT,
    source TEXT,
    author TEXT,
    published TIMESTAMP,
    description TEXT,
    url TEXT,
    sentiment VARCHAR(20),
    polarity FLOAT
);
""")

conn.commit()

inserted = 0

for article in data.get("articles", []):

    title = article.get("title")
    source = article.get("source", {}).get("name")
    author = article.get("author")
    description = article.get("description")
    published = article.get("publishedAt")
    news_url = article.get("url")

    polarity = TextBlob(title or "").sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    cursor.execute("""
        INSERT INTO news
        (title, source, author, published, description, url, sentiment, polarity)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        title,
        source,
        author,
        published,
        description,
        news_url,
        sentiment,
        polarity
    ))

    inserted += 1

    conn.commit()

    cursor.close()
    conn.close()
    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }