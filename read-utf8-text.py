import argparse
import sys

__author__ = "Sjfke"
__copyright__ = "Copyleft"


def display_lines(lines, line_numbers=False):
    line_count = 0

    for line in lines:
        line_count += 1
        if line_numbers:
            print(f"{line_count:03d}: {line.rstrip()}")  # remove newline '\n'
        else:
            print(f"{line.rstrip()}")  # remove newline '\n'

    return None


""" Useful references
# Python Library: https://docs.python.org/dev/library/argparse.html
# Nargs usage: https://docs.python.org/dev/library/argparse.html#nargs
# Tutorial: https://docs.python.org/dev/howto/argparse.html
# PEP 8 – Style Guide for Python Code: https://peps.python.org/pep-0008/
# PyFormat Using % and .format() for great good!: https://pyformat.info/
# Search Python Standard Library: https://docs.python.org/3/library/index.html
# Logging Best Practices: https://www.loggly.com/use-cases/6-python-logging-best-practices-you-should-be-aware-of/
"""


# python .\read-utf8-text.py -rv .\examples\european-words.txt
# python .\read-utf8-text.py -n .\examples\european-words.txt
# python .\read-utf8-text.py -v .\examples\european-words.txt

def main(args=None) -> None:
    arguments = None
    parser = argparse.ArgumentParser(description='Display the contents of a UTF-8 text file')
    parser.add_argument('-n', '--number', action='store_true', default=False, help='display line numbers')
    parser.add_argument('-r', '--raw', action='store_true', default=False, help='raw contents')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    # Forcing UTF-8 encoding, to avoid unpredictable results with international characters
    parser.add_argument('filename', nargs='?', type=argparse.FileType('r', encoding='utf-8'), default=sys.stdin)

    args = parser.parse_args()

    if args.verbose > 1:
        print(f"args: {args.__str__()}")

    # Note equivalent of: filename = open('filename.txt', 'r')
    # Done by: add_argument('filename', nargs='?', type=argparse.FileType('r', encoding='utf-8'), default=sys.stdin)
    try:
        contents = args.filename.readlines()
        if args.raw:
            print(f"contents: {contents}")
        else:
            if args.verbose >= 1:
                print(f"filename: {args.filename}")

            display_lines(lines=contents, line_numbers=args.number)

        sys.exit(0)

    except FileNotFoundError as file_not_found_error:
        print(f"{file_not_found_error}")
        sys.exit(1)
    except Exception as error:
        print(f"{error}")
        sys.exit(1)


if __name__ == '__main__':
    main()
