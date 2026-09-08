import os
import json
import requests

NEWS_API_KEY = os.environ["NEWS_API_KEY"]

def lambda_handler(event, context):

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

    response = requests.get(url)
    data = response.json()

    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }