import boto3

s3 = boto3.client("s3")

bucket_name = "YOUR_BUCKET_NAME"

s3.upload_file(
    "news_data.json",
    bucket_name,
    "news_data.json"
)

print("File uploaded successfully")