#!/usr/bin/env python3

import boto3
import os
from botocore.exceptions import EndpointConnectionError as net_error
from dotenv import load_dotenv

# Load Environmetal variables
load_dotenv()

def uploadS3(*args):
    region = args[0]
    bucket_name = args[1]

    # Create AWS session
    session = boto3.Session(
            region_name=os.getenv('REGION'),
            aws_access_key_id=os.getenv('ACCESS_KEY'),
            aws_secret_access_key=os.getenv('SECRET_KEY')
            )

    # Connect session to S3
    s3 = session.client('s3')
    try:
      for subdir, dirs, files in os.walk('logs'):
          for file in files:
              absolute_path = os.path.join(subdir, file)
              with open(absolute_path, 'rb') as data:
                  s3.put_object(Bucket=bucket_name, Key=absolute_path, Body=data)
      return True
    except (net_error, s3.exceptions.NoSuchBucket):
        return False
         
