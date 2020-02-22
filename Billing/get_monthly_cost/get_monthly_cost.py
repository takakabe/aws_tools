import argparse
import boto3
import calendar
import datetime

class cost():
    def __init__(self, year=None, month=None, profile='default'):
        self.session = boto3.Session(profile_name=profile)
        self.ce = self.session.client('ce')
        self.year = datetime.date.today().year if year is None else int(year)
        self.month = datetime.date.today().month if month is None else int(month)

    def get(self):
        self.month_last_day = calendar.monthrange(self.year, self.month)[1]
        self.start_time = datetime.date(self.year, self.month, 1).strftime('%Y-%m-%d')
        self.end_time = datetime.date(self.year, self.month, self.month_last_day).strftime('%Y-%m-%d')

        self.cost = self.ce.get_cost_and_usage(
            TimePeriod={
                'Start': self.start_time,
                'End': self.end_time
            },
            Granularity='MONTHLY',
            Metrics=['BlendedCost'],
        )['ResultsByTime'][0]['Total']['BlendedCost']['Amount']

        return(self.cost, 'USD')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=__file__)
    parser.add_argument('--profile',nargs='?',default='default',help='Use a specific profile from your credential file.')
    parser.add_argument('--year',nargs='?',help='Sets the year for retrieving AWS costs.')
    parser.add_argument('--month',nargs='?',help='Sets the month for retrieving AWS costs.')
    
    args = parser.parse_args()
    profile = args.profile
    year = args.year
    month = args.month

    print(*cost(year, month, profile).get())
