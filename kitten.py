import argparse
import sys


def display_contents(lines, line_numbers=False, first_line=0, last_line=0, verbose=0):
    """ Display file contents line by line
    :param lines: file content as a List
    :param line_numbers: prefix line with line count
    :param first_line: first line to display
    :param last_line: last line to display
    :param verbose: messages
    """

    line_count = 0

    for line in lines:
        line_count += 1
        if (first_line > 0) and (last_line > 0):
            if (line_count >= first_line) and (line_count <= last_line):
                if line_numbers:
                    print("{:03d}: {}".format(line_count, line.rstrip()))  # remove newline '\n'
                else:
                    print("{}".format(line.rstrip()))  # remove newline '\n'
        elif (first_line > 0) and (line_count >= first_line):
            if line_numbers:
                print("{:03d}: {}".format(line_count, line.rstrip()))  # remove newline '\n'
            else:
                print("{}".format(line.rstrip()))  # remove newline '\n'
        elif (last_line > 0) and (line_count <= last_line):
            if line_numbers:
                print("{:03d}: {}".format(line_count, line.rstrip()))  # remove newline '\n'
            else:
                print("{}".format(line.rstrip()))  # remove newline '\n'
        else:
            if line_numbers:
                print("{:03d}: {}".format(line_count, line.rstrip()))  # remove newline '\n'
            else:
                print("{}".format(line.rstrip()))  # remove newline '\n'

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    arguments = None
    parser = argparse.ArgumentParser(description='Simple version on UNIX cat application')
    parser.add_argument('-n', '--number', action='store_true', default=False, help='display line numbers')
    parser.add_argument('-f', '--first', type=int, default=0, help='first line to display')
    parser.add_argument('-l', '--last', type=int, default=0, help='last line to display')
    parser.add_argument('-r', '--reverse', action='store_true', default=False, help='reverse contents')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('filename', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

    args = parser.parse_args()

    if args.verbose > 1:
        print("args: {0}".format(args.__str__()))

    # Note equivalent of: filename = open('filename.txt', 'r')
    # Done by: add_argument('filename', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    try:
        contents = args.filename.readlines()
        if args.reverse:
            contents.reverse()

        if args.verbose >= 1:
            print("filename: {0}".format(args.infd.name))
            print("contents: {0}".format(contents))

        display_contents(lines=contents, line_numbers=args.number, first_line=args.first, last_line=args.last,
                         verbose=args.verbose)
        sys.exit(0)
    except FileNotFoundError as file_not_found_error:
        print("{0}".format(file_not_found_error))
        sys.exit(1)
    except Exception as error:
        print('{0}'.format(error))
        sys.exit(1)
