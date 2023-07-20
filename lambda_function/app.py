import os
import boto3
import csv
import urllib.parse

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # Get bucket name and file key from the event parameter
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print(bucket)
    print(key)

    # Get the file object from S3
    file_obj = s3.get_object(Bucket=bucket, Key=key)

    # Read the file contents
    file_content = file_obj['Body'].read().decode('utf-8')

    # Use csv.reader to split the file into lines
    lines = list(csv.reader(file_content.splitlines()))

    # Count the number of lines and log it
    num_lines = len(lines)
    print(f'Number of lines in the file: {num_lines}')
              