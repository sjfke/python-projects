# python-projects

Collection of Simple Python Utility Scripts

## Simple Jinja Template merge

Useful references:

* [TTL255 - Przemek Rogala's blog Computer Networks, Python and Automation](https://github.com/progala/ttl255.com/tree/master/jinja2)
* [Jinja-2.11: Frequently Asked Questions](https://jinja.palletsprojects.com/en/2.11.x/faq/#why-is-it-called-jinja)
* [Jinja-2.11: Template Designer Documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/)
* [Primer on Jinja Templating](https://realpython.com/primer-on-jinja-templating/)

Files:

* ``jinja-cli.py`` - Python script

* Network interface example
    * examples\interfaces.txt - template file
    * examples\interfaces.json - parameters file
    * examples\interfaces.yaml - parameters file

```console
PS1> python .\jinja-cli.py -t .\examples\interfaces.txt -p .\examples\interfaces.json
PS1> python .\jinja-cli.py -t .\examples\interfaces.txt -p .\examples\interfaces.yaml
interface Ethernet1
  description leaf01-eth51
  ip address 10.50.0.0/31
interface Ethernet2
  description leaf02-eth51
  ip address 10.50.0.2/31
```

* Flintstones family example using an array
    * examples\flintstones.txt - template file
    * examples\flintstones.json - parameters file
    * examples\flintstones.yaml - parameters file

```console
PS1> python .\jinja-cli.py -t .\examples\flintstones.txt -p .\examples\flintstones.json
PS1> python .\jinja-cli.py -t .\examples\flintstones.txt -p .\examples\flintstones.yaml
FamilyName: flintstone
  Fred: 30 years old;
  Wilma: 25 years old;
  Pebbles: 1 years old;
  Dino: 5 years old;

FamilyName: Flintstone
      Fred: 30 years old;
     Wilma: 25 years old;
   Pebbles: 01 years old;
      Dino: 05 years old;
```

* Rubbles family example using key-value pairs
    * examples\rubbles.txt - template file
    * examples\rubbles.json - parameters file
    * examples\rubbles.yaml - parameters file

```console
PS1> python .\jinja-cli.py -t .\examples\rubbles.txt -p .\examples\rubbles.json
PS1> python .\jinja-cli.py -t .\examples\rubbles.txt -p .\examples\rubbles.yaml
FamilyName: rubbles
  barney: 29 years old;
  betty: 26 years old;
  bamm-bamm: 1 years old;
  hoppy: 2 years old;

FamilyName: Rubbles
    Barney: 29 years old;
     Betty: 26 years old;
 Bamm-bamm: 01 years old;
     Hoppy: 02 years old;
```

## Simple ArgParse example programs

Written to demonstrate how to use `argparse` to read from a positional file parameter or standard-in.

``simple-cli.py`` - simple command line example for reading/writing files

```console
PS1> python .\simple-cli.py .\examples\flintstones.json
001: {
002:         "family":"flintstone",
003:         "members":
004:                 [
005:                         {"Name":"Fred", "Age":30},
006:                         {"Name":"Wilma", "Age":25},
007:                         {"Name":"Pebbles", "Age":1},
008:                         {"Name":"Dino", "Age":5}
009:                 ]
010: }
```

``kitten.py`` - a simplistic UNIX `cat` example

```console
PS1> python .\kitten.py -n -f 3 -l 9 .\examples\flintstones.json
003:         "members":
004:                 [
005:                         {"Name":"Fred", "Age":30},
006:                         {"Name":"Wilma", "Age":25},
007:                         {"Name":"Pebbles", "Age":1},
008:                         {"Name":"Dino", "Age":5}
009:                 ]
```

**Note:** Add `#!/usr/bin/python3` or `#!/usr/bin/env python3` to the first line of the file to run directly from UNIX
command-line.

## UNIX epoch example

Utility for displaying a [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time) in UTC or local time-zone.

* ``unix-epoch.py`` - example for displaying a UNIX epoch in UTC or local time-zone

```console
PS1> python .\unix_epoch.py                  # 1734877954
PS1> python .\unix_epoch.py -i -e 1734877954 # 2024-12-22T15:32:34+0000
PS1> python .\unix_epoch.py -l -e 1734877954 # 2024-12-22 16:32:34 W. Europe Standard Time+0100
```

## Base64 binary file encoding and decoding

Restricted to common image and video file types, but could *easily* be extended to support other binary file types.

* ``image-to-json.py`` - reads and encodes binary file, wrapping its content in a JSON file
* ``json-to-image.py`` - extracts and decodes the binary data and writes it to a file

```console
PS1> python .\image-to-json.py .\examples\python-logo.png .\examples\python-logo.json
```

JSON file content

```json
  {
  "type": "png",
  "data": "<base64-encoded-content>",
  "epoch": 1735030251,
  "created": "2024-12-24T09:50:51+0000"
}
```

## Kitten

A simplistic version on UNIX `cat` command

```console
PS1> python .\kitten.py --help                         
usage: kitten.py [-h] [-n] [-f FIRST] [-l LAST] [-r] [-v] [filename]

Simple version of UNIX cat application

positional arguments:
  filename

options:
  -h, --help         show this help message and exit
  -n, --number       display line numbers
  -f, --first FIRST  first line to display
  -l, --last LAST    last line to display
  -r, --reverse      reverse contents
  -v, --verbose
```

Examples

```console
PS1> python .\kitten.py -n .\examples\fruits.xml       
001: <?xml version="1.0" encoding="UTF-8"?>
002: <fruits>
003:   <fruit><name>apple</name><color>green</color><price>1.20</price></fruit>
004:   <fruit><name>banana</name><color>yellow</color><price>0.5</price></fruit>
005:   <fruit><name>kiwi</name><color>green</color><price>1.25</price></fruit>
006: </fruits>
007:

PS1> python .\kitten.py -rn .\examples\fruits.xml
001: 
002: </fruits>
003:   <fruit><name>kiwi</name><color>green</color><price>1.25</price></fruit>
004:   <fruit><name>banana</name><color>yellow</color><price>0.5</price></fruit>
005:   <fruit><name>apple</name><color>green</color><price>1.20</price></fruit>
006: <fruits>
007: <?xml version="1.0" encoding="UTF-8"?>

PS1> python .\kitten.py -f 2 -l 6 .\examples\fruits.xml
<fruits>
  <fruit><name>apple</name><color>green</color><price>1.20</price></fruit>
  <fruit><name>banana</name><color>yellow</color><price>0.5</price></fruit>
  <fruit><name>kiwi</name><color>green</color><price>1.25</price></fruit>
</fruits>
```

## Python Objects

``Python`` objects do not support [encapsulation](https://en.wikipedia.org/wiki/Encapsulation_\(computer_programming\))
or **static type checking** unlike many object-oriented programming languages.

* It is possible to indicate that data is not intended to be modified by prefixing a variable with
  * ``_`` (underscore) or
  * ``__`` (double underscore).
* A constant value is indicated making it **UPPERCASE** and to show it should not be modified can be prefixed with
  * ``_`` (underscore) or 
  * ``__`` (double underscore)
* By convention ``getter`` and ``setter`` methods are discouraged.

It is recommended that [mypy](https://www.mypy-lang.org/) is used to check for **encapsulation violations** and
**static typing** because the ``Python`` language does not enforce it.

The following examples attempt to cover the most common approaches:

* [Person_Simple](./Person_Simple.py) illustrates attributes being accessed directly
* [Person_Attributes](./Person_Attributes.py) illustrates attributes created using ``property()``
* [Person_Decorators](./Person_Decorators.py) illustrates properties created using ``decorators``
* [Person_Encapsulation](./Person_Encapsulation.py) illustrates ``getter/setter`` approach

Running the ``pytest`` tests

```console
PS1> pip install pytest
PS1> pytest .\tests\test_person_simple.py -v
PS1> pytest .\tests\test_person_attributes.py -v
PS1> pytest .\tests\test_person_decorators.py -v
PS1> pytest .\tests\test_person_encapsulation.py -v
```

Checking for **encapsulation violations** and **static typing** errors

```console
PS1> pip install mypy
PS1> mypy .\Person_Simple.py 
PS1> mypy .\Person_Attributes.py 
PS1> mypy .\Person_Decorators.py 
PS1> mypy .\Person_Encapsulation.py 
```

Useful resources

* [Python's property(): Add Managed Attributes to Your Classes](https://realpython.com/python-property/)
* [Python Descriptors: An Introduction](https://realpython.com/python-descriptors/)
* [``pytest`` - Get Started](https://docs.pytest.org/en/stable/getting-started.html)
* [``mypy`` - Getting started](https://mypy.readthedocs.io/en/stable/getting_started.html)

## Rhythmbox.xml file parser (unfinished)

* ``rhythmbox.py`` - (unfinished) rhythmbox.xml file parser

## Pytest Testing

A series of `pytest` based test programs are being developed and will be stored in the `tests` sub-folder.

In order for tests to work the project folder needs to be in the Python search path, and the `tests` folder needs to 
be a package, that is, it must have an `__init.py__` for it to work directly from the command line.

* [Effective Python Testing With pytest](https://realpython.com/pytest-python-testing/)
* [pytest](https://docs.pytest.org/en/7.4.x/)
* [Pytest Plugin List](https://docs.pytest.org/en/stable/reference/plugin_list.html)
* [pytest import mechanisms and sys.path/PYTHONPATH](https://docs.pytest.org/en/stable/explanation/pythonpath.html)