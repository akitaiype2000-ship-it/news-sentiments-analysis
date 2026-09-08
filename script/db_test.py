import psycopg2

try:
    conn = psycopg2.connect(
        host="YOUR_RDS_ENDPOINT",
        database="postgres",
        user="postgres",
        password="YOUR_PASSWORD",
        port="5432"
    )

    print("Database connected successfully!")

    conn.close()

except Exception as e:
    print("Connection failed")
    print(e)