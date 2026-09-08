import psycopg2

conn = psycopg2.connect(
    host="YOUR_RDS_ENDPOINT",
    database="postgres",
    user="postgres",
    password="YOUR_PASSWORD",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM news")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()