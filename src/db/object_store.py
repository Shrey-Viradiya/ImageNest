"""
This module helps to upload files to an S3 bucket.
"""

import boto3
from botocore.exceptions import NoCredentialsError

from src.constants import AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY


def upload_to_s3(file_path, bucket, s3_file_name):
    """
    Upload a file to an S3 bucket.
    :param file_path: The path to the file to upload.
    :param bucket: The name of the S3 bucket.
    :param s3_file_name: The name of the file in the S3 bucket.
    :return: The URL of the uploaded file.
    """
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION,
    )

    try:
        s3.upload_file(file_path, bucket, s3_file_name)
        print("Upload Successful")
        return f"https://{bucket}.s3.amazonaws.com/{s3_file_name}"
    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None
