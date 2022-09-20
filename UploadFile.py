from distutils.command import upload
import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "singular-acumen-350204-72ca2ce1d476.json"

storage_client = storage.Client()

dir(storage_client)

 # create a Bucket object
bucket_name = 'bucketfile-1'
bucket = storage_client.bucket(bucket_name)
bucket.location = 'US'
bucket = storage_client.create_bucket(bucket)

# print Bucket Detail
vars(bucket) 

# Accessing a Specific Bucket
my_bucket = sorage_client.get_bucket('bucketfile-1')

# Upload Files
def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob =  bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

file_path = r'C:\Users\test\Pictures\FOTO DAVA'
upload_to_bucket('FotoDava1', os.path.join(file_path, 'IMG_0619.JPG','bucketfile-1'))

# Download Files
def download_file_from_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob =  bucket.blob(blob_name)
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob, f)
        return True
    except Exception as e:
        print(e)
        return False

bucket_name="bucketfile-1"
download_file_from_bucket('FotoDava1', os.path.join(os.getcwd(), 'IMG_0619.JPG') bucket_name)