import boto3
import argparse

parser = argparse.ArgumentParser(prog=__file__)
parser._action_groups.pop() # Edited this line
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument('--role-name',required=True,help='The name of the role to delete.') 
optional.add_argument('--profile',nargs='?',default='default',help='Use a specific profile from your credential file.') 

args = parser.parse_args()
profile = args.profile
role_name = args.role_name

session = boto3.Session(profile_name=profile)
iam = session.resource('iam')

role = iam.Role(role_name)

policies = list(role.attached_policies.all())
for policy in policies:
    policy.detach_role(RoleName=role_name)

instance_profiles = list(role.instance_profiles.all())
for instance_profile in instance_profiles:
    instance_profile.remove_role(RoleName=role_name)
    instance_profile.delete()

role.delete()
