# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import argparse
    import sys
    import xmltodict

    arguments = None
    parser = argparse.ArgumentParser(description='Simple RhythmBox Parser')
    # parser.add_argument('-r', '--readfile', type=argparse.FileType('r'), default='-')
    # parser.add_argument('-w', '--writefile', type=argparse.FileType('w'), default='-')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    # https://docs.python.org/dev/library/argparse.html#nargs
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    # parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

    args = parser.parse_args()

    if args.verbose >= 1:
        print("args: {0}".format(args.__str__()))

    try:

        data = xmltodict.parse(args.infile.read())
        print(data)
        sys.exit(0)

    except FileNotFoundError as e:
        print("{0}".format(e))
        sys.exit(1)
