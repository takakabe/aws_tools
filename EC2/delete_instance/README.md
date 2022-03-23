# delete_instance
Delete AMI and snapshot.

## usage
```
$ python3 ./delete_instance.py -h
usage: ./delete_instance.py [-h] [--profile [PROFILE]] --instance_id [INSTANCE_ID] [--force]

optional arguments:
  -h, --help            show this help message and exit
  --profile [PROFILE]   Use a specific profile from your credential file.
  --instance_id [INSTANCE_ID]
                        Set the instance ID to delete.
  --force               Forced termination even if it is termination protection.
```