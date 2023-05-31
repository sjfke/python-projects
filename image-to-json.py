import argparse
import base64
import json
import sys

import filetype

""" Useful references
# Python Library: https://docs.python.org/dev/library/argparse.html
# Tutorial: https://docs.python.org/dev/howto/argparse.html
# Search Python Standard Library: https://docs.python.org/3/library/index.html
# Base64 to Image: https://base64.guru/converter/decode/image
"""

# https://pypi.org/project/filetype/#supported-types
IMAGE_FORMATS = {
    "dwg", "xcf", "jpg", "jpx", "png", "apng", "gif", "webp", "cr2", "tif", "bmp", "jxr", "psd", "ico", "heic", "avif",
}

VIDEO_FORMATS = {
    "3gp", "mp4", "m4v", "mkv", "webm", "mov", "avi", "wmv", "mpg", "flv",
}

EXTRA_FORMATS = {
    "jpeg", "svg", "webp",
}

ALLOWED_IMAGE_FORMATS = IMAGE_FORMATS.union(VIDEO_FORMATS).union(EXTRA_FORMATS)


def validate_image(filename):
    """
    Open and parse the file to determine its type
    :param filename: binary file to be analysed to determine its contents
    :type filename: str
    :return: The matched file type instance. Otherwise None.
    :rtype: str
    """
    try:
        kind = filetype.guess(filename)
    except FileNotFoundError as _error:
        print(f"{_error}")
        raise

    return f"{kind.extension}"


def generate_json(base64_encoded_image, image_format):
    """
    Create a JSON file containing the based64 encoded file
    :param base64_encoded_image: Base64 encoded text
    :type base64_encoded_image: str
    :param image_format: suffix, .png ...,  representing the encoded file type contents
    :type image_format: str
    :return: JSON formatted string
    :rtype: str
    """
    import time
    from datetime import datetime, timezone

    if image_format is None:
        raise TypeError(
            f"Unsupported image format, '{_image_format}', {ALLOWED_IMAGE_FORMATS}"
        )

    _now = datetime.now(timezone.utc)  # timezone aware datetime
    _epoch = int(time.mktime(_now.timetuple()))  # convert to epoch and cast to int
    _date_format = "%Y-%m-%dT%H:%M:%S%z"  # ISO8601 format
    _tstamp = (datetime.fromtimestamp(_epoch).replace(tzinfo=timezone.utc).strftime(_date_format))

    json_dict = {
        "type": image_format,
        "data": base64_encoded_image,
        "epoch": _epoch,
        "created": _tstamp,
    }
    return json.dumps(json_dict)


# --------------------------------------------------------------------------

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Base64 encode the image and create a JSON file",
        epilog="That's all Folks! ... Porky Pig",
    )
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument(
        "infile", nargs="?", type=argparse.FileType("rb"), default=sys.stdin
    )
    parser.add_argument(
        "outfile", nargs="?", type=argparse.FileType("w"), default=sys.stdout
    )

    args = parser.parse_args()

    if args.verbose >= 1:
        print(f"args: {args.__str__()}")

    try:
        _image_format = validate_image(args.infile)
        if _image_format not in ALLOWED_IMAGE_FORMATS:
            raise TypeError(
                f"Unsupported image format, '{_image_format}', {ALLOWED_IMAGE_FORMATS}"
            )

        encoded = base64.b64encode(args.infile.read()).decode("utf-8")

        json_str = generate_json(base64_encoded_image=encoded, image_format=_image_format)

        args.outfile.write(f"{json_str}")
        args.outfile.flush()
        args.outfile.close()
        args.infile.close()

        sys.exit(0)
    except ValueError as _value_error:
        print(f"{_value_error}")
    except TypeError as _type_error:
        print(f"{_type_error}")

    sys.exit(1)
