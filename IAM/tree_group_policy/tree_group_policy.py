import boto3
import argparse

parser = argparse.ArgumentParser(prog=__file__)
parser._action_groups.pop() # Edited this line
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument('--group-name',required=True,help='The name of the IAM group to delete.') 
optional.add_argument('--profile',nargs='?',default='default',help='Use a specific profile from your credential file.') 

args = parser.parse_args()
profile = args.profile
group_name = args.group_name

session = boto3.Session(profile_name=profile)
iam = session.resource('iam')
group = iam.Group(group_name)

policies = list(group.attached_policies.all())
policies_list = [ policy.policy_name for policy in policies ]
policies_list.sort()

print(group_name)
for policy_name in policies_list:
    if policy_name == policies_list[-1]:
        print('└─ '+policy_name+'\n')
    else:
        print('├─ '+policy_name)
