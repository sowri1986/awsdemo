import streamlit as st
import logging
import boto3
from botocore.exceptions import ClientError



def upload_file(uploaded_file, bucket,fileName):
    
    # Upload the file
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.upload_fileobj(uploaded_file, bucket, fileName)
    except ClientError as e:
        logging.error(e)
        return False
    return True

uploaded_file = st.file_uploader("Choose a file")


if(st.button('Upload to Bucket')):
    #st.write(os.path.basename(uploaded_file.name))
    upload_file(uploaded_file,"bit2terabyte",uploaded_file.name)

def hello_s3():
    """
    Use the AWS SDK for Python (Boto3) to create an Amazon Simple Storage Service
    (Amazon S3) resource and list the buckets in your account.
    This example uses the default settings specified in your shared credentials
    and config files.
    """
    s3_resource = boto3.resource('s3')
    st.write("Hello, Amazon S3! Let's list your buckets:")
    for bucket in s3_resource.buckets.all():
        st.write(f"\t{bucket.name}")

if __name__ == '__main__':
    hello_s3()