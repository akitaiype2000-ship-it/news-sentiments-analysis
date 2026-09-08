import psycopg2
import pandas as pd

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="YOUR_RDS_ENDPOINT",
    database="postgres",
    user="postgres",
    password="YOUR_PASSWORD",
    port="5432"
)

cursor = conn.cursor()

# Read CSV
df = pd.read_csv("news_sentiment.csv")

# Insert each row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO news
        (title, source, author, published, description, url, sentiment, polarity)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row["Title"],
        row["Source"],
        row["Author"],
        row["Published"],
        row["Description"],
        row["URL"],
        row["Sentiment"],
        row["Polarity"]
    ))

conn.commit()

print("News inserted successfully")

cursor.close()
conn.close()