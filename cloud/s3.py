#!/usr/bin/env python3

import boto3
import os
from botocore.exceptions import EndpointConnectionError as error

def uploadS3(*args):
    region = args[0]
    bucket_name = args[1]

    # Create AWS session
    session = boto3.Session(
            region_name=region
            )

    # Connect session to S3
    s3 = session.resource('s3')
    bucket = s3.Bucket(bucket_name)
    try:
      for subdir, dirs, files in os.walk('logs'):
          for file in files:
              absolute_path = os.path.join(subdir, file)
              with open(absolute_path, 'rb') as data:
                  bucket.put_object(Key=absolute_path, Body=data)
      return True
    except error:
        return False
         
