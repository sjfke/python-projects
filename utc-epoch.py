import argparse
import sys
import time
from datetime import datetime, timezone

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display UNIX epoch')
    parser.add_argument('-e', '--epoch', type=int, default=None, help='epoch to display as date string')
    parser.add_argument('-v', '--verbose', action='count', default=0)

    args = parser.parse_args()

    if args.verbose >= 1:
        print("args: {0}".format(args.__str__()))

    if args.epoch:
        print(datetime.fromtimestamp(args.epoch).strftime('%c'))
    else:
        print(int(time.mktime(datetime.now(timezone.utc).timetuple())))

    sys.exit(0)
