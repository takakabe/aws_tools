# delete_role
ロールを削除する際にはポリシーをデタッチしたりインスタンスプロファイルをリムーブしたりいろいろしなければいけないですがこのスクリプトはそれらを解決します。  
いろいろデタッチしたりしてからロールを自動で削除してくれます。  


```
usage: ./delete_role.py [-h] [--profile [PROFILE]] --role-name ROLE_NAME

required arguments:  
  --role-name ROLE_NAME The name of the role to delete.

optional arguments:  
  --profile [PROFILE]   Use a specific profile from your credential file.
  ```