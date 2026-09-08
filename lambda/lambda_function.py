import os
import json
import requests
import boto3

NEWS_API_KEY = os.environ["NEWS_API_KEY"]
BUCKET_NAME = os.environ["BUCKET_NAME"]


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

    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }