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
  * examples\interfaces.txt  - template file
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
  * examples\flintstones.txt  - template file
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
  * examples\rubbles.txt  - template file
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

* ``kitten.py`` - a simplistic UNIX `cat` example
* ``simple-cli.py`` - simple command line example for reading/writing files

**Note:** Add `#!/usr/bin/env python3` to the first line of the file to run on UNIX.

## UNIX epoch example

Utility for displaying a [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time) in UTC or local time-zone.

* ``unix-epoch.py`` - example for displaying a UNIX epoch in UTC or local time-zone

```console
PS1> python .\unix-epoch.py                  # 1734877954
PS1> python .\unix-epoch.py -i -e 1734877954 # 2024-12-22T15:32:34+0000
PS1> python .\unix-epoch.py -l -e 1734877954 # 2024-12-22 16:32:34 W. Europe Standard Time+0100
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
## Rhythmbox.xml file parser (unfinished)

* ``rhythmbox.py`` - (unfinished) rhythmbox.xml file parser

