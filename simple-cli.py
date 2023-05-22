
import argparse
import sys

""" Useful references
# Python Library: https://docs.python.org/dev/library/argparse.html
# Nargs usage: https://docs.python.org/dev/library/argparse.html#nargs
# Tutorial: https://docs.python.org/dev/howto/argparse.html
# PEP 8 – Style Guide for Python Code: https://peps.python.org/pep-0008/
# PyFormat Using % and .format() for great good!: https://pyformat.info/
# Search Python Standard Library: https://docs.python.org/3/library/index.html
# Logging Best Practices: https://www.loggly.com/use-cases/6-python-logging-best-practices-you-should-be-aware-of/
"""

if __name__ == '__main__':

    arguments = None
    parser = argparse.ArgumentParser(
        description='Simple UNIX CLI like example',
        epilog="That's all Folks! ... Porky Pig")
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

    args = parser.parse_args()

    if args.verbose >= 1:
        print(f"args: {args.__str__()}")

    try:
        count = 0
        lines = args.infile.readlines()

        for line in lines:
            count += 1
            args.outfile.write(f"{count:03d}: {line}")

        args.outfile.flush()
        args.outfile.close()
        args.infile.close()
        sys.exit(0)
    except Exception as error:
        print(f"{error}")
        sys.exit(1)
