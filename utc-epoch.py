import argparse
import sys
import time
import pytz
from datetime import datetime
from pytz import timezone
from tzlocal import get_localzone


# https://www.tutorialspoint.com/How-to-convert-date-and-time-with-different-timezones-in-Python
# https://www.tutorialspoint.com/How-do-I-print-a-Python-datetime-in-the-local-timezone
# https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones
# https://gist.github.com/mjrulesamrat/0c1f7de951d3c508fb3a20b4b0b33a98 # time-zone list
# https://stackoverflow.com/questions/7065164/how-to-make-a-datetime-object-aware-not-naive-in-python


def get_datetime(epoch):
    """
    Return DateTime string in UTC or local timezone (e.g. 2023-04-26 12:47:10 UTC+0000)
    :param epoch: UNIX epoch to convert
    :type epoch: int
    :return: DateTime
    :rtype: str
    """

    _format = "%Y-%m-%d %H:%M:%S %Z%z"

    if args.local_time:
        return datetime.fromtimestamp(epoch).replace(tzinfo=pytz.UTC).astimezone(get_localzone()).strftime(_format)
    else:
        return datetime.fromtimestamp(epoch).replace(tzinfo=pytz.UTC).strftime(_format)


def get_epoch(local_time):
    """
    Return current datetime as UNIX epoch in UTC or local timezone
    :param local_time: use local time-zone not UTC
    :type local_time: bool
    :return: UNIX epoch
    :rtype: int
    """
    if local_time:
        return int(time.mktime(datetime.now(get_localzone()).timetuple()))
    else:
        return int(time.mktime(datetime.now(timezone('UTC')).timetuple()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display UNIX epoch')
    parser.add_argument('-e', '--epoch', type=int, default=None, help='epoch to display as date string')
    parser.add_argument('-l', '--local-time', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()

    if args.verbose:
        print("args: {0}".format(args.__str__()))

    if args.epoch:
        print(get_datetime(args.epoch))
    else:
        print(get_epoch(args.local_time))

    sys.exit(0)
