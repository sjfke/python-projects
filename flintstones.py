import argparse
import sys

_dict = {'Fred': 30, 'Wilma': 25, 'Pebbles': 1, 'Dino': 5}


def get_names():
    return _dict.keys()


def get_ages():
    return _dict.values


def get_person(name=None):
    if name is not None:
        return "{0}: {1}".format(name, _dict[name])


if __name__ == '__main__':
    arguments = None
    parser = argparse.ArgumentParser(description='Simple version on UNIX cat application')
    parser.add_argument('-n', '--names', action='store_true', default=False, help='display names')
    parser.add_argument('-a', '--ages', action='store_true', default=False, help='display ages')
    parser.add_argument('-p', '--person', type=str, default=None, help='person to display')
    parser.add_argument('-v', '--verbose', action='count', default=0)

    args = parser.parse_args()

    sys.exit(0)
