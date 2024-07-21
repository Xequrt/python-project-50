# ***The difference calculator***
### Hexlet tests and linter status:
[![Actions Status](https://github.com/Xequrt/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Xequrt/python-project-50/actions)
### Maintainability Badge
[![Maintainability](https://api.codeclimate.com/v1/badges/039f234fb1e411827caa/maintainability)](https://codeclimate.com/github/Xequrt/python-project-50/maintainability)
### Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/039f234fb1e411827caa/test_coverage)](https://codeclimate.com/github/Xequrt/python-project-50/test_coverage)

### Description.
___
***The difference calculator*** - The program compares and finds 
differences between two data structures.

***Utility capabilities:***
+ Support for various input formats: yaml, json
+ Report generation in plain text, stylish, and json formats

### Example of use.
___
***🐫≠🐪Comparison of flat files (JSON)***

`gendiff file1.json file2.json`

The program compares and finds differences in the data structure in two JSON format files.

[![asciicast](https://asciinema.org/a/662259.svg)](https://asciinema.org/a/662259)

***🐫≠🐪Comparison of flat files (YML, YAML)***

`gendiff file1.yml file2.yml`

The program compares and finds differences in the data structure in two YML format files.

[![asciicast](https://asciinema.org/a/662584.svg)](https://asciinema.org/a/662584)

***🐫≠🐪Comparison of tree files (JSON, YML, YAML) with stylish formatter***

`gendiff stylish file1.yaml file2.yaml`

The program compares two data structures and finds the differences between them with stylish formatter. JSON and YAML formats have a recursive structure. 

[![asciicast](https://asciinema.org/a/667774.svg)](https://asciinema.org/a/667774)

***🐫≠🐪Comparison of tree files (JSON, YML, YAML) with plain formatter***

`gendiff plain file1.yaml file2.json`

The program compares two data structures and finds the differences between them with plain formatter. JSON and YAML formats have a recursive structure.

[![asciicast](https://asciinema.org/a/669037.svg)](https://asciinema.org/a/669037)

***🐫≠🐪Comparison of tree files (JSON, YML, YAML) with json formatter***

`gendiff json file1.json file2.json`

The program compares two data structures and finds the differences between them with json formatter. JSON and YAML formats have a recursive structure.

[![asciicast](https://asciinema.org/a/669052.svg)](https://asciinema.org/a/669052)
