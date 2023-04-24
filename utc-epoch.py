import argparse
import sys
import time
from datetime import datetime, timezone


def get_datetime(epoch):
    """
    Return DateTime string in UTC or local timezone (e.g. Sat Apr 15 12:14:46 2023)
    :param epoch: UNIX epoch to convert
    :type epoch: int
    :return: DateTime
    :rtype: str
    """
    if args.local_time:
        return datetime.fromtimestamp(epoch).strftime('%c')
    else:
        return datetime.utcfromtimestamp(epoch).strftime('%c')


def get_epoch(local_time):
    """
    Return current datetime as UNIX epoch in UTC or local timezone
    :param local_time: use local time-zone not UTC
    :type local_time: bool
    :return: UNIX epoch
    :rtype: int
    """
    if local_time:
        return int(time.mktime(datetime.now().timetuple()))
    else:
        return int(time.mktime(datetime.now(timezone.utc).timetuple()))


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
