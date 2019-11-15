# get_bucket_size
Get the size of the S3 bucket.  
Get the value from CloudWatchMetrics.  

## usage
```
usage: 'get_bucket_size.py [-h] --bucket BUCKET [--profile [PROFILE]]

optional arguments:
  -h, --help           show this help message and exit

required arguments:
  --bucket BUCKET      The name of the bucket name.

optional arguments:
  --profile [PROFILE]  Use a specific profile from your credential file.
```

## demo

```
$ python ./get_bucket_size.py --bucket mybucket
6487.0 Bytes
```