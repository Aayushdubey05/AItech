import os
import sys
from dotenv import load_dotenv,dotenv_values
from pathlib import Path
from google.cloud import storage
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

gcp_project_id = os.getenv("GCP_PROJECT_ID")
bucket_name = os.getenv("BUCKET_NAME")
service_account_file = os.getenv("SERVICE_ACCOUNT_FILE_PATH")

def create_gcs_bucket(gcp_project_id,bucket_name,service_account_file):
    created = False
    try:
        client = storage.Client.from_service_account_json(service_account_file)
        bucket = client.create_bucket(bucket_name)
        print(f"Bucket name: {bucket} created successfully ")
        created = True
    except Exception as e:
        print(f"Error Creation Buckets: {str(e)}")

create_gcs_bucket(gcp_project_id,bucket_name,service_account_file)


