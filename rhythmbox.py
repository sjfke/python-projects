import argparse
import sys

import xmltodict


def list_entries(entries: object, TYPE_TO_MATCH: str = 'ignore', yaml_format=False, verbose=0):
    """ List Internet Radio entries
    :type entries: object - list of entries
    :param TYPE_TO_MATCH: entry type to match ('iradio', 'song', 'ignore')
    :param yaml_format - YAML rather than JSON
    :param verbose: messages
    """

    line_count: int = 0

    try:
        for entry in entries:
            if entry['@type'] == TYPE_TO_MATCH:
                line_count += 1
                if verbose > 0:
                    if TYPE_TO_MATCH == 'ignore':
                        location_entry = {'@type': entry['@type'], 'location': entry['location']}
                        print("{:03d}: {}".format(line_count, location_entry))
                    else:
                        print("{:03d}: {}".format(line_count, entry))

        if verbose == 0:
            print("{1:6s}: {0:03d}".format(line_count, TYPE_TO_MATCH))

    except KeyError as entry_key_error:
        print("Missing key {0}, in, '{1}'".format(entry_key_error, args.infd.name))

    return None


def list_all_entries(entries: object, KNOWN_ENTRIES=('iradio', 'song', 'ignore'), known_type=False, verbose=0):
    """ List Internet Radio entries
    :type entries: object - list of entries
    :param KNOWN_ENTRIES: known entry types ('iradio', 'song', 'ignore')
    :param known_type: entry type in TYPE_TO_MATCH
    :param verbose: messages
    """

    line_count: int = 0

    try:
        for entry in entries:
            if known_type and entry['@type'] in KNOWN_ENTRIES:
                line_count += 1
                if verbose > 0:
                    print("{:03d}: {}".format(line_count, entry))
            elif entry['@type'] not in KNOWN_ENTRIES:
                line_count += 1
                if verbose > 0:
                    print("{:03d}: {}".format(line_count, entry))

        if verbose == 0:
            if known_type and entry['@type'] in KNOWN_ENTRIES:
                print("{1:6s}: {0:03d}".format(line_count, 'known'))
            else:
                print("{1:6s}: {0:03d}".format(line_count, 'unknown'))

    except KeyError as entry_key_error:
        print("Missing key {0}, in, '{1}'".format(entry_key_error, args.infd.name))

    return None

# ==============================================================================
# Python Library: https://docs.python.org/dev/library/argparse.html
# Nargs usage: https://docs.python.org/dev/library/argparse.html#nargs
# Tutorial: https://docs.python.org/dev/howto/argparse.html
# PEP 8 – Style Guide for Python Code: https://peps.python.org/pep-0008/
# PyFormat Using % and .format() for great good!: https://pyformat.info/
# Search Python Standard Library: https://docs.python.org/3/library/index.html
# Python Basics: https://docs.python-guide.org/scenarios/xml/
# The ElementTree XML API: https://docs.python.org/3/library/xml.etree.elementtree.html
# Dictionary into a valid XML string: https://pypi.org/project/dicttoxml/
# Logging Best Practices: https://www.loggly.com/use-cases/6-python-logging-best-practices-you-should-be-aware-of/
# ==============================================================================

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    arguments = None
    parser = argparse.ArgumentParser(description='Simple RhythmBox XML File Parser')
    parser.add_argument('-r', '--radio', action='store_true', help='extract radio entries')
    parser.add_argument('-s', '--song', action='store_true', help='extract song entries')
    parser.add_argument('-i', '--ignore', action='store_true', help='extract ignore entries')
    parser.add_argument('-u', '--unknown', action='store_true', help='extract unknown entries')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('infd', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    # parser.add_argument('outfd', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

    args = parser.parse_args()

    if args.verbose >= 1:
        print("args: {0}".format(args.__str__()))

    # Note equivalent of: infd = open('filename.txt', 'r')
    # Done by: add_argument('infd', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    try:
        data = xmltodict.parse(args.infd.read())
        entries = data['rhythmdb']['entry']
        known_entries = ('iradio', 'song', 'ignore')

        if args.radio:
            list_entries(entries=entries, TYPE_TO_MATCH='iradio', yaml_format=False, verbose=args.verbose)
        elif args.song:
            list_entries(entries=entries, TYPE_TO_MATCH='song', yaml_format=False, verbose=args.verbose)
        elif args.ignore:
            list_entries(entries=entries, TYPE_TO_MATCH='ignore', yaml_format=True, verbose=args.verbose)
        elif args.unknown:
            list_all_entries(entries=entries, KNOWN_ENTRIES=known_entries, known_type=False, verbose=args.verbose)
        else:
            list_all_entries(entries=entries, KNOWN_ENTRIES=known_entries, known_type=True, verbose=args.verbose)

        sys.exit(0)

    except FileNotFoundError as file_not_found_error:
        print("{0}".format(file_not_found_error))
        sys.exit(1)
    except Exception as error:
        print('{0}'.format(error))
        sys.exit(1)
