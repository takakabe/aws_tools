# get_monthly_cost
Get AWS Monthly Cost

## usage
### Command line
```
python get_monthly_cost.py --help
usage: get_monthly_cost.py [-h] [--profile [PROFILE]] [--year [YEAR]]
                           [--month [MONTH]]

optional arguments:
  -h, --help           show this help message and exit
  --profile [PROFILE]  Use a specific profile from your credential file.
  --year [YEAR]        Sets the year for retrieving AWS costs.
  --month [MONTH]      Sets the month for retrieving AWS costs.
```
```
$ python get_monthly_cost.py
9.4029780888 USD
$ python get_monthly_cost.py --year 2020 --month 1
10.2359175577 USD
```

### Programming
```python
import get_monthly_cost
response = get_monthly_cost.cost().get()
# ('9.4029780888', 'USD')
```
```python
import get_monthly_cost
response = get_monthly_cost.cost(2020,1).get()
# ('10.2359175577', 'USD')
```



