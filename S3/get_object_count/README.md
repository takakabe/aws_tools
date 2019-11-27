# get_bucket_size
Count object of the S3 bucket.
Value from CloudWatchMetrics.  

## usage
```
$ python get_object_count.py --help
usage: get_object_count.py [-h] --bucket BUCKET [--profile [PROFILE]]

optional arguments:
  -h, --help           show this help message and exit
  --profile [PROFILE]  Use a specific profile from your credential file.

required arguments:
  --bucket BUCKET      The name of the bucket name.
  ```

## demo

```
$ python ./get_object_count.py --bucket mybucket
12 Count
```
