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

Utility returning a [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time) in UTC or local time-zone and to display an
epoch as a date string.

* ``utc-epoch.py`` - example for displaying a UNIX epoch in UTC or local time-zone

## Rhythmbox.xml file parser (unfinished)

* ``rhythmbox.py`` - (unfinished) rhythmbox.xml file parser

