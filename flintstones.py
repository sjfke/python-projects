import argparse
import sys

# https://docs.python.org/3/howto/argparse.html
_dict = {'Fred': 30, 'Wilma': 25, 'Pebbles': 1, 'Dino': 5}


def get_names() -> list[str]:
    """
    Get Flintstones family firstnames
    :return: list of names
    """
    return list(_dict.keys())


def get_ages() -> list[int]:
    """
    Get Flintstones family ages
    :return: list of ages
    """
    return list(_dict.values())


def get_person(name: str = None) -> (dict[str,int] | None):
    """
    Get age of Flintstones family member
    :param name: firstname
    :return: integer age or None
    """
    if name is not None:

        try:
            _ans = {name: _dict[name]}
            return _ans
        except KeyError:
            print(f"KeyError: {name} not found", file=sys.stderr)
            # print("KeyError: {0} not found".format(name))  # prior to Python 3.6
            return None
    else:
        return None


if __name__ == '__main__':
    arguments = None
    parser = argparse.ArgumentParser(description='Simple Command Line Application')
    parser.add_argument('-n', '--names', action='store_true', default=False, help='display names')
    parser.add_argument('-a', '--ages', action='store_true', default=False, help='display ages')
    parser.add_argument('-p', '--person', type=str, default=None, help='display person age')
    parser.add_argument('-v', '--verbose', action='count', default=0)

    args = parser.parse_args()

    if args.verbose >= 1:
        print(f"args: {args.__str__()}")

    if args.names:
        print(f"{get_names()}")
    elif args.ages:
        print(f"{get_ages()}")
    elif args.person:
        print(f"{get_person(name=args.person)}")
    else:
        parser.print_help()

    sys.exit(0)
