import os 
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.cloudconnect import bucket_name,service_account_file,gcp_project_id,create_gcp_bucket
from google.cloud import storage
from pydantic import BaseModel


class cloud_interation:
    def __init__(self,bucket_name,service_account_file,project_id):
        self.bucket_name = bucket_name ## creating the new variable bucket to store the name of the bucket assigned during configurations
        self.service_account_file = service_account_file ## creating the new variable service_account_file to store the name of the service_account_file assigned during configurations
        self.projcet_id = project_id  ## creating the new variable gcp_project_id to store the name of the gcp_project_id assigned during configurations 
    
    
    def upload_object_to_bucket(self,source_file,destination_blob_name):
        try:
            # Initialize a GCS client
            client = storage.Client.from_service_account_json(self.service_account_file)

            #Get a reference to the target GCS bucket
            bucket = client.get_bucket(self.bucket_name)

            #Upload the local file to GCS
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_filename(source_file)

            print(f'File {source_file} uploaded to {self.bucket_name}/{destination_blob_name}')

        except Exception as e:
            print(f"Error uploading the File: {e}")

    def retrieve_object_from_bucket(self,object_name,destination_file_path):

        try:
            client = storage.Client.from_service_account_json(self.service_account_file)

            #Get the bucket 
            bucket = client.get_bucket(self.bucket_name)

            #get the blob (Object) from the Bucket
            blob = bucket.blob(object_name)

            blob.download_to_filename(destination_file_path)

            print(f"Object '{object_name}' retrieved and saved to '{destination_file_path}'.")

        except Exception as e:
            print(f"Error retriving the file: {e}")
    


cloudfeature = cloud_interation(bucket_name,service_account_file,gcp_project_id)