import boto3, argparse

class s3():
    def __init__(self, bucket_name, profile='default'):
        self.session = boto3.Session(profile_name=profile)
        self.s3 = self.session.resource('s3')
        self.bucket = self.s3.Bucket(bucket_name)

    def delete_all_object(self):
        self.s3_objects = list(self.bucket.objects.all())
        for self.s3_object in self.s3_objects:
            self.s3_object.delete()

    def delete_all_object_versions(self):
        self.s3_object_versions = list(self.bucket.object_versions.all())
        for self.s3_object_version in self.s3_object_versions:
            self.s3_object_version.delete()

    def delete_bucket(self):
        self.bucket.delete()

    def delete(self):
        self.delete_all_object()
        self.delete_all_object_versions()
        self.delete_bucket()


def main():
    s3(bucket_name, profile).delete()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=__file__)
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument('--bucket',required=True, help='The name of the bucket name.')
    optional.add_argument('--profile',nargs='?',default='default',help='Use a specific profile from your credential file.')
    
    args = parser.parse_args()
    bucket_name = args.bucket
    profile = args.profile

    main()
