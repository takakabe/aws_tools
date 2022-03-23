import argparse
import boto3

class ec2_instance():
    def __init__(self, instance_id=None, force_flag=None, profile='default'):
        self.session = boto3.Session(profile_name=profile)
        self.ec2 = self.session.resource('ec2')
        self.instance = self.ec2.Instance(instance_id)

    def delete(self):
        if force_flag:
            self.instance.modify_attribute(DisableApiTermination={'Value': False})
        return(self.instance.terminate())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=__file__)
    parser.add_argument('--profile',nargs='?',default='default',help='Use a specific profile from your credential file.')
    parser.add_argument('--instance_id',nargs='?',required=True,help='Set the instance ID to delete.')
    parser.add_argument('--force',action='store_true',help='Forced termination even if it is termination protection.')
    
    args = parser.parse_args()
    profile = args.profile
    instance_id = args.instance_id
    force_flag = args.force

    result = ec2_instance(instance_id,force_flag,profile,).delete()
    print(result['TerminatingInstances'][0]['CurrentState']['Name'])
