# tree_group_policy
ツリー形式でグループにアタッチされているポリシーを表示してくれます。  

```
usage: ./tree_group_policy.py [-h] --group-name GROUP_NAME [--profile [PROFILE]]

required arguments:
  --group-name GROUP_NAME  The name of the IAM group to delete.

optional arguments:
  --profile [PROFILE]   Use a specific profile from your credential file.
```

実行してみるとこんなかんじ。  
```
$ ./python tree_group_policy.py --group-name test_group
test_group
├─ AWSElasticBeanstalkEnhancedHealth
├─ AWSElasticBeanstalkMulticontainerDocker
├─ AWSElasticBeanstalkService
├─ AdministratorAccess
└─ AmazonRDSEnhancedMonitoringRole
```
