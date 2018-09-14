"""
module to handle Google cloud storage
Important resources 
    - https://pypi.org/project/google-cloud-storage/
    - https://cloud.google.com/storage/docs/
"""
from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    blob = bucket.blob(destination_blob_name)
    blob.make_public()

    url = blob.public_url

    message = ('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

    return (message,url)

def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()
    list_blobs = [blob.public_url for blob in blobs]
    return list_blobs

