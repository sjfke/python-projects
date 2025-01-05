import argparse
import sys
import time
import pytz
from tzlocal import get_localzone

_datetime_iana_support = False
if sys.version_info.major >= 3 and sys.version_info.minor >= 9:
    from zoneinfo import ZoneInfo
    from datetime import datetime, timezone
    _datetime_iana_support = True
else:
    from datetime import datetime
    from pytz import timezone


# https://www.tutorialspoint.com/How-to-convert-date-and-time-with-different-timezones-in-Python
# https://www.tutorialspoint.com/How-do-I-print-a-Python-datetime-in-the-local-timezone
# https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones
# https://gist.github.com/mjrulesamrat/0c1f7de951d3c508fb3a20b4b0b33a98 # time-zone list
# https://stackoverflow.com/questions/7065164/how-to-make-a-datetime-object-aware-not-naive-in-python


def get_datetime(epoch, local_time=False, date_format="%Y-%m-%d %H:%M:%S %Z%z"):
    """
    Return DateTime string in UTC or local timezone (e.g. 2023-04-26 12:47:10 UTC+0000)
    :param epoch: UNIX epoch to convert
    :type epoch: int
    :param local_time: use local timezone, not UTC the default
    :type: local_time: Boolean
    :param date_format: date formatting (default "%Y-%m-%d %H:%M:%S %Z%z")
    :type date_format: str
    :return: DateTime
    :rtype: str
    """

    if local_time:
        if _datetime_iana_support:
            return str(datetime.fromtimestamp(epoch).replace(tzinfo=timezone.utc).astimezone(get_localzone()).strftime(date_format))
        else:
            return str(datetime.fromtimestamp(epoch).replace(tzinfo=pytz.UTC).astimezone(get_localzone()).strftime(
                date_format))
    else:
        if _datetime_iana_support:
            return str(datetime.fromtimestamp(epoch).replace(tzinfo=timezone.utc).strftime(date_format))
        else:
            return str(datetime.fromtimestamp(epoch).replace(tzinfo=pytz.UTC).strftime(date_format))


def get_epoch(local_time):
    """
    Return current datetime as UNIX epoch in UTC or local timezone
    :param local_time: use local time-zone not UTC
    :type local_time: bool
    :return: UNIX epoch
    :rtype: int
    """
    if _datetime_iana_support:
        if local_time:
            return int(time.mktime(datetime.now().timetuple()))
        else:
            return int(time.mktime(datetime.now(timezone.utc).timetuple()))
    else:
        if local_time:
            return int(time.mktime(datetime.now(get_localzone()).timetuple()))
        else:
            return int(time.mktime(datetime.now(timezone('UTC')).timetuple()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display UNIX epoch')
    parser.add_argument('-e', '--epoch', type=int, default=None, help='epoch to display as date string')
    parser.add_argument('-i', '--iso8601', action='store_true', help='ISO-8601 date format')
    parser.add_argument('-l', '--local-time', action='store_true', help='use local time-zone')
    parser.add_argument('-v', '--verbose', action='count', default=0)

    args = parser.parse_args()

    if args.verbose > 1:
        print("args: {0}".format(args.__str__()))

    if args.epoch:
        if args.iso8601:
            if args.local_time:
                _datetime = get_datetime(epoch=args.epoch, local_time=True, date_format="%Y-%m-%dT%H:%M:%S%z")
            else:
                _datetime = get_datetime(epoch=args.epoch, date_format="%Y-%m-%dT%H:%M:%S%z")
        else:
            if args.local_time:
                _datetime = get_datetime(epoch=args.epoch, local_time=True)
            else:
                _datetime = get_datetime(epoch=args.epoch)

        if args.verbose == 1:
            print(f"{_datetime} / {args.epoch}")
        else:
            print(f"{_datetime}")
    else:
        if args.verbose >= 1:
            _epoch = get_epoch(local_time=args.local_time)
            if args.iso8601:
                _datetime = get_datetime(epoch=_epoch, local_time=args.local_time, date_format="%Y-%m-%dT%H:%M:%S%z")
            else:
                _datetime = get_datetime(epoch=_epoch, local_time=args.local_time)

            print(f"{_epoch} / {_datetime}")
        else:
            print(get_epoch(local_time=args.local_time))

    sys.exit(0)
