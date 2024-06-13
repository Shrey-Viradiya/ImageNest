"""
This module helps to upload files to an S3 bucket.
"""

import boto3
from botocore.exceptions import NoCredentialsError

from src.constants import AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)


def generate_presigned_url(bucket, s3_file_name, expiration=300):
    """
    Generate a presigned URL to share an S3 object
    :param bucket: string
    :param s3_file_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    try:
        response = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket, "Key": s3_file_name},
            ExpiresIn=expiration,
        )
    except NoCredentialsError:
        print("Credentials not available")
        return None
    return response


def upload_to_s3(file_path, bucket, s3_file_name):
    """
    Upload a file to an S3 bucket.
    :param file_path: The path to the file to upload.
    :param bucket: The name of the S3 bucket.
    :param s3_file_name: The name of the file in the S3 bucket.
    :return: The URL of the uploaded file.
    """

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


def download_from_s3(bucket, s3_file_name, local_file_path):
    """
    Download a file from an S3 bucket.
    :param bucket: The name of the S3 bucket.
    :param s3_file_name: The name of the file in the S3 bucket.
    :param local_file_path: The local path where the file should be downloaded to.
    :return: None
    """

    try:
        s3.download_file(bucket, s3_file_name, local_file_path)
        print("Download Successful")
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("Credentials not available")
