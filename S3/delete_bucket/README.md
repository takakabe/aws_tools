# delete_bucket
Delete the bucket. It is not necessary to delete all objects in the bucket (including all object versions and delete markers) before deleting the bucket itself.  

## usage
```
$ python ./delete_bucket.py --help
usage: .\delete_bucket.py [-h] --bucket BUCKET [--profile [PROFILE]]

optional arguments:
  -h, --help           show this help message and exit

required arguments:
  --bucket BUCKET      The name of the bucket name.

optional arguments:
  --profile [PROFILE]  Use a specific profile from your credential file.
```

## demo
```
$ python delete_bucket.py mybucket
```