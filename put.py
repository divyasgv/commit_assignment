import boto3
def upload_csv_to_s3(bucket_name, file_name, s3_key):
s3 = boto3.client('s3')
try:
s3.upload_file(file_name, bucket_name, s3_key)
print("File uploaded successfully to s3")
except fileNotFounderError:
print("The file was not found")
except Exception as e:
print(f"An error occurred: {str(e)}")

bucket_name = 'etls3bucket11'
file_name = 'data.csv'
s3_key = 'new/data.csv'

upload_csv_to_s3(bucket_name,file_name,s3_key
