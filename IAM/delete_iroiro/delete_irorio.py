import boto3, argparse

class iam():
    def __init__(self):
        self.session = boto3.Session(profile_name=args.profile)
        self.iam = self.session.resource('iam')

    def detach_all_policies(self):  # iam_resource is group or role
        policies = list(self.iam_resource.attached_policies.all())
        for policy in policies:
            self.iam_resource.detach_policy(PolicyArn=policy.arn)

    def delete(self):
        self.iam_resource.delete()


class group(iam):
    def __init__(self):
        super().__init__()
        self.iam_resource = self.iam.Group(args.group_name)

    def remove_all_users(self):
        users = list(self.iam_resource.users.all())
        for user in users:
            self.iam_resource.remove_user(UserName=user.name)

    def delete(self):
        self.detach_all_policies()
        self.remove_all_users()
        super().delete()


class role(iam):
    def __init__(self):
        super().__init__()
        self.iam_resource = self.iam.Role(args.role_name)

    def delete_instance_profiles(self):
        instance_profiles = list(self.iam_resource.instance_profiles.all())
        for instance_profile in instance_profiles:
            instance_profile.remove_role(RoleName=args.role_name)
            instance_profile.delete()

    def delete(self):
        self.detach_all_policies()
        self.delete_instance_profiles()
        super().delete()


def main():
    if args.group_name:
        group().delete()
    else:
        role().delete()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=__file__)
    parser._action_groups.pop()

    mutual = parser.add_mutually_exclusive_group(required=True)
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    mutual.add_argument('--group-name',help='The name of the IAM group to delete.')
    mutual.add_argument('--role-name',help='The name of the role to delete.')
    optional.add_argument('--profile',nargs='?',default='default',help='Use a specific profile from your credential file.')

    args = parser.parse_args()
    main()
