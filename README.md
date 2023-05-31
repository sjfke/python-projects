# python-projects
 Collection of Simple Python Utility Scripts

## Simple Jinja Template merge

Based on examples from:
* [TTL255 - Przemek Rogala's blog Computer Networks, Python and Automation](https://github.com/progala/ttl255.com/tree/master/jinja2)
* [Jinja-2.11: Frequently Asked Questions](https://jinja.palletsprojects.com/en/2.11.x/faq/#why-is-it-called-jinja)
* [Jinja-2.11: Template Designer Documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/)
* [PyFormat Using % and .format() for great good!](https://pyformat.info/)

Files:

* ``jinja-cli.py`` - Python script

* Network interface example
  * tests\interfaces.txt  - template file
  * tests\interfaces.json - parameters file 
  * tests\interfaces.yaml - parameters file

* Flintstones family example using an array
  * tests\flintstones.txt  - template file
  * tests\flintstones.json - parameters file 
  * tests\flintstones.yaml - parameters file

* Rubbles family example using key-value pairs
  * tests\rubbles.txt  - template file
  * tests\rubbles.json - parameters file 
  * tests\rubbles.yaml - parameters file

## Simple ArgParse example programs

Written to demonstrate how to use `argparse` to read from a positional file parameter or standard-in.

* ``kitten.py`` - a simplistic UNIX `cat` example
* ``simple-cli.py`` - simple command line example for reading/writing files

**Note:** Add `#!/usr/bin/env python3` to the first line of the file to run on UNIX.

## UNIX epoch example

Utility for displaying a [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time) in UTC or local time-zone.

* ``unix-epoch.py`` - example for displaying a UNIX epoch in UTC or local time-zone

## Base64 binary file encoding and decoding

Restricted to common image and video file types, but could *easily* be extended to support other binary file types.

* ``image-to-json.py`` - reads and encodes binary file, wrapping its content in a JSON file
* ``json-to-image.py`` - extracts and decodes the binary data and writes it to a file

JSON file content

```json
  {
    "type": "png", 
    "data": "<base64-encoded-content>",
    "epoch": 1685547388, 
    "created": "2023-05-31T17:36:28+0000"
  }
```

## Rhythmbox.xml file parser (unfinished)

* ``rhythmbox.py`` - (unfinished) rhythmbox.xml file parser

