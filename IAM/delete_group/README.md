# delete_group
グループを削除する際にはポリシーをデタッチしたりユーザをリムーブしたりいろいろしなければいけないですがこのスクリプトはそれらを解決します。  
いろいろデタッチしたりしてからグループを削除してくれます。


```
usage: ./delete_group.py [-h] --group-name GROUP_NAME [--profile [PROFILE]]

required arguments:
  --group-name GROUP_NAME  The name of the IAM group to delete.

optional arguments:
  --profile [PROFILE]      Use a specific profile from your credential file.
```