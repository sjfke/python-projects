import argparse
import base64
import json
import os
import sys

""" Useful references
# Python Library: https://docs.python.org/dev/library/argparse.html
# Tutorial: https://docs.python.org/dev/howto/argparse.html
# Search Python Standard Library: https://docs.python.org/3/library/index.html
# Base64 to Image: https://base64.guru/converter/decode/image
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='JSON {"type": "<image-type>", "data":<base64>} to an image',
        epilog="That's all Folks! ... Porky Pig",
    )
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument(
        "infile", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    parser.add_argument("outfile", nargs="?", type=argparse.FileType("wb"))

    args = parser.parse_args()

    if args.verbose >= 1:
        print(f"args: {args.__str__()}")

    try:
        json_dict = json.load(args.infile)

        image_code = base64.b64decode(json_dict['data'])
        if args.outfile is None:
            _name = os.path.splitext(args.infile.name)[0]
            _filename = f"{_name}.{json_dict['type']}"

            sys.stderr.write(f"writing '{_filename}'")
            with open(_filename, 'wb') as f:
                f.write(image_code)

        else:
            args.outfile.write(image_code)
            args.outfile.flush()
            args.outfile.close()

        args.infile.close()
        sys.exit(0)
    except Exception as error:
        print(f"{error}")
        sys.exit(1)
