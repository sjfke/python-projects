import argparse
import sys

# https://docs.python.org/3/howto/argparse.html

_dict = {'Fred': 30, 'Wilma': 25, 'Pebbles': 1, 'Dino': 5}


def get_names():
    """
    Get person names

    :rtype: List
    :return: person names
    """
    return _dict.keys()


def get_ages():
    """
    Get ages

    :rtype: List
    :return: person ages
    """

    return _dict.values()


def get_person(name=None):
    """
    Get age of person

    :param name: of the person
    :type name: str

    :rtype: str
    :return: firstnames or None
    """

    if name is not None:

        try:
            _ans = {name: _dict[name]}
            return _ans
        except KeyError:
            return f"KeyError: {name}"
            # return "KeyError: {0}".format(name)  # prior to Python 3.6
    else:
        return None


if __name__ == '__main__':
    arguments = None
    parser = argparse.ArgumentParser(description='Simple Command Line Application')
    parser.add_argument('-n', '--names', action='store_true', default=False, help='display names')
    parser.add_argument('-a', '--ages', action='store_true', default=False, help='display ages')
    parser.add_argument('-p', '--person', type=str, default=None, help='person to display')
    parser.add_argument('-v', '--verbose', action='count', default=0)

    args = parser.parse_args()

    if args.verbose >= 1:
        print("args: {0}".format(args.__str__()))

    if args.names:
        print("{0}".format(get_names()))
    elif args.ages:
        print("{0}".format(get_ages()))
    elif args.person:
        print("{0}".format(get_person(name=args.person)))

    sys.exit(0)
