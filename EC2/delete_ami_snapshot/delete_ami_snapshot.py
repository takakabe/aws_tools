import boto3, argparse

class ami():
    def __init__(self, image_id, profile='default'):
        self.session = boto3.Session(profile_name=profile)
        self.ec2 = self.session.resource('ec2')
        self.image = self.ec2.Image(image_id)
        self.block_device_mappings = list(self.image.block_device_mappings)


    def delete(self):
        self.deregister_image(image_id)
        for self.block_device_mapping in self.block_device_mappings:
            self.snapshot_id = self.block_device_mapping['Ebs']['SnapshotId']
            self.delete_snapshot(self.snapshot_id)

    def deregister_image(self, image_id):
        self.image.deregister()
    
    def delete_snapshot(self, snapshot_id):
        self.ec2.Snapshot(self.snapshot_id).delete()


def main():
    ami(image_id).delete()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=__file__)
    required = parser.add_argument_group('required arguments')
    required.add_argument('--image_id',required=True, help='AMI image ID.')
    parser.add_argument('--profile',nargs='?',default='default',help='Use a specific profile from your credential file.')
    
    args = parser.parse_args()
    profile = args.profile
    image_id = args.image_id

    main()
