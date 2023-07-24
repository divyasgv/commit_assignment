import boto3

def get_csv_from_s3(bucket_name,s3_key,file
_name):
    s3=boto3.client('s3')
try:
    s3.download_file(bucket_name,s3_key,file name)
    print("File downloaded successfully from s3")
 except Exception as e:
    print(f"An error occured:{str(e)}")

#specify the bucket name,s3 key,and local file path to save the downloaded file
bucket_name = 'fintech sem5'
file_name ='test_14.py'
s3_key = 'data.csv'

get _csv_from_s3(bucket_name,s3_key,file_name)	
