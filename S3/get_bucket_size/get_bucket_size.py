import argparse
import boto3 
from boto3.session import Session 
import datetime 
from dateutil.relativedelta import relativedelta


class s3():
    def __init__(self, bucket_name, profile='default'):
        self.session = boto3.Session(profile_name=profile)
        self.s3 = self.session.resource('s3')
        self.bucket = self.s3.Bucket(bucket_name)
        self.cloudwatch = self.session.resource('cloudwatch') 
        self.namespace = 'AWS/S3'
        self.name = 'BucketSizeBytes'
        self.yesterday = datetime.datetime.today() - datetime.timedelta(days=2) 
        self.today = datetime.datetime.today() 

    def get_size(self):
        self.metric = self.cloudwatch.Metric(self.namespace,self.name)
        self.response = self.metric.get_statistics(
            StartTime=self.yesterday, 
            EndTime=self.today, 
            Statistics=['Maximum'], 
            Unit='Bytes', 
            Dimensions=[ 
                {'Name': 'BucketName', 'Value': bucket_name}, 
                {'Name': 'StorageType', 'Value': 'StandardStorage'} 
            ], 
            Period=86400 
        )
        print(self.response['Datapoints'][0]['Maximum'],self.response['Datapoints'][0]['Unit'])


if __name__ == "__main__": 
    parser = argparse.ArgumentParser(prog=__file__)
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument('--bucket',required=True, help='The name of the bucket name.')
    optional.add_argument('--profile',nargs='?',default='default',help='Use a specific profile from your credential file.')
    
    args = parser.parse_args()
    bucket_name = args.bucket
    profile = args.profile

    s3(bucket_name).get_size()
    