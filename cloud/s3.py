#!/usr/bin/env python3

import boto3
import os

def uploadS3(*args):
    region = args[0]
    bucket_name = args[1]

    session = boto3.Session(
            region_name=region
            )
    s3 = session.resource('s3')
