import argparse
import sys
import xmltodict
import logging


def list_radio_entry(data_dict, yaml_format=False, verbose=0):
    """ List Internet Radio entries
    :param data_dict - XML file as dictionary
    :param yaml_format - YAML rather than JSON
    :param verbose: messages
    """

    count = 0

    try:
        for entry in data_dict['rhythmdb']['entry']:
            if entry['@type'] == 'iradio':
                count += 1
                print("{:03d}: {}".format(count, entry))
    except KeyError as entry_key_error:
        print("Missing key {0}, in, '{1}'".format(entry_key_error, args.infd.name))

    return None

    logging.critical("{0}: not yet implemented".format('list_radio_entry'))
    return None


def list_song_entry(data_dict, yaml_format=False, verbose=0):
    """ List song entries
    :param data_dict - XML file as dictionary
    :param yaml_format - YAML rather than JSON
    :param verbose: messages
    """

    count = 0

    try:
        for entry in data_dict['rhythmdb']['entry']:
            if entry['@type'] == 'song':
                count += 1
                print("{:03d}: {}".format(count, entry))
    except KeyError as entry_key_error:
        print("Missing key {0}, in, '{1}'".format(entry_key_error, args.infd.name))

    return None

    logging.critical("{0}: not yet implemented".format('list_song_entry'))
    return None


def list_ignore_entry(data_dict, yaml_format=False, verbose=0):
    """ List ignore entries
    :param data_dict - XML file as dictionary
    :param yaml_format - YAML rather than JSON
    :param verbose: messages
    """

    count = 0

    try:
        for entry in data_dict['rhythmdb']['entry']:
            if entry['@type'] == 'ignore':
                count += 1
                print("{:03d}: {}".format(count, entry))
    except KeyError as entry_key_error:
        print("Missing key {0}, in, '{1}'".format(entry_key_error, args.infd.name))

    return None

    logging.critical("{0}: not yet implemented".format('list_ignore_entry'))
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
# Logging Best Practices: https://www.loggly.com/use-cases/6-python-logging-best-practices-you-should-be-aware-of/
# ==============================================================================

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    arguments = None
    parser = argparse.ArgumentParser(description='Simple RhythmBox Parser')
    parser.add_argument('-r', '--radio', action='store_true', help='extract radio entries')
    parser.add_argument('-s', '--song', action='store_true', help='extract song entries')
    parser.add_argument('-i', '--ignore', action='store_true', help='extract ignore entries')
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

        if args.radio:
            list_radio_entry(data_dict=data, yaml_format=False, verbose=0)
        elif args.song:
            list_song_entry(data_dict=data, yaml_format=False, verbose=0)
        elif args.ignore:
            list_ignore_entry(data_dict=data, yaml_format=False, verbose=0)
        else:
            known_entries = ('iradio', 'song', 'ignore')
            count = 0
            for entry in data['rhythmdb']['entry']:
                if entry['@type'] not in known_entries:
                    count += 1
                    print("{:03d}: {}".format(count, entry))
            # print(data)

        sys.exit(0)

    except FileNotFoundError as file_not_found_error:
        print("{0}".format(file_not_found_error))
        sys.exit(1)
    except Exception as error:
        print('{0}'.format(error))
        sys.exit(1)
